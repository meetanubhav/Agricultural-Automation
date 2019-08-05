#include  <ESP8266WiFi.h>
#include <dht.h>

#define dht_apin A0 

#define WIFI_SSID "ProjectAI" 
#define WIFI_PASSWORD "project@sil123" 
dht DHT;
void setup(){
	Serial.begin(9600);
  	Serial.print("Wifi connecting to ");
 	Serial.println(WIFI_SSID);
	Serial.println("Wifi Connected Success!");
  	WiFi.begin (WIFI_SSID, WIFI_PASSWORD);
  	while (WiFi.status() != WL_CONNECTED) 
  	{
     delay(500);
     Serial.print(".");
   }

}
void loop(){
DHT.read11(dht_apin);
    
    Serial.print("Current humidity = ");
    Serial.print(DHT.humidity);
    Serial.print("%  ");
    Serial.print("temperature = ");
    Serial.print(DHT.temperature); 
    Serial.println("C  ");
    
    delay(5000);//Wait 5 seconds before accessing sensor again.

	//http://192.168.0.100/projectai/first.php?x=2
	
}