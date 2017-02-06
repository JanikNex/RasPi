import RPi.GPIO as GPIO
from time import sleep

tasterPin = 16
LEDPin = 18

GPIO.setmode(GPIO.BOARD)
GPIO.setup(LEDPin, GPIO.OUT)
GPIO.setup(tasterPin, GPIO.IN)

taster = False
mode = 2
sosSequence = [0,1,0,1,0,1,0,1,1,1,0,1,1,1,0,1,1,1,0,1,0,1,0,1]
sequenceIndex = 0
try:
    while True:
        if GPIO.input(tasterPin) and not taster:
			taster = True
			mode += 1
			if mode > 2:
				mode == 0
		elif not(GPIO.input(tasterPin)) and taster:
			taster = False
				
        if(mode == 1):
            GPIO.output(LEDPin, True)
        elif(mode == 2):
            GPIO.output(LEDPin, sosSequence[sequenceIndex])
            if sequenceIndex < len(sosSequence)-1:
                sequenceIndex += 1
            else:
                sequenceIndex = 0
        elif(mode == 3):
            GPIO.output(LEDPin, False)
        sleep(0.1)
finally:
    GPIO.cleanup()
