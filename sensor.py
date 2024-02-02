import paho.mqtt.client as mqtt
import time
import Adafruit_DHT
import Adafruit_ADS1x15
import math


import json

from RPLCD.i2c import CharLCD


sensorId = "5"
locationVal = "w502g"


def lcdDisplay(a, v):
    lcd = CharLCD("PCF8574", 0x27)
    lcd.backlight_enabled = True
    lcd.clear()
    lcd.cursor_pos = (0,0)
    if a == "T":
        lcd.write_string("Temperature")
    elif a == "H":
        lcd.write_string("Humidity")
    lcd.cursor_pos = (1,0)
    lcd.write_string(v)
    time.sleep(2)
    lcd.clear()
    lcd.backlight_enabled = False



def execute():
    DHT_SENSOR = Adafruit_DHT.DHT11
    DHT_PIN = 4
    adc = Adafruit_ADS1x15.ADS1015()
    values2 = adc.read_adc(2, gain=4) 
    values3 = adc.read_adc(3, gain=1)      
           
    humidity, temperature = Adafruit_DHT.read_retry(DHT_SENSOR, DHT_PIN)
    light = int((values3-326)/(1500-326)*100)
    snd = int(20*math.log10((values2+0.1)/5200))+80
    publishMsg = {"node_id" : sensorId, "loc" : locationVal, "temp" : temperature, "hum" : humidity, "light" : light, "snd":snd}
    print(publishMsg)
    client.publish("iot/sensor", json.dumps(publishMsg))
    


def on_connect(client, userdata, flags, rc):

    client.subscribe("iot/sensor")

def on_message(client, userdata, msg):
    execute()
   
    
client = mqtt.Client()

client.on_connect = on_connect
client.on_message = on_message

client.connect("ia.ic.polyu.edu.hk", 1883)
client.loop_forever()

while True:
    execute()
    time.sleep(1000)
