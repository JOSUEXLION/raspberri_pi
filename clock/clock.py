#led7segtime

import RPi.GPIO as GPIO
import time 
GPIO.setmode(GPIO.BCM)

GPIO.setup(17, GPIO.OUT) #serial data
GPIO.setup(18, GPIO.OUT)#
GPIO.setup(27, GPIO.OUT)#clock, 21 on older
GPIO.setup(18, GPIO.OUT)#latch

#segments 1 nul then G-F-E-D-C-B-A
Nums = {  #' ':(1,1,1,1,1,1,1),
     
	'0':(0,0,1,1,1,1,1,1),
	'1':(0,0,0,0,0,1,1,0),
	'2':(0,1,0,1,1,0,1,1),
	'3':(0,1,0,0,1,1,1,1),
	'4':(0,1,1,0,0,1,1,0),
	'5':(0,1,1,0,1,1,0,1),
	'6':(0,1,1,1,1,1,0,1),
	'7':(0,0,0,0,0,1,1,1),
	'8':(0,1,1,1,1,1,1,1),
	'9':(0,1,1,0,0,1,1,1)}

print ('the current tieme is:')
print time.strftime('%H:%M:%S')

#set up the loop
while True:
	tstr=time.strftime('%H:%M:%S')
	Data1=Nums[tstr[0]]+Nums[tstr[1]]+Nums[tstr[3]]+Nums[tstr[4]]+Nums[tstr[6]]+Nums[tstr[7]]
	#send data the shift  rigisters
	shift  = 47
	while shift >=0:
		GPIO.output(17, GPIO.LOW)
		#dertermine if bit is set or clear data is NOT inverted
		if Data1[shift] ==1: GPIO.output(17, GPIO.HIGH)
		#ADVANCE THE CLOCK
		GPIO.output(27, GPIO.LOW); GPIO.output(27, GPIO.HIGH)
		shift=shift-1
		#latch and display the output
		GPIO.output(22, GPIO.LOW); GPIO.output(22, GPIO.HIGH)
		time.sleep(.1)
