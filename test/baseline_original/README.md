# Baseline – Antena Original de Fábrica

**Data:** 30/06/2026

## Descrição

Este diretório contém os dados brutos coletados do ESP32 utilizando a antena original integrada à placa (**PCB Trace Antenna**). Esses dados representam a linha de base (_baseline_) do experimento e serão utilizados como referência para comparação com os testes realizados utilizando uma antena dipolo externa.

---

## 1. Objetivo

Estabelecer a linha de base (_baseline_) da recepção de sinal do ESP32 utilizando a antena original integrada à placa (PCB Trace Antenna). Os resultados obtidos servirão como referência para comparação quantitativa com os testes realizados utilizando uma antena dipolo externa.

---

## 2. Parâmetros do Teste

| Parâmetro             | Valor                                    |
| --------------------- | ---------------------------------------- |
| **Local**             | Mesa de trabalho (ambiente doméstico)    |
| **Tempo de captura**  | Aproximadamente 3 minutos                |
| **Formato dos dados** | JSON bruto coletado via interface serial |

---

## 3. Observações Técnicas

- O sistema apresentou funcionamento estável durante toda a varredura de redes Wi-Fi na faixa de **2,4 GHz**.
- Para a rede de referência **"LINKCE BATCAVERNA"**, o nível médio de sinal (**RSSI**) observado foi de aproximadamente **-40 dBm**.
- Não foram observadas oscilações críticas de conexão durante as medições realizadas.

---

## 4. Evidências (Logs de Execução)

Abaixo estão trechos do log do servidor Python, confirmando a estabilidade na captura e no processamento dos pacotes JSON durante o experimento.

```text
SUCESSO: 12 redes identificadas e enviadas para o Dashboard!
127.0.0.1 - - [30/Jun/2026 03:46:47] "GET /dados HTTP/1.1" 200 -

SUCESSO: 14 redes identificadas e enviadas para o Dashboard!

SUCESSO: 10 redes identificadas e enviadas para o Dashboard!

SUCESSO: 13 redes identificadas e enviadas para o Dashboard!
127.0.0.1 - - [30/Jun/2026 03:47:47] "GET /dados HTTP/1.1" 200 -

SUCESSO: 8 redes identificadas e enviadas para o Dashboard!
127.0.0.1 - - [30/Jun/2026 03:47:54] "GET /dados HTTP/1.1" 200 -

SUCESSO: 4 redes identificadas e enviadas para o Dashboard!
127.0.0.1 - - [30/Jun/2026 03:48:14] "GET /dados HTTP/1.1" 200 -

SUCESSO: 8 redes identificadas e enviadas para o Dashboard!
127.0.0.1 - - [30/Jun/2026 03:48:24] "GET /dados HTTP/1.1" 200 -

SUCESSO: 7 redes identificadas e enviadas para o Dashboard!
127.0.0.1 - - [30/Jun/2026 03:48:44] "GET /dados HTTP/1.1" 200 -
```

> **Nota:** O log completo da captura está disponível no arquivo **`capturas.json`** presente nesta mesma pasta.

---

## 5. Conclusão

Os dados obtidos constituem a linha de base (_baseline_) do experimento e serão utilizados para comparar o desempenho de recepção do ESP32 após a substituição da antena original por uma **antena dipolo externa de 3,1 cm**.

A comparação permitirá avaliar quantitativamente possíveis ganhos de:

- Sensibilidade de recepção (RSSI);
- Quantidade de redes detectadas;
- Estabilidade da recepção;
- Diretividade e desempenho geral da nova antena.
