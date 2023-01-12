# -*- coding: utf-8 -*-
 
import RPi.GPIO as GPIO
import time
 
GPIO.setmode(GPIO.BCM)
GPIO.setup(17,GPIO.OUT)
 
for i in range(5):
    GPIO.output(17, True)
    time.sleep(3)
    GPIO.output(17, False)
    time.sleep(3)
    
GPIO.cleanup()