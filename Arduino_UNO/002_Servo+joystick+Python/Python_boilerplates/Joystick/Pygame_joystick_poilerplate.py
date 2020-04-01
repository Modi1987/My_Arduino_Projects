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
loopFlag=True
while loopFlag:
	clock.tick(10) # perform the loop at 10 times a second
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			print("Event QUIT is initiated, exitting")
			loopFlag=False
			break
		""""
		if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
			print("ESC is pressed, exitting")
			loopFlag=False
			break
		if event.type == pygame.JOYAXISMOTION:
			message=event.axis
			print(message)
		if event.type == pygame.JOYBUTTONDOWN:
			message=event.button
			print(message)
		
		if event.type == pygame.JOYHATMOTION:
			message=event.hat
			print(message)
		"""
		if event.type == pygame.JOYBALLMOTION:
			message=event.ball
			print(message)
input("Press enter to terminate")