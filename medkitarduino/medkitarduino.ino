
#include "SerialTransfer.h"
#include "FPS_GT511C3.h"
#include "SoftwareSerial.h"
FPS_GT511C3 fps(11, 12); // (Arduino SS_RX = pin 4, Arduino SS_TX = pin 5)
double id;
double y;
SerialTransfer myTransfer;
int x=0;
int i=0;
int g=0;
char arr[] = "Ready";
char arr2[] = "no";
void setup()
{
  Serial.begin(9600); //set up Arduino's hardware serial UART
  Serial.setTimeout(1);
  myTransfer.begin(Serial);
  pinMode(A11,OUTPUT);
  pinMode(A9,OUTPUT);
  fps.SetLED(false);
  /*for(i=2;i<=10;i++){
        pinMode(i,OUTPUT);
        delay(500);
        digitalWrite(i-1,LOW);
        analogWrite(i,150);
      }
      delay(500);
  digitalWrite(10,LOW);*/
}
void Enroll()
{
  // Enroll test

  // find open enroll id
  int enrollid = 0;
  bool usedid = true;
  while (usedid == true)
  {
    usedid = fps.CheckEnrolled(enrollid);
    if (usedid==true) enrollid++;
  }
  fps.EnrollStart(enrollid);

  // enroll
  //Serial.print("Press finger to Enroll #");
  //Serial.println(enrollid);
  uint16_t sendSize = 0;
  sendSize = myTransfer.txObj(arr, sendSize, strlen(arr));
  myTransfer.sendData(sendSize);
  while(fps.IsPressFinger() == false) delay(100);
  bool bret = fps.CaptureFinger(true);
  int iret = 0;
  if (bret != false)
  {
    sendSize = myTransfer.txObj(arr, sendSize, strlen(arr));
    myTransfer.sendData(sendSize);
    //Serial.println("Remove finger");
    fps.Enroll1(); 
    while(fps.IsPressFinger() == true) delay(100);
    //Serial.println("Press same finger again");
    while(fps.IsPressFinger() == false) delay(100);
    bret = fps.CaptureFinger(true);
    if (bret != false)
    {
      //Serial.println("Remove finger");
      fps.Enroll2();
      while(fps.IsPressFinger() == true) delay(100);
     // Serial.println("Press same finger yet again");
      while(fps.IsPressFinger() == false) delay(100);
      bret = fps.CaptureFinger(true);
      if (bret != false)
      {
        //Serial.println("Remove finger");
        iret = fps.Enroll3();
        if (iret == 0)
        {
          y=10;
          myTransfer.sendDatum(y);
        }
        else
        {
          y=11;
          myTransfer.sendDatum(y);
        }
      }
      uint16_t sendSize = 0;
      y=11;
          myTransfer.sendDatum(y);
    }
    uint16_t sendSize = 0;
    y=11;
          myTransfer.sendDatum(y);
  }
  else{ uint16_t sendSize = 0;
  y=11;
          myTransfer.sendDatum(y);
}}
void IDit(){
  if (fps.IsPressFinger())
  {
    fps.CaptureFinger(false);
    id = fps.Identify1_N();
    if (id <200) 
    {
      //Serial.print("Verified ID:");
     //Serial.println(id);
    }else{
      id = 0;
    }
}
}
/*
 legend
 biggest bay
 */
void loop()
{ 
  if(myTransfer.available())
  {
   uint16_t recSize = 0;
    recSize = myTransfer.rxObj(x, recSize);
    y=x-8;
  }
    if(x==1){
      digitalWrite(A9,HIGH); //green
      digitalWrite(A11,LOW);
    }else if(x==2){
      digitalWrite(A11,HIGH); //yellow
      digitalWrite(A9,HIGH);
    }else if(x==3){
      digitalWrite(A11,HIGH); //red
      digitalWrite(A9,LOW);
    }else if(x==4){
      digitalWrite(A11,LOW); //off
      digitalWrite(A9,LOW);
    }else if(x==5){
      //deetc
    }else if(x==6){
      fps.SetLED(true); //on finger led
    }else if(x==7){
      fps.SetLED(false);//off finger led
    }else if(x==8){
      Enroll(); //enroll finger
    }else if(x==9){
      IDit(); // read id finger
    }
   else if(x==10){
        analogWrite(2,150);
        digitalWrite(3,LOW);
        digitalWrite(4,LOW);
        digitalWrite(5,LOW);
        digitalWrite(6,LOW);
        digitalWrite(7,LOW);
        digitalWrite(8,LOW);
        digitalWrite(9,LOW);
        digitalWrite(10,LOW);
    }else if(x==11){
      analogWrite(3,150);
        digitalWrite(2,LOW);
        digitalWrite(4,LOW);
        digitalWrite(5,LOW);
        digitalWrite(6,LOW);
        digitalWrite(7,LOW);
        digitalWrite(8,LOW);
        digitalWrite(9,LOW);
        digitalWrite(10,LOW);
        if (analogRead(A1)>= 0){
          digitalWrite(A9,HIGH);
          digitalWrite(A11,LOW);
          uint16_t sendSize = 0;
          myTransfer.sendDatum(10);
        }else{
          digitalWrite(A11,HIGH);
          digitalWrite(A9,LOW);
        }
    }else if(x==12){
      analogWrite(4,150);
        digitalWrite(3,LOW);
        digitalWrite(2,LOW);
        digitalWrite(5,LOW);
        digitalWrite(6,LOW);
        digitalWrite(7,LOW);
        digitalWrite(8,LOW);
        digitalWrite(9,LOW);
        digitalWrite(10,LOW);
    }else if(x==13){
      analogWrite(5,150);
        digitalWrite(3,LOW);
        digitalWrite(4,LOW);
        digitalWrite(2,LOW);
        digitalWrite(6,LOW);
        digitalWrite(7,LOW);
        digitalWrite(8,LOW);
        digitalWrite(9,LOW);
        digitalWrite(10,LOW);
    }else if(x==14){
      analogWrite(6,150);
        digitalWrite(3,LOW);
        digitalWrite(4,LOW);
        digitalWrite(5,LOW);
        digitalWrite(2,LOW);
        digitalWrite(7,LOW);
        digitalWrite(8,LOW);
        digitalWrite(9,LOW);
        digitalWrite(10,LOW);
    }else if(x==15){
      analogWrite(7,150);
        digitalWrite(3,LOW);
        digitalWrite(4,LOW);
        digitalWrite(5,LOW);
        digitalWrite(6,LOW);
        digitalWrite(2,LOW);
        digitalWrite(8,LOW);
        digitalWrite(9,LOW);
        digitalWrite(10,LOW);
    }else if(x==16){
      analogWrite(8,150);
        digitalWrite(3,LOW);
        digitalWrite(4,LOW);
        digitalWrite(5,LOW);
        digitalWrite(6,LOW);
        digitalWrite(7,LOW);
        digitalWrite(2,LOW);
        digitalWrite(9,LOW);
        digitalWrite(10,LOW);
    }else if(x==17){
      analogWrite(9,150);
        digitalWrite(3,LOW);
        digitalWrite(4,LOW);
        digitalWrite(5,LOW);
        digitalWrite(6,LOW);
        digitalWrite(7,LOW);
        digitalWrite(8,LOW);
        digitalWrite(2,LOW);
        digitalWrite(10,LOW);
    }else if(x==18){  
      analogWrite(10,150);
        digitalWrite(3,LOW);
        digitalWrite(4,LOW);
        digitalWrite(5,LOW);
        digitalWrite(6,LOW);
        digitalWrite(7,LOW);
        digitalWrite(8,LOW);
        digitalWrite(9,LOW);
        digitalWrite(2,LOW);
    }
  
  if (x==9){
  myTransfer.sendDatum(id);//data to python is not consistent please debug
  }
    //myTransfer.sendData(10);
}
