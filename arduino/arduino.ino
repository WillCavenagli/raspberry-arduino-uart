#include <Adafruit_Sensor.h>
#include <DHT.h>
#define DHTPIN 7
#define LEDPIN 8
#define DHTTYPE DHT22

DHT dht(DHTPIN, DHTTYPE);

int incomingByte = 0;

void setup() 
{
  Serial.begin(9600);
  pinMode(LEDPIN, OUTPUT);
  dht.begin();
}

void loop()
{
  delay(1000);
  
  float t = dht.readTemperature();

  if (isnan(t))
  {
    Serial.println("Falha ao ler dados do sensor DHT !!!");
    return;
  }

  Serial.println(t);
  
  while (Serial.available() > 0) {
   
    incomingByte = Serial.read();
  
    if (incomingByte > 0) {
      digitalWrite(LEDPIN, HIGH);
    } else {
      digitalWrite(LEDPIN, LOW);
    }
  }
}
