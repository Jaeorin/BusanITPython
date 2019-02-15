#include<SoftwareSerial.h>
#include <DHT11.h>
#define BT_TX 7
#define BT_RX 6
int led = 8;
int pin=9;
DHT11 dht11(pin);

SoftwareSerial BTSerial(BT_TX, BT_RX);

void setup() {
  BTSerial.begin(9600);
  pinMode(led, OUTPUT);
  
}

void loop() {
   int err;    // result code
   float temp, humi;   // temperature, humidity
   if(BTSerial.available()){
    char cData = BTSerial.read();
    if('1' == cData){
      digitalWrite(led, OUTPUT);
    }
    if('2' == cData){
      digitalWrite(led, LOW);
    }
   if('3' == cData){
      while(0<1){
        if((err=dht11.read(humi, temp))==0){
        BTSerial.print("temperature:");
        BTSerial.print(temp);
        BTSerial.println();
        BTSerial.print(" humidity:");
        BTSerial.print(humi);
        BTSerial.println();
        }
        delay(2000);
        
       BTSerial.available();
       char cData = BTSerial.read();
        if('4' == cData){
          break;
        }
     }
    }
  }
}
