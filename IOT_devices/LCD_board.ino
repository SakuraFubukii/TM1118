#include <ESP8266WiFi.h> 
#include "LedMatrix.h"
#include <NTPClient.h>
// change next line to use with another board/shield
//#include <WiFi.h> // for WiFi shield
//#include <WiFi101.h> // for WiFi 101 shield or MKR1000
#include <WiFiUdp.h>
LedMatrix ledMatrix(1,D4);

char timeBuf[8];
const char *ssid     = "EIA-W311MESH";
const char *password = "42004200";

WiFiUDP ntpUDP;
NTPClient timeClient(ntpUDP, "ntp1.aliyun.com",60*60*8, 30*60*1000);

void setup(){
  Serial.begin(115200);
  ledMatrix.init();
  ledMatrix.setIntensity(5);

  ledMatrix.setTextAlignment(TEXT_ALIGN_LEFT);
  WiFi.begin(ssid, password);

  while ( WiFi.status() != WL_CONNECTED ) {
    delay ( 500 );
    Serial.print ( "." );
  }

  timeClient.begin();
}

void loop() {
  timeClient.update();
  int hour = timeClient.getHours();
  int minute = timeClient.getMinutes();
  sprintf(timeBuf,"%02d:%02d",hour, minute);

  for(int i=0; i<strlen(timeBuf); i++) {
    
    ledMatrix.setText(timeBuf + i); 
    ledMatrix.clear();
    ledMatrix.drawText();
    ledMatrix.commit();

    delay(200);

  }

  ledMatrix.clear();

  delay(1000);

}
