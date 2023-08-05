import paho.mqtt.client as paho

broker = "mqtt-dashboard.com"
port = 1883
timeout = 60

def ketika_connect(client, userdata, flags, rc):
    print("Connected to MQTT with result code "+str(rc))
    client.publish("A","Kirim Pertama")

def ketika_publish():
    print("data terkirim")

client = paho.Client("Client1") 

client.on_connect = ketika_connect

# client.on_publish = ketika_publish

client.connect(broker, port, timeout)

client.loop_forever()