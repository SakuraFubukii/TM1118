import paho.mqtt.client as mqtt
from .models import Event
import json

mqtt_broker = "broker.hivemq.com" # Broker
mqtt_port = 1883 # Default
mqtt_qos = 1 # Quality of Service = 1
mqtt_topic = "good"

def mqtt_on_message(client, userdata, msg):
    d_msg = str(msg.payload.decode("utf-8"))
    Data = json.loads(d_msg)
    
    print("Received message on topic %s : %s" % (msg.topic, Data))
    p = Event(people_num = iotData["Number of People"])
    p.save()

mqtt_client = mqtt.Client("django-B05")
mqtt_client.on_message = mqtt_on_message
mqtt_client.connect(mqtt_broker, mqtt_port)

print("Connect to MQTT broker")
mqtt_client.subscribe(mqtt_topic, mqtt_qos)

mqtt_client.loop_start()