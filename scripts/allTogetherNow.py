#!/usr/bin/python
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

# This will be used for checking the state of the door

# Pins to use GPIO25, GPIO8, GPIO7, GPIO2
# Pins on Pi  22      24     26     3

#Pin In check from switch
pinIn = 25
GPIO.setup(pinIn, GPIO.IN)
#Pin out to switch
pinOut = 8
GPIO.setup(pinOut, GPIO.OUT)
#Pin for Relay
pin = 18
GPIO.setup(pin, GPIO.OUT)

def run(state):
    if state == "open":
        try:
            time.sleep(1)
            GPIO.output(pin, GPIO.HIGH)
            #time.sleep(.2)
            GPIO.output(pin, GPIO.LOW)
            print "Closed Door"
    elif state == "closed":
        try:
            time.sleep(1)
            GPIO.output(pin, GPIO.HIGH)
            #time.sleep(.2)
            GPIO.output(pin, GPIO.LOW)
            print "Opened Door"
    GPIO.cleanup()

