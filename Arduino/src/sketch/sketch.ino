// Incluimos Arduino
#include <Arduino.h>

// Definimos el pin del LED
const uint8_t PIN_LED = 13;

void setup()
{
  pinMode(PIN_LED, OUTPUT);
  digitalWrite(PIN_LED, LOW);
}

void loop()
{
  digitalWrite(PIN_LED, HIGH);
  delay(500);
  digitalWrite(PIN_LED, LOW);
  delay(500);
}
