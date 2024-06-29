#include <DHT.h>

#define DHTPIN 2  // Pin where the DHT22 sensor is connected
#define DHTTYPE DHT22

DHT dht(DHTPIN, DHTTYPE);
const int ledPin = 13;  // Pin for the LED actuator

void setup() {
  Serial.begin(9600);
  dht.begin();
  pinMode(ledPin, OUTPUT);
}

void loop() {
  delay(2000);  // Wait for 2 seconds between readings

  float temperature = dht.readTemperature();
  float humidity = dht.readHumidity();

  Serial.print("Temperature (°C): ");
  Serial.println(temperature);
  Serial.print("Humidity (%): ");
  Serial.println(humidity);

  // Example actuation: Turn on LED if temperature exceeds 25°C
  if (temperature > 25) {
    digitalWrite(ledPin, HIGH);
  } else {
    digitalWrite(ledPin, LOW);
  }
}
