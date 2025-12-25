import json
import time

import paho.mqtt.client as mqtt

id = 'a3fbee76-fa78-4268-8127-a8cdd2b72c61'

client_telemetry_topic = id + '/telemetry'
client_name = id + 'nightlight_server'

mqtt_client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION1,client_name)
mqtt_client.connect('test.mosquitto.org',1883)
mqtt_client.loop_start()

def handle_telemetry(client, userdata, message):
    payload = json.loads(message.payload.decode())
    print("Message received:", payload)

mqtt_client.subscribe(client_telemetry_topic)
mqtt_client.on_message = handle_telemetry

while True:
    time.sleep(2)