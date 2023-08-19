import paho.mqtt.client as paho
from paho import mqtt
import json
from random import randint
import time
import RPi.GPIO as GPIO

GPIO_LAMPU = 18


GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(GPIO_LAMPU,GPIO.OUT)
# define static variable
# broker = "mqtt-dashboard.com"
broker = "industrial.api.ubidots.com"
port = 1883
timeout = 60

username = 'BBFF-JwhfZjHhOhkAoH4jq2bcVAl2IEF76r'
# username = ''
password = ''
# topic default "/v2.0/devices/label-devices"
publish = "/v2.0/devices/mentoring"
subscribe = "/v2.0/devices/mentoring/#"
# topic default "/v2.0/devices/label-devices/varibale-label"
lampu = "/v2.0/devices/mentoring/lampu"
kulkas = "/v2.0/devices/mentoring/kulkas"

listrik = "/v2.0/devices/mentoring/listrik"

def menyalakanrelay(data_lampu):
    if(data_lampu == 1):
        print("menyalakan lampu")
        GPIO.output(GPIO_LAMPU,GPIO.HIGH)
    else:
        print("mematikan lampu")
        GPIO.output(GPIO_LAMPU,GPIO.LOW)

def menyalakan_kulkas(data_kulkas):
    if(data_kulkas == 1):
        print("menyalakan kulkas")
    else:
        print("mematikan kulkas")

def menyalakan_listrik(data_Listrik):
    if(data_Listrik == 1):
        print("menyalakan Listrik")
        #GPIO MENYALAKAN
    else:
        print("mematikan Listrik")
        #GPIO MATIKAN

def on_connect(client, userdata, flag, rc):
    print("Connected with result code "+str(rc))
    client.subscribe(subscribe,qos=1)

def on_publish(client, userdata, result):
    print("data published \n")

def on_message(client, userdata, msg):
    print("Topic :"+msg.topic+"\nMessage:"+str(msg.payload.decode('utf-8')))
    if(msg.topic == lampu):
        data = json.loads(msg.payload.decode('utf-8'))
        menyalakanrelay(data['value'])
    elif(msg.topic == kulkas):
        data = json.loads(msg.payload.decode('utf-8'))
        menyalakan_kulkas(data['value'])
    elif(msg.topic == listrik):
        data = json.loads(msg.payload.decode('utf-8'))
        menyalakan_listrik(data['value'])
    

client = paho.Client("Mentoring", userdata=None) #client ID tidakboleh sama
client.username_pw_set(username=username, password=password)
client.on_connect = on_connect
client.on_publish = on_publish
client.on_message = on_message
client.connect(broker, port, timeout)
client.loop_forever()




