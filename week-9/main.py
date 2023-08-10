import paho.mqtt.client as paho
from paho import mqtt
import time
import random
import json

broker = "mqtt-dashboard.com"
port = 1883
timeout = 60
data1 = "ta/angga/data1"
data2 = "ta/angga/data2"

def getRandom():
    #disini bisa di isi dengan sensor kalian -> Example 
    return random.randrange(30, 100, 3)


def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))


def publishPeriod():
    while True:
        data = {'data1':getRandom(),'data2':getRandom()}
        payload = json.dumps(data)
        client.publish(data1, payload=getRandom(), qos=1, retain=False)
        client.publish(data2, payload=getRandom(), qos=1, retain=False)
        time.sleep(10)

def run():
    publishPeriod()

client = paho.Client("anggata")  # Tidak Boleh Sama
# client.tls_set(tls_version=mqtt.client.ssl.PROTOCOL_TLS)
client.on_connect = on_connect

client.connect(broker, port, timeout)

run()
