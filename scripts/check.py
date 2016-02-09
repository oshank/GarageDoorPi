#!/usr/bin/python
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

# This will be used for checking the state of the door

# Pins to use GPIO25, GPIO8, GPIO7, GPIO2
# Pins on Pi  22      24     26     3

pinIn = 2
GPIO.setup(pinIn, GPIO.IN)

if
