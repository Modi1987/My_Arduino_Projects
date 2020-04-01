# Mohammad Safeea. 1St-April-2020
# Controlling Servos from joystick
# works with python 3

import pygame
import serial
# Print some stuff
print('Controlling servo motor using a Joystick')
print('By Mohammad Safeea')
print('Make sure that you have pyserial and pygame installed on your system')
x=input('Press enter to continue')
# define a function to be used later
def sendOneByteThroughUART(serObj,cmdStick):
    temp=int((cmdStick+1)*90)
    vals=temp.to_bytes(2,'little')
    print(vals[0])
    cmd=chr(temp)
    serObj.write(cmd.encode('utf-8'));
# Initiate the joystick
pygame.init()

clock=pygame.time.Clock()

joysticks=[]
for i in range(0,pygame.joystick.get_count()):
	joysticks.append(pygame.joystick.Joystick(i))
	joysticks[-1].init()
	message="Joystick "+joysticks[-1].get_name()+" is detected at index "+str(i)
	print(message)	

temp=input("Input the index of your joystick\n")
index=int(temp)
dajoystick=joysticks[index]
numAxis=dajoystick.get_numaxes()
# initite the serial port
ser=serial.Serial('COM4',baudrate=9600,timeout=1)
# Control loop
loopFlag=True
while loopFlag:
	clock.tick(10) # perform the loop at 4 times a second
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			print("Event QUIT is initiated, exitting")
			loopFlag=False
			break
		if event.type == pygame.JOYAXISMOTION:
			values=[]
			for i in range(numAxis):
				values.append(dajoystick.get_axis(i))
			print(values) # print analog values from joystickSSS
			# send command to arudino
			cmdStick=values[2]
			sendOneByteThroughUART(ser,cmdStick)
input("Press enter to terminate")
