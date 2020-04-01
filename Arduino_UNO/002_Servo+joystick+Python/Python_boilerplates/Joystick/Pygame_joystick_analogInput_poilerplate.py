# Mohammad Safeea

import pygame
pygame.init()

clock=pygame.time.Clock()

joysticks=[]
for i in range(0,pygame.joystick.get_count()):
	joysticks.append(pygame.joystick.Joystick(i))
	joysticks[-1].init()
	message="Joystick "+joysticks[-1].get_name()+" is detected at index "+str(i)
	print(message)	

temp=input("Input the index of your joystick")
index=int(temp)
dajoystick=joysticks[index]
numAxis=dajoystick.get_numaxes()
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
			print(values)
input("Press enter to terminate")