#!/usr/bin/python
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

#GPIO pin 18, pin 12 on board
pin = 18
GPIO.setup(pin, GPIO.OUT)

# This will be used to close the door if the door is open.

try:
    time.sleep(1)
    GPIO.output(pin, GPIO.HIGH)
    #time.sleep(.2)
    GPIO.output(pin, GPIO.LOW)
    GPIO.cleanup()
    print "Closed Door"

except KeyboardInterrupt:
  # print "  Quit"
  # Reset GPIO settings
  GPIO.cleanup()
