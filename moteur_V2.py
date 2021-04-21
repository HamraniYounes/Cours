#!/usr/bin/python
# -*- coding:utf-8 -*-

'''
Controle d'un moteur à courant continu par le Raspberry Pi
Plus de details:
http://electroniqueamateur.blogspot.com/2014/09/controler-un-moteur-dc-en-python-avec.html
'''

import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BOARD)   ##je prefere la numerotation BOARD plutot que BCM

Moteur1A = 12      ## premiere entree du premier moteur, pin 11
Moteur1B = 11      ## deuxieme entree du premier moteur, pin 12
Moteur1E = 22      ## enable du premier moteur, pin 22

Moteur2A = 15      ## premiere entree du premier moteur, pin 15
Moteur2B = 13      ## deuxieme entree du premier moteur, pin 13
Moteur2E = 24      ## enable du premier moteur, pin 22

GPIO.setup(Moteur1A,GPIO.OUT)  ## ces trois broches du Raspberry Pi sont des sorties
GPIO.setup(Moteur1B,GPIO.OUT)
GPIO.setup(Moteur1E,GPIO.OUT)

GPIO.setup(Moteur2A,GPIO.OUT)
GPIO.setup(Moteur2B,GPIO.OUT)
GPIO.setup(Moteur2E,GPIO.OUT)

pwm = GPIO.PWM(Moteur1E,50)   ## pwm de la broche 22 a une frequence de 50 Hz
pwm2 = GPIO.PWM(Moteur2E,50)


pwm.start(33)   ## on commemnce avec un rapport cyclique de 100%
pwm2.start(33)


print ("Rotation sens direct, vitesse maximale (rapport cyclique 33%)")
GPIO.output(Moteur1A,GPIO.HIGH)
GPIO.output(Moteur1B,GPIO.LOW)
GPIO.output(Moteur1E,GPIO.HIGH)

GPIO.output(Moteur2A,GPIO.HIGH)
GPIO.output(Moteur2B,GPIO.LOW)
GPIO.output(Moteur2E,GPIO.HIGH)

sleep(3)  ## on laisse tourner le moteur 5 secondes avec des parametres

pwm.ChangeDutyCycle(66)  ## modification du rapport cyclique a 66%
pwm2.ChangeDutyCycle(66)

sleep(3)


print ("Rotation sens direct, au ralenti (rapport cyclique 66%)")

pwm.ChangeDutyCycle(100)  ## modification du rapport cyclique a 66%
pwm2.ChangeDutyCycle(100)

print ("Rotation sens direct, au ralenti (rapport cyclique 100%)")

sleep(3)

print ("Rotation sens inverse, au ralenti (rapport cyclique 33%)")
pwm.ChangeDutyCycle(33)
pwm2.ChangeDutyCycle(33)
GPIO.output(Moteur1A,GPIO.LOW)
GPIO.output(Moteur1B,GPIO.HIGH)

GPIO.output(Moteur2A,GPIO.LOW)
GPIO.output(Moteur2B,GPIO.HIGH)

sleep(3)

pwm.ChangeDutyCycle(66)
pwm2.ChangeDutyCycle(66)
print ("Rotation sens inverse, vitesse maximale (rapport cyclique 66%)")
sleep(3)

pwm.ChangeDutyCycle(100)
pwm2.ChangeDutyCycle(100)
print ("Rotation sens inverse, vitesse maximale (rapport cyclique 100%)")
sleep(3)

print ("Arret du moteur")
GPIO.output(Moteur1E,GPIO.LOW)
GPIO.output(Moteur2E,GPIO.LOW)

pwm.stop()    ## interruption du pwm
pwm2.stop()

GPIO.cleanup()