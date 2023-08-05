import paho.mqtt.client as paho
from paho import mqtt
import time
import random

broker = "mqtt-dashboard.com"
port = 1883
timeout = 60
topic = "mentor/angga/week9"


def getRandom():
    #disini bisa di isi dengan sensor kalian -> Example 
    return random.randrange(30, 100, 3)


def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))


def publishPeriod():
    while True:
        getData = getRandom()
        client.publish(topic, payload=getData, qos=1, retain=False)
        time.sleep(1)

def run():
    publishPeriod()

client = paho.Client("Contoh")  # Tidak Boleh Sama
# client.tls_set(tls_version=mqtt.client.ssl.PROTOCOL_TLS)
client.on_connect = on_connect

client.connect(broker, port, timeout)

run()
