import RPi.GPIO as GPIO
import time 
#GPIO.setmode(GPIO.BCM)

lhoradec=[17,4,3,2]
lhorauni=[25,23,22,27]
lmindec=[19,13,6,5]
lminuni=[26,21,20,16]

nums = {'0':(0,0,0,0),
    '1':(0,0,0,1),
    '2':(0,0,1,0),
    '3':(0,0,1,1),
    '4':(0,1,0,0),
    '5':(0,1,0,1),
    '6':(0,1,1,0),
    '7':(0,1,1,1),
    '8':(1,0,0,0),
    '9':(1,0,0,1)}

i = 1

while i > 0:
    hora = int ((time.strftime ('%H')))
    horadec = hora // 10
    horauni = abs (horadec * 10 - hora)
    minuto = int((time.strftime ('%M')))
    minutodec = minuto // 10
    minutouni = abs (minutodec * 10 - minuto)  

    ahoradec=[]
    ahorauni=[]
    amindec=[]
    aminuni=[]
 
#HORA DECENAS
if horadec==0:

    ahoradec = nums['0']
    GPIO.output(lhoradec, ahoradec)


elif horadec==1:
    ahoradec = nums['1']
    GPIO.output(lhoradec, ahoradec)

elif horadec==2:
    ahoradec = nums['2']
    GPIO.output(lhoradec, ahoradec)
    
elif horadec==3:
    ahoradec = nums['3']
    GPIO.output(lhoradec, ahoradec)
    
elif horadec==4:
    ahoradec = nums['4']
    GPIO.output(lhoradec, ahoradec)
    
elif horadec==5:
    ahoradec = nums['5']
    GPIO.output(lhoradec, ahoradec)
    
elif horadec==6:
    ahoradec = nums['6']
    GPIO.output(lhoradec, ahoradec)
    
elif horadec==7:
    ahoradec = nums['7']
    GPIO.output(lhoradec, ahoradec)
    
elif horadec==8:
    ahoradec = nums['8']
    GPIO.output(lhoradec, ahoradec)
    
elif horadec==9:
    ahoradec = nums['9']
    GPIO.output(lhoradec, ahoradec)
    time.sleep(.1)
