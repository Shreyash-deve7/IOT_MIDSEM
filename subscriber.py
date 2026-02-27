import paho.mqtt.client as mqtt

broker_address = "broker.hivemq.com"
topic_name = "security/face_alert"

# Function when message is received
def on_message(client, userdata, message):
    received_message = message.payload.decode()
    print("Received Alert:", received_message)

client = mqtt.Client()
client.connect(broker_address, 1883, 60)

client.subscribe(topic_name)

client.on_message = on_message

print("Waiting for alerts...")

client.loop_forever()

