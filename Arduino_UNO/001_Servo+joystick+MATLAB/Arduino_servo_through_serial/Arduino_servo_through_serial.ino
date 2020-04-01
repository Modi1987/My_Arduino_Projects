// Mohammad Safeea, 1st-April-2020
// Controlling Servo motor thorugh UART command

// Note, the wiring colors for SG90 servo:
//  -Brown GND
//  -Red +5v
//  -Yellow is command signal (attached to pin 9 in this sketch) 

#include <Servo.h>

Servo myServo;  // create a servo object

void setup() {
  // put your setup code here, to run once:
  myServo.attach(9); // attaches the servo on pin 9 to the servo object
  Serial.begin(9600);
}

void loop() {
  // put your main code here, to run repeatedly:
  if (Serial.available()) {
    int inByte = Serial.read();
    int angle=inByte; // angle command from 0 to 180 degrees
    myServo.write(angle);
  }
}
