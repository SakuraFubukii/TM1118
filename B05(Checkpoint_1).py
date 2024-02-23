import RPi.GPIO as GPIO
import paho.mqtt.client as mqtt
import time
from RPLCD.i2c import CharLCD
import Adafruit_DHT
import Adafruit_ADS1x15
import json
import math

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
output_channel = [18, 23, 24, 25, 8]
GPIO.setup(output_channel, GPIO.OUT, initial=GPIO.LOW)

lcd = CharLCD('PCF8574', 0x27)
adc= Adafruit_ADS1x15.ADS1115()
DHT_SENSOR = Adafruit_DHT.DHT11
DHT_PIN = 4
mqtt_broker = 'broker.hivemq.com'
mqtt_port = 1883
mqtt_qos = 1
GAIN=1
lcd.cursor_pos = (0,0)
lcd.write_string("TEAM B05 Node")
lcd.cursor_pos = (1,0)
lcd.write_string("Now Operating!")

mqtt_topic = 'iot/sensor-B05'
mqtt_client = mqtt.Client('B05')
mqtt_client.connect(mqtt_broker,mqtt_port)
mqtt_client.subscribe(mqtt_topic,mqtt_qos)

def mqtt_on_message(client,userdata,msg):
    d_msg = str(msg.payload.decode('utf-8'))
    
def convert_to_percentage(sensor_value, min_value, max_value):
    percentage = ((sensor_value - min_value) / (max_value - min_value)) * 100
    return round(percentage, 2)

def adc_to_db(adc_value, max_adc_value, db_reference):
    voltage_ratio = adc_value / max_adc_value
    db_value = 20 * math.log10(voltage_ratio) + db_reference
    return round(db_value,2)


mqtt_client.on_message = mqtt_on_message
mqtt_client.loop_start()

while True:
    for i in range(len(output_channel)):
        GPIO.output(output_channel[i], GPIO.HIGH)
        time.sleep(0.5)
        GPIO.output(output_channel[i], GPIO.LOW)
    humidity, temperature = Adafruit_DHT.read_retry(DHT_SENSOR, DHT_PIN)
    adc_value= adc.read_adc(2,gain=GAIN)
    sensor_value = adc.read_adc(3, gain=GAIN)
    light = convert_to_percentage(sensor_value, 1000, 26000)
    snd = adc_to_db(adc_value, 1300, 80)
    
    temperature= str(temperature)
    humidity= str(humidity)
    light= str(light)
    snd= str(snd)
    message = {"node_id": "B05","loc": "W311-H1","temp": temperature, "hum": humidity, "light": light,"snd": snd}
    message = json.dumps(message)
    print(message)
    mqtt_client.publish(mqtt_topic, message, mqtt_qos)
    print()
    
    time.sleep(0.01)
            
