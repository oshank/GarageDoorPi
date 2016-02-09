#!/usr/bin/python
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

#GPIO pin 18, pin 12 on board
pin = 18
GPIO.setup(pin, GPIO.OUT)

n = 0

# This will be used to close the door if the door is open.

while (n==0):
    sleep(1)
    GPIO.output(pin, GPIO.HIGH)
    sleep(.5)
    GPIO.output(pin, GPIO.LOW)
    n = 1
