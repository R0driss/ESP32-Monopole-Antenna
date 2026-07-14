# ESP32 RF Dipole Analysis System

Sistema de monitoramento e análise de propagação de sinais Wi-Fi em **2,4 GHz**, desenvolvido para avaliar o desempenho de uma **antena dipolo externa** em comparação com a **antena original de fábrica (PCB Trace Antenna)** do ESP32.

---

## Objetivo

Este projeto tem como objetivo desenvolver uma ferramenta de **site survey Wi-Fi** de baixo custo, capaz de monitorar em tempo real a intensidade do sinal (**RSSI**) das redes sem fio próximas.

A aplicação permite realizar experimentos controlados para comparar quantitativamente o desempenho da antena original do ESP32 com uma antena dipolo externa, utilizando visualização gráfica e armazenamento dos dados coletados.

---

## Arquitetura do Sistema

O sistema é composto por três camadas principais.

### Hardware e Firmware (ESP32)

- Varredura de redes Wi-Fi utilizando a biblioteca `WiFi.h`;
- Coleta dos valores de RSSI das redes detectadas;
- Serialização dos dados em formato **JSON**;
- Envio contínuo das informações pela interface serial.

### Back-end (Python + Flask)

- Comunicação com o ESP32 através da porta serial;
- Processamento dos dados recebidos em JSON;
- Tratamento de mensagens de inicialização (_boot_) e possíveis erros de leitura;
- Disponibilização dos dados para o dashboard via API HTTP.

### Front-end (Dashboard Web)

- Interface desenvolvida com **HTML**, **JavaScript** e **Chart.js**;
- Atualização automática dos gráficos em tempo real;
- Visualização da evolução temporal do RSSI das redes monitoradas;
- Comparação visual da estabilidade do sinal durante os testes.

---

## Metodologia Experimental

O experimento foi dividido em três etapas.

### 1. Baseline

Coleta de dados utilizando exclusivamente a antena original integrada ao ESP32 (**PCB Trace Antenna**).

### 2. Modificação Física

Substituição da antena original por uma **antena dipolo externa de aproximadamente 3,1 cm**, dimensionada para operação na faixa de **2,4 GHz**.

### 3. Análise Comparativa

Comparação dos resultados obtidos antes e depois da modificação, considerando métricas como:

- Intensidade média do sinal (RSSI);
- Quantidade de redes detectadas;
- Estabilidade das medições;
- Possível ganho de recepção da antena modificada.

Os conjuntos de dados utilizados na análise encontram-se na pasta **`/test`**.

---

## Estrutura do Projeto

```text
.
├── app.py                 # Servidor Flask
├── templates/             # Interface Web
├── static/                # CSS e JavaScript
├── test/
│   ├── baseline/          # Dados com antena original
│   └── dipole/            # Dados com antena dipolo
├── capturas.json          # Dados coletados
└── README.md
```

---

## Como Executar

### 1. Instale as dependências

```bash
pip install flask pyserial
```

### 2. Conecte o ESP32

Verifique a porta serial utilizada pelo dispositivo e ajuste-a no arquivo **`app.py`**, caso necessário.

### 3. Execute o servidor

```bash
python app.py
```

### 4. Abra o Dashboard

Acesse no navegador:

```
http://127.0.0.1:5000
```

---

## Tecnologias Utilizadas

- ESP32
- Arduino Framework
- WiFi.h
- Python
- Flask
- PySerial
- HTML5
- JavaScript
- Chart.js

---

## Contexto Acadêmico

Projeto desenvolvido para a disciplina **Ondas e Antenas** da **Universidade Federal do Ceará (UFC) – Campus Quixadá**.

O objetivo é validar experimentalmente o impacto da substituição da antena original do ESP32 por uma antena dipolo externa, utilizando técnicas de medição, aquisição de dados e análise gráfica em tempo real.

---

## Licença

Este projeto foi desenvolvido para fins acadêmicos e de pesquisa.
