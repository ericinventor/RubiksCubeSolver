
from time import sleep
import RPi.GPIO as GPIO

DIR = 17  # Direction GPIO Pin
STEP = 27   # Step GPIO Pin
CW = 1     # Clockwise Rotation
CCW = 0   # Counterclockwise Rotation
SPR = 316   # Steps per Revolution (360 /1.8)

GPIO.setmode(GPIO.BCM)
GPIO.setup(DIR, GPIO.OUT)
GPIO.setup(STEP, GPIO.OUT)
GPIO.output(DIR, CW)

step_count = SPR
speed = 2
delay = 0.0007887

for x in range(step_count/4):
    GPIO.output(STEP, GPIO.HIGH)
    sleep(delay)
    GPIO.output(STEP, GPIO.LOW)
    sleep(delay)
   

GPIO.cleanup()
