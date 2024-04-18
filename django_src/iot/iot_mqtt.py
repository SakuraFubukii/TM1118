import paho.mqtt.client as mqtt
from .models import Event
import json
from datetime import datetime
import smtplib
from email.mime.text import MIMEText

mqtt_broker = "broker.hivemq.com"
mqtt_port = 1883
mqtt_qos = 1
mqtt_topic = "iot/sensor-AB"

def mqtt_on_message(client, userdata, msg):
    d_msg = str(msg.payload.decode("utf-8"))
    iotData = json.loads(d_msg)
    
    print("Received message on topic %s : %s" % (msg.topic, iotData))

    if(int(iotData["snd"]) > 10):
        mail_host = 'smtp.qq.com'  
        mail_user = '3014171139'  
        mail_pass = 'gjuhlxpzhteudfgj'   
        sender = '3014171139@qq.com'  
        receivers = ['me@wzt.email']  

        message = MIMEText('content','plain','utf-8')     
        message['Subject'] = 'title' 
        message['From'] = sender     
        message['To'] = receivers[0]  

        try:
            smtpObj = smtplib.SMTP() 
            smtpObj.connect(mail_host,25)
            smtpObj.login(mail_user,mail_pass) 
            smtpObj.sendmail(
                sender,receivers,message.as_string()
            ) 
            smtpObj.quit() 
            print('success')
        except smtplib.SMTPException as e:
            print('error',e)

    p = Event(node_id=iotData["node_id"], loc=iotData["loc"], temp=iotData["temp"] ,hum = iotData["hum"], light = iotData["light"], snd = iotData["snd"], time = datetime.now())
    p.save()

mqtt_client = mqtt.Client("django-B05") # Create a Client Instance
mqtt_client.on_message = mqtt_on_message
mqtt_client.connect(mqtt_broker, mqtt_port)

 # Establish a connection to a broker
print("Connect to MQTT broker")
mqtt_client.subscribe(mqtt_topic, mqtt_qos)

mqtt_client.loop_start()