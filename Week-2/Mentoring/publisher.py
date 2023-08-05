import paho.mqtt.client as paho
from paho import mqtt
import time
import datetime
import random
import json

broker = "mqtt-dashboard.com"
port = 1883
timeout = 60


def createJson():
    presentDate = datetime.datetime.now()
    unix_timestamp = datetime.datetime.timestamp(presentDate)*1000
    dictionary = {'temperature': random.randrange(
        30, 100, 3), 'humidity': random.randrange(50, 80, 2), 'timestamp': unix_timestamp}
    jsonString = json.dumps(dictionary, indent=4)
    return jsonString


def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))


def publishPeriod():
    while True:
        pay = createJson()
        print(pay)
        client.publish("mentor/angga/week2",
                       payload=pay, qos=1, retain=False)
        time.sleep(10)

def run():
    publishPeriod()

client = paho.Client("Contoh")  # Tidak Boleh Sama
# client.tls_set(tls_version=mqtt.client.ssl.PROTOCOL_TLS)
client.on_connect = on_connect

client.connect(broker, port, timeout)

run()
