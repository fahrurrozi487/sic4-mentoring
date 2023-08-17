import paho.mqtt.client as paho
from paho import mqtt
import json
from random import randint
import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

# Define GPIO pins for trigger and echo
trig_pin = 21 # sesuaikan pin
echo_pin = 20 # sesuaikan pin

# Set up GPIO pins
GPIO.setup(trig_pin, GPIO.OUT)
GPIO.setup(echo_pin, GPIO.IN)
# define static variable
# broker = "mqtt-dashboard.com"
broker = "industrial.api.ubidots.com"
port = 1883
timeout = 60

username = 'BBFF-JwhfZjHhOhkAoH4jq2bcVAl2IEF76r'
# username = ''
password = ''
# topic default "/v2.0/devices/label-devices"
publish = "/v2.0/devices/sweet-unicorn"

def measure_distance():
    # Send a short pulse to the trigger pin (10 microseconds)
    GPIO.output(trig_pin, GPIO.HIGH)
    time.sleep(0.00001)
    GPIO.output(trig_pin, GPIO.LOW)

    # Measure the time taken for the pulse to travel back and forth
    while GPIO.input(echo_pin) == GPIO.LOW:
        pulse_start_time = time.time()

    while GPIO.input(echo_pin) == GPIO.HIGH:
        pulse_end_time = time.time()

    pulse_duration = pulse_end_time - pulse_start_time

    # Calculate the distance using the speed of sound (34300 cm/s)
    # and considering the pulse traveled to the object and back
    distance_cm = (pulse_duration * 34300) / 2

    return distance_cm

def getDataSensor1():
    #codingan sensor

    #
    hasil_sensor = randint(0,100)
    return hasil_sensor

def getDataSensor2():
    #codingan sensor
    hasil_sensor = randint(0,100)
    if(hasil_sensor > 50):
        hasil_sensor = 1
    else:
        hasil_sensor = 0
    return hasil_sensor

def on_connect(client, userdata, flag, rc):
    print("Connected with result code "+str(rc))

def on_publish(client, userdata, result):
    print("data published \n")


def run():
    while True:
        sensor1 = measure_distance()
        sensor2 = getDataSensor2()
        latidude = -6.3124254
        longitude = 106.7516467
        #dapet GPS
        json_temp = {'ultrasonik':sensor1,'pir':sensor2, "location":{"value":0,"context":{"lat": latidude, "lng": longitude}}}
        payload = json.dumps(json_temp, indent=4)
        client.publish(publish,payload,qos=1)
        time.sleep(20)

        
client = paho.Client("Mentoring", userdata=None) #client ID tidakboleh sama
client.username_pw_set(username=username, password=password)
client.on_connect = on_connect
client.on_publish = on_publish
client.connect(broker, port, timeout)
# client.loop_forever()
#menjalankan periodic pengiriman Data
run()



