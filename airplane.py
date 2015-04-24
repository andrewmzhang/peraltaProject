import RPi.GPIO as GPIO
import PiFm
GPIO.setmode(GPIO.BCM)

#GPIO.setup(4, GPIO.IN)
#GPIO.setup(7, GPIO.IN)
#GPIO.setup(8, GPIO.IN)
#GPIO.setup(17, GPIO.IN)
GPIO.setup(18, GPIO.IN)

#GPIO.setup(21, GPIO.OUT)
#GPIO.setup(22, GPIO.OUT)
#GPIO.setup(23, GPIO.OUT)
#GPIO.setup(24, GPIO.OUT)
GPIO.setup(25, GPIO.OUT)

def detection(): 
	inputPins = [4, 7, 8, 17, 18]
	for x in inputPins:
		if GPIO.input(x) == true:
			return x
		else:
			return 


def shutdownAllNodes():
	outputs = [21, 22, 23, 24, 25]
	for x in outputs:
		GPIO.output(x, False)



def decisionTree(x):
	shutdownAllNodes()
	if x == 4:
		GPIO.output(21, True)
	if x == 7:
		GPIO.output(22, True)
		GPIO.output(21, True)
	if x == 8:
		GPIO.output(23, True)
		GPIO.output(22, True)
		GPIO.output(21, True)
	if x == 17:
		GPIO.output(24, True)
		GPIO.output(23, True)
		GPIO.output(22, True)
		GPIO.output(21, True)
	if x == 18:
		GPIO.output(25, True)
		GPIO.output(24, True)
		GPIO.output(23, True)
		GPIO.output(22, True)
		GPIO.output(21, True)
		playSound()


def lastPinDetector():
	lastState = True;
	currentState = GPIO.input(18)
	
	while True:
		currentState = GPIO.input(18)
		if (lastState != currentState):
			print("current state" + str(currentState))
			GPIO.output(25, True)
			if (currentState == 1):
				playSound()
			print("trigger detected!")
			lastState = currentState

def playSound():
	PiFm.play_sound("sound.wav")

lastPinDetector()
