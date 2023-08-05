import paho.mqtt.client as paho
from paho import mqtt
import json
broker = "mqtt-dashboard.com"
port = 1883 #tls 
timeout = 60

topic = "A"



def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    client.subscribe(topic, qos=0)


def on_message(client, userdata, msg):
    print("Topic :"+msg.topic+"\nMessage:"+str(msg.payload.decode('utf-8')))
    messageMqtt = json.loads(msg.payload.decode('utf-8'))
    print(f"M MQTT - > {messageMqtt}")
    print(f"Temperature : {messageMqtt['temperature']}")

client = paho.Client("client 2")
# client.tls_set(tls_version=mqtt.client.ssl.PROTOCOL_TLS)
client.on_connect = on_connect #Callback
client.on_message = on_message

client.connect(broker, port, timeout)

client.loop_forever()
