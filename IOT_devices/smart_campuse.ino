//IOT motion sensor

#include <WiFi.h>               // Wifi driver
#include <PubSubClient.h>       // MQTT server library
#include <ArduinoJson.h>        // JSON library
#include <M5StickC.h>
#define ID 9

// MQTT and WiFi set-up
WiFiClient espClient;
PubSubClient client(espClient);

const char *ssid = "EIA-W311MESH";      // Your SSID             
const char *password = "42004200";  // Your Wifi password
const char *mqtt_server = "broker.hivemq.com"; // MQTT server name
char *mqttTopic = "IC/123";
char *mqttTopic1 = "iot/sensor-AB";

float accX = 0.0F;
float accY = 0.0F;
float accZ = 0.0F;

float gyroX = 0.0F;
float gyroY = 0.0F;
float gyroZ = 0.0F;

float pitch = 0.0F;
float roll = 0.0F;
float yaw = 0.0F;

byte reconnect_count = 0;
long currentTime = 0;

char msg[100];
String ipAddress;
String macAddr;
String recMsg="";

const char* node_id =" ";
const char* loc=" ";
const char* temp=" ";
const char* hum=" ";
const char* light=" ";
const char* snd=" ";

int count = 0;

StaticJsonDocument<100> Jsondata; // Create a JSON document of 200 characters max
StaticJsonDocument<200> jsonBuffer;

//Set up the Wifi connection
void setup_wifi() {
  byte count = 0;
  
  WiFi.disconnect();
  delay(100);
  // We start by connecting to a WiFi network
  Serial.printf("\nConnecting to %s\n", ssid);
  WiFi.begin(ssid, password); // start the Wifi connection with defined SSID and PW

  // Indicate "......" during connecting
  // Restart if WiFi cannot be connected for 30sec
  currentTime = millis();
  M5.Lcd.setCursor(0,0);
  M5.Lcd.print("Connecting");
  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
    M5.Lcd.print(".");
    count++;
    if (count == 6) {
      count = 0;
      M5.Lcd.setCursor(0,0);
      M5.Lcd.print("Connecting       "); //clear the dots
      M5.Lcd.setCursor(0,0);
    }
      
    if (millis()-currentTime > 30000){
      ESP.restart();
    }
  }
  // Show "WiFi connected" once linked and light up LED1
  Serial.printf("\nWiFi connected\n");
  // Show IP address and MAC address
  ipAddress=WiFi.localIP().toString();
  Serial.printf("\nIP address: %s\n", ipAddress.c_str());
  macAddr=WiFi.macAddress();
  Serial.printf("MAC address: %s\n", macAddr.c_str());
  
  //Show in the small TFT
  M5.Lcd.fillScreen(BLACK);
  M5.Lcd.setCursor(0,0);
  M5.Lcd.print("WiFi connected!");
  delay(3000);
}

// Routine to receive message from MQTT server
void callback(char* topic, byte* payload, unsigned int length) {
  
  recMsg ="";
  for (int i = 0; i < length; i++) {
    recMsg = recMsg + (char)payload[i];
  }
  Serial.printf("%d: Message arrived [%s] %s\n", millis(), topic, recMsg.c_str());
  Serial.println(recMsg);
  delay(500);

  DeserializationError error = deserializeJson(jsonBuffer, recMsg);

  if (error) {
    Serial.print(F("deserializeJson() failed: "));
    Serial.println(error.c_str());
    return;
  }

  node_id = jsonBuffer["node_id"];
  loc = jsonBuffer["loc"];
  temp = jsonBuffer["temp"];
  hum = jsonBuffer["hum"];
  light = jsonBuffer["light"];
  snd = jsonBuffer["snd"];

  Serial.println(node_id);
  Serial.println(loc);
  Serial.println(temp);
  Serial.println(hum);
  Serial.println(light);
  Serial.println(snd);
  /*
  Serial.println(value);
  Serial.println(value);*/
}


// Reconnect mechanism for MQTT Server
void reconnect() {
  // Loop until we're reconnected
  
  while (!client.connected()) {
    Serial.printf("Attempting MQTT connection...");
    // Attempt to connect
    //if (client.connect("ESP32Client")) {
    if (client.connect(macAddr.c_str())) {
      Serial.println("Connected");
      // Once connected, publish an announcement...
      snprintf(msg, 75, "IoT System (%s) is READY", ipAddress.c_str());
      client.subscribe(mqttTopic1);
      delay(1000);
      client.publish(mqttTopic, msg);
      reconnect_count = 0;
    } else {
      Serial.print("failed, rc=");
      Serial.print(client.state());
      Serial.println(" try again in 5 seconds");
      reconnect_count++;
      
      //reconnect wifi by restart if retrial up to 5 times
      if (reconnect_count == 5){
        ESP.restart();//reset if not connected to server 
      }
        
      // Wait 5 seconds before retrying
      delay(5000);
    }
  }
}

void check_Accel(){
  count++;
  if ((abs(accX)>1.3)|(abs(accY)>1.3)|(abs(accZ-1)>1.5)) {
    Jsondata["MOVED"] = "Yes";
    //Serial.println("The part is moved!!");
  }else {
    Jsondata["MOVED"] = "No";
    //Serial.println("No movement detected!!");
  }
   // Packing the JSON message into msg
   serializeJson(Jsondata, Serial);
   serializeJson(Jsondata, msg);

   if (count >= 500) {
    client.publish(mqttTopic, msg);
    count = 0;
   } 
}

void setup() {
  //pinMode(TRIG, INPUT);
  //pinMode(FUNC_KEY, INPUT);
  //pinMode(LED1, OUTPUT);

  //digitalWrite(LED1, LOW);
  
  Serial.begin(115200); 
  Serial.println("System Start!");  

  M5.begin();
  M5.IMU.Init();
  M5.Lcd.setRotation(3);
  M5.Lcd.fillScreen(BLACK);
  M5.Lcd.setTextSize(1);

  setup_wifi();
  
  client.setServer(mqtt_server, 1883);
  client.setCallback(callback);

  //Initalize Json message
  Jsondata["PART"] = ID;
  Jsondata["MOVED"] = "No"; 

  M5.Lcd.setCursor(0, 0);
  M5.Lcd.println("      Smart Campuse");
  M5.Lcd.setCursor(0, 20);
  M5.Lcd.println(" Node_ID     Loc     Temp");
  M5.Lcd.setCursor(0, 50);
  M5.Lcd.println("  Hum     Light     Snd");
  
}

void loop() {
  M5.IMU.getGyroData(&gyroX,&gyroY,&gyroZ);
  M5.IMU.getAccelData(&accX,&accY,&accZ);
  M5.IMU.getAhrsData(&pitch,&roll,&yaw);

  
  M5.Lcd.setCursor(0, 30);
  M5.Lcd.printf("   %s    %s    %s      ", node_id, loc, temp);
  /*M5.Lcd.setCursor(140, 20);
  M5.Lcd.print("o/s");
  M5.Lcd.setCursor(0, 30);
  M5.Lcd.printf(" %s   %s   %s   ", hu, light, snd);
  M5.Lcd.setCursor(140, 30);
  M5.Lcd.print("G");*/
  M5.Lcd.setCursor(0, 60);
  M5.Lcd.printf("  %s      %s      %s   ",  hum, light, snd);

  check_Accel();
   if (!client.connected()){
    reconnect();
   }
   client.loop();

  /*//Use Timer Interrupt to repeat the following task regularly
   if(mytimer.repeat()){  
      Serial.println("Alive");
      
      //Sending "alive" message to server regularly
      Jsondata["hand_id"] = ID;
      Jsondata["COUNT"] = -2; 
      // Packing the JSON message into msg
      serializeJson(Jsondata, Serial);
      serializeJson(Jsondata, msg);
      
      //Publish msg to MQTT server
      client.publish(mqttTopic, msg);
      Serial.println();
     } */
}
