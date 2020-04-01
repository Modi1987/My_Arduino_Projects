# Boilerplate - how to use serial port with python
import serial
ser=serial.Serial('COM4',baudrate=9600,timeout=1)

while 1:
	data=ser.readline()
	print(data)



