import paho.mqtt.client as mqtt

def on_message(client, userdata, message):
    print(f"Received message: {message.payload.decode()} on topic {message.topic}")

broker_address = "test.mosquitto.org"
client = mqtt.Client("subscriber")
client.on_message = on_message

client.connect(broker_address)
client.subscribe("home/temperature")  # Subscribe to the same topic
client.loop_forever()
