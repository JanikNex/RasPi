import RPi.GPIO as GPIO
from time import sleep
from random import randint

tasterPin = 16
LEDPin1 = 18
LEDPin2 = 20
LEDPin3 = 22

GPIO.setmode(GPIO.BOARD)
GPIO.setup(tasterPin, GPIO.IN)
GPIO.setup(LEDPin1, GPIO.OUT)
GPIO.setup(LEDPin2, GPIO.OUT)
GPIO.setup(LEDPin3, GPIO.OUT)

taster = False

try:
    while True:
        if GPIO.input(tasterPin) and not taster:
			taster = True
			numb = randint(1,6)
			GPIO.output(LEDPin1, False)
			GPIO.output(LEDPin2, False)
			GPIO.output(LEDPin3, False)
			if numb == 1 or numb == 3 or numb == 5: 
				GPIO.output(LEDPin1, True)
			if numb == 2 or numb == 3 or numb == 6: 
				GPIO.output(LEDPin2, True)
			if numb == 4 or numb == 5 or numb == 6: 
				GPIO.output(LEDPin3, True)
		elif not(GPIO.input(tasterPin)) and taster:
			taster = False
        sleep(0.1)
finally:
    GPIO.cleanup()
