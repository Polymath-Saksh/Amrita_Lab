import paho.mqtt.client as mqtt

broker_address = "test.mosquitto.org"  # Use any public MQTT broker
client = mqtt.Client("publisher")
client.connect(broker_address)
client.publish("home/temperature", "25.5")  # Publish a temperature value
client.disconnect()
