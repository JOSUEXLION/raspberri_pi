# -*- coding: utf-8 -*-
#------------------------------------------------------------------------------------------
# Código para decrementar un conteo en un display de 7 segmentos

import RPi.GPIO as GPIO                     # Importamos la biblioteca de GPIO
import time                                 # Importa la biblioteca de tiempo
GPIO.setmode(GPIO.BCM)                      # Setiamos pin de acuerdo con la CPU

#------------------------------------------------------------------------------------------
# Define las puertas (pines) de GPIO para la display de 7 segmentos

#            G  F  E D C B  A  P
segmentos = (11,4,23,8,7,10,18,25)          # indicamos los pines que vamos ha utilizar en la pi

# En este bucle con for voy a cortar cada pin como salida y borrar bit

for pino in segmentos:
    GPIO.setup(pino, GPIO.OUT)              # Coloca o pin como salída
    GPIO.output(pino, 0)                    # cero  pino que esta como salída

# codificacion de los pines para el display de 7 segmentos en binario

num = {' ':(1,1,1,1,1,1,1),
       '0':(1,0,0,0,0,0,0),
       '1':(1,1,1,1,0,0,1),
       '2':(0,1,0,0,1,0,0),
       '3':(0,1,1,0,0,0,0),
       '4':(0,0,1,1,0,0,1),
       '5':(0,0,1,0,0,1,0),
       '6':(0,0,0,0,0,1,0),
       '7':(1,1,1,1,0,0,0),
       '8':(0,0,0,0,0,0,0),
       '9':(0,0,1,0,0,0,0)}

n = 99;                                      # Numero que va a ser decrementado

#------------------------------------------------------------------------------------------

try:
    while True:
        print("el valor de n es: %d" %n)       # Imprime el valor de n la console
        for loop in range(99, 00):            # aparecera todos los pines de salida
            GPIO.output(segmentos[loop], num[str(n)][loop])
        n -= 1                              # decrementa para el próximo numero
        if n > 99:                           # llego al final
            n == 00                           # si, entonces vuelve a cero
        time.sleep(1)                       # Aguarda 1 segundo
finally:
    GPIO.cleanup()                          # Limpia los puertos
