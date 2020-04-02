# Mohammad Safeea, 2nd-April-2020
# ESP8266 micropython tutorial
# controlling SG90 servomotor using PWM

from machine import Pin
from machine import PWM
from machine import sleep

p=Pin(5,1) # Pin 5 corresponds to PIN D1 on the NODEMCU module
servo=PWM(p)

servo.freq(100)
servo.duty(55) # corresponds to 0 degrees
sleep(2)
servo.duty(255) # corresponds to 180 degrees
sleep(2)

# for 15 degrees angle
d=55+15*(200/180) # d correpsonds to the duty cycle of 15 degrees
d=int(d)
servo.duty(d) # motor shaft shall mvoe to approximatly 15 degrees
