#!/usr/bin/python
import RPi.GPIO as GPIO
import time
import os
import closeDoor
import openDoor

GPIO.setmode(GPIO.BCM)

# This will be used for checking the state of the door

# Pins to use GPIO25, GPIO8, GPIO7, GPIO2
# Pins on Pi  22      24     26     3

pinIn = 25
pinOut = 8
GPIO.setup(pinIn, GPIO.IN)
GPIO.setup(pinOut, GPIO.OUT)

try:
    GPIO.output(pinOut, GPIO.HIGH)
    if GPIO.input(pinIn):
        print "Door is Open"
        closeDoor
        print "Closing Door"
        GPIO.cleanup()
    else:
        print "Door is Closed"
        openDoor
        print "Opening Door"
        GPIO.cleanup()

except KeyboardInterrupt:
  # print "  Quit"
  # Reset GPIO settings
  GPIO.cleanup()
