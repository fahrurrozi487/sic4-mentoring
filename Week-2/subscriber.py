import paho.mqtt.client as paho
from paho import mqtt

# define static variable
# broker = "mqtt-dashboard.com"
broker = "industrial.api.ubidots.com"
port = 1883
timeout = 60

username = 'BBFF-JwhfZjHhOhkAoH4jq2bcVAl2IEF76r'
# username = ''
password = ''
# topic = "test_topic/1"
topic = "/v2.0/devices/example"

def on_connect(client, userdata, flag, rc):
    print("Connected with result code "+str(rc))
    client.publish(topic, '{"temperature":12}', qos=1) 

def on_publish(client, userdata, result):
    print("data published \n")

client = paho.Client("d01", userdata=None) #client ID name
client.username_pw_set(username=username, password=password)
client.on_connect = on_connect
client.on_publish = on_publish
client.connect(broker, port, timeout)
client.loop_forever()