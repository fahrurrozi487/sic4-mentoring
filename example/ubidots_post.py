import time
import requests
import random

TOKEN = "BBFF-HRGwpx4IeRlvLnblG1tRny0YehPjWz"
DEVICE_LABEL = "demo"
TEMPERATURE_LABEL = "temperature"
HUMIDITY_LABEL = "humidity"

def kirim():
    temperature_value = round(random.uniform(-10, 50), 2)
    humidity_value = round(random.uniform(0, 100), 2)

    payload = {
        TEMPERATURE_LABEL: temperature_value,
        HUMIDITY_LABEL: humidity_value
    }

    url = f"http://industrial.api.ubidots.com/api/v1.6/devices/{DEVICE_LABEL}"
    headers = {"X-Auth-Token": TOKEN, "Content-Type": "application/json"}

    try:
        response = requests.post(url=url, headers=headers, json=payload)
        if response.status_code == 200:
            print(f"Data sent to Ubidots: Temperature={temperature_value}, Humidity={humidity_value}")
        else:
            print("Failed to send data. Status code:", response.status_code)
    except requests.exceptions.RequestException as e:
        print("Connection error:", e)

if __name__ == "__main__":
    while True:
        kirim()
        time.sleep(0.5)