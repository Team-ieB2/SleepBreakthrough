# -*- coding: utf-8 -*-

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setup(12, GPIO.OUT)

pwm = GPIO.PWM(12, 100)

pwm.start(100)
time.sleep(5)
pwm.stop()

GPIO.cleanup()