import paho.mqtt.client as mqtt
import json
import time
#全局变量
id = 'a3fbee76-fa78-4268-8127-a8cdd2b72c61'
client_name = id + 'nightlight_client'

mqtt_client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION1,client_name)
mqtt_client.connect('test.mosquitto.org',port=1883)

mqtt_client.loop_start()
print("MQTT connected!")

client_telemetry_topic = id + '/telemetry'

while True:
    light = 100
    telemetry = json.dumps({'light' : light})

    print("Sending telemetry ", telemetry)
    mqtt_client.publish(client_telemetry_topic, telemetry)
    time.sleep(5)