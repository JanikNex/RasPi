import RPi.GPIO as GPIO
from time import sleep

pinRot = 11
pinOrange = 13
pin Gruen = 15

gruenPhase = 5.0
orangePhase = 2.0
rotPhase = 5.0

phase = 0

GPIO.setmode(GPIO.BOARD)
GPIO.setup(pinRot, GPIO.OUT)
GPIO.setup(pinOrange, GPIO.OUT)
GPIO.setup(pinGruen, GPIO.OUT)

GPIO.output(pinRot, True)
GPIO.output(pinOrange, True)
GPIO.output(pinGruen, True)
sleep(3)
GPIO.output(pinRot, False)
GPIO.output(pinOrange, False)
GPIO.output(pinGruen, False)
phase += 1

try:
    while True:
        if phase == 1:
            GPIO.output(pinRot, True)
            GPIO.output(pinOrange, False)
            GPIO.output(pinGruen, False)
            sleep(rotPhase)
            phase += 1
        if phase == 2:
            GPIO.output(pinRot, True)
            GPIO.output(pinOrange, True)
            GPIO.output(pinGruen, False)
            sleep(orangePhase)
            phase += 1
        if phase == 3:
            GPIO.output(pinRot, False)
            GPIO.output(pinOrange, False)
            GPIO.output(pinGruen, True)
            sleep(gruenPhase)
            phase += 1
        if phase == 4:
            GPIO.output(pinRot, False)
            GPIO.output(pinOrange, True)
            GPIO.output(pinGruen, False)
            sleep(orangePhase)
            phase = 1
            
finally:
    GPIO.cleanup()
