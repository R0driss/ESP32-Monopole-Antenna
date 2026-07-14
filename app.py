from flask import Flask, render_template, jsonify
import serial
import json
import threading
import time

app = Flask(__name__)

PORTA = '/dev/ttyUSB0'
BAUD_RATE = 115200

dados_wifi = []

def ler_serial():
    global dados_wifi
    porta_serial = None
    buffer = ""
    lendo_json = False
    
    while True:
        try:
            if porta_serial is None or not porta_serial.is_open:
                porta_serial = serial.Serial(PORTA, BAUD_RATE, timeout=1)
                
            if porta_serial.in_waiting > 0:
                linha = porta_serial.readline().decode('utf-8', errors='ignore').strip()
                
                # Só começa a gravar quando achar a abertura do JSON
                if linha == "[":
                    buffer = "["
                    lendo_json = True
                elif lendo_json:
                    buffer += linha
                    # Finaliza a gravação e tenta converter
                    if linha == "]":
                        try:
                            dados_wifi = json.loads(buffer)
                            print(f"\n SUCESSO: {len(dados_wifi)} redes identificadas e enviadas para o Dashboard!")
                        except json.JSONDecodeError:
                            print("\n AVISO: Pacote corrompido, aguardando próxima leitura...")
                            
                        lendo_json = False
                        buffer = ""
                        
        except (serial.SerialException, OSError):
            if porta_serial:
                porta_serial.close()
            time.sleep(2)
        except Exception:
            time.sleep(1)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/dados')
def dados():
    return jsonify(dados_wifi)

if __name__ == '__main__':
    t = threading.Thread(target=ler_serial)
    t.daemon = True
    t.start()
    # O use_reloader=False evita que o Flask abra a porta serial duas vezes
    app.run(debug=True, port=5000, use_reloader=False)