import paho.mqtt.client as paho
from paho import mqtt
broker = "broker.hivemq.com"
port = 1883
timeout = 60

def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    client.publish("mentor/angga/pubsher", "Halo {nama}, selamat Pagi")


client = paho.Client("publisher")
# client.tls_set(tls_version=mqtt.client.ssl.PROTOCOL_TLS)
client.on_connect = on_connect

client.connect(broker, port, timeout)

client.loop_forever()
