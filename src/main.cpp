#include <Arduino.h>
#include "WiFi.h"

void setup()
{
  Serial.begin(115200);
  WiFi.mode(WIFI_STA);
  WiFi.disconnect();
  delay(100);
}

void loop()
{
  int n = WiFi.scanNetworks();
  if (n > 0)
  {
    Serial.println("[");
    for (int i = 0; i < n; ++i)
    {
      int canal = WiFi.channel(i);
      int freq = 2407 + (canal * 5);

      Serial.print("  {\"ssid\": \"");
      Serial.print(WiFi.SSID(i));
      Serial.print("\", \"rssi\": ");
      Serial.print(WiFi.RSSI(i));
      Serial.print(", \"canal\": ");
      Serial.print(canal);
      Serial.print(", \"freq\": ");
      Serial.print(freq);
      Serial.print("}");

      if (i < n - 1)
      {
        Serial.println(",");
      }
      else
      {
        Serial.println("");
      }
    }
    Serial.println("]");
  }
  else
  {
    Serial.println("[]");
  }

  delay(10000);
}