# Mohammad Safeea, 
# https://mohammadsafeea.weebly.com/
# Controlling Servo using ESP8266 from PC over wifi
# Arduino code for ESP8266 server is available at:
# https://github.com/Modi1987/My_Arduino_Projects/tree/master/ESP8266/Controlling_Servos/Arduino_IDE/ESP8266_controlServoOverWifi


from Tkinter import *
import socket

soc=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

root=Tk()
mf=Frame(root)
mf.pack()
Label(mf,text='IP:').grid(row=0,column=0)
txtIP=StringVar()
Entry(mf,textvariable=txtIP).grid(row=0,column=1)
txtIP.set('192.168.4.1')
Label(mf,text='Spindle Angle:').grid(row=1,column=0)
txtCMD=StringVar()
Entry(mf,textvariable=txtCMD).grid(row=1,column=1)
Label(mf,text='State Message:').grid(row=2,column=0)
Label(mf,text='Enter angle in textbox then hit Send').grid(row=2,column=1)

def sendCommand():
 try:
  print('Converting the string in the entry into an int')
  cmd=int(txtCMD.get())
 except:
  print('Error, could not convert value in the entry into an int')
  return
 try:
  print('Sending joint angle to motor over wifi')
  c=chr(cmd)
  soc.send(c)
 except:
  print('Error has happened')


def connectCommand():
 ip=txtIP.get()
 address=(ip,1987)
 soc.connect(address)

def closeCommand():
 soc.close()
 root.destroy()

Button(mf,text='Send',command=sendCommand).grid(row=4,column=0)
Button(mf,text='Connect',command=connectCommand).grid(row=4,column=1)
Button(mf,text='Close',command=closeCommand).grid(row=5,column=0)
root.title('WIFI Servo CtrlL')
