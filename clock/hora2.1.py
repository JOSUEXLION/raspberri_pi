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
##############################################################
#HORA UNIDAD

if horauni==0:

    ahorauni = nums['0']
    GPIO.output(lhorauni, ahorauni)


elif horauni==1:
    ahorauni = nums['1']
    GPIO.output(lhorauni, ahorauni)

elif horauni==2:
    ahorauni = nums['2']
    GPIO.output(lhorauni, ahorauni)
    
elif horauni==3:
    ahorauni = nums['3']
    GPIO.output(lhorauni, ahorauni)
    
elif horauni==4:
    ahorauni = nums['4']
    GPIO.output(lhorauni, ahorauni)
    
elif horauni==5:
    ahorauni = nums['5']
    GPIO.output(lhorauni, ahorauni)
    
elif horauni==6:
    ahorauni = nums['6']
    GPIO.output(lhorauni, ahorauni)
    
elif horauni==7:
    ahorauni = nums['7']
    GPIO.output(lhorauni, ahorauni)
    
elif horauni==8:
    ahorauni = nums['8']
    GPIO.output(lhorauni, ahorauni)
    
elif horauni==9:
    ahorauni = nums['9']
    GPIO.output(lhorauni, ahorauni)
time.sleep(.1)


########################################################
#MINUTOS DECENAS
if minutodec==0:

    ahoradec = nums['0']
    GPIO.output(lmindec, amindec)


elif minutodec==1:
    ahoradec = nums['1']
    GPIO.output(lmindec, amindec)

elif minutodec==2:
    ahoradec = nums['2']
    GPIO.output(lmindec, amindec)
    
elif minutodec==3:
    ahoradec = nums['3']
    GPIO.output(lmindec, amindec)
    
elif minutodec==4:
    ahoradec = nums['4']
    GPIO.output(lmindec, amindec)
    
elif minutodec==5:
    ahoradec = nums['5']
    GPIO.output(lmindec, amindec)
    
elif minutodec==6:
    ahoradec = nums['6']
    GPIO.output(lmindec, amindec)
    
elif minutodec==7:
    ahoradec = nums['7']
    GPIO.output(lmindec, amindec)
    
elif minutodec==8:
    ahoradec = nums['8']
    GPIO.output(lmindec, amindec)
    
elif minutodec==9:
    ahoradec = nums['9']
    GPIO.output(lmindec, amindec)
time.sleep(.1)

###########################################################
#MINUTOS UNIDAD

if minutouni==0:

    ahoradec = nums['0']
    GPIO.output(lminuni, aminuni)


elif horadec==1:
    ahoradec = nums['1']
    GPIO.output(lminuni, aminuni)

elif horadec==2:
    ahoradec = nums['2']
    GPIO.output(lminuni, aminuni)
    
elif horadec==3:
    ahoradec = nums['3']
    GPIO.output(lminuni, aminuni)
    
elif horadec==4:
    ahoradec = nums['4']
    GPIO.output(lminuni, aminuni)
    
elif horadec==5:
    ahoradec = nums['5']
    GPIO.output(lminuni, aminuni)
    
elif horadec==6:
    ahoradec = nums['6']
    GPIO.output(lminuni, aminuni)
    
elif horadec==7:
    ahoradec = nums['7']
    GPIO.output(lminuni, aminuni)
    
elif horadec==8:
    ahoradec = nums['8']
    GPIO.output(lminuni, aminuni)
    
elif horadec==9:
    ahoradec = nums['9']
    GPIO.output(lminuni, aminuni)
time.sleep(.1)

