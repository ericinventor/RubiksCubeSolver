import RPi.GPIO as GPIO
from time import sleep

# statics definition
RIGHT_DIR = 5   # direction GPIO pin
RIGHT_STEP = 6  # step GPIO pin
LEFT_DIR = 20
LEFT_STEP = 21
FRONT_DIR = 19
FRONT_STEP = 26
BACK_DIR = 17
BACK_STEP = 27
RIGHT_SOLEN = 22  # right solenoid pin
LEFT_SOLEN = 13
FRONT_SOLEN = 4
BACK_SOLEN = 12
CW = 1           # clockwise rotation
CCW = 0          # counterclockwise rotation
ATTACH = GPIO.LOW       # signal for the solenoid to attach
DETACH = GPIO.HIGH       # signal for the solenoid to detach
SPR = 320        # steps per revolution (360/1.8)

# global variables definition
speed = 2
delay = .0007887 #0.0007887
interMoveDelay = 0.2 #0.1

# GPIO set up 
GPIO.setmode(GPIO.BCM)
GPIO.setup(RIGHT_DIR, GPIO.OUT)
GPIO.setup(RIGHT_STEP, GPIO.OUT)
GPIO.setup(LEFT_DIR, GPIO.OUT)
GPIO.setup(LEFT_STEP, GPIO.OUT)
GPIO.setup(FRONT_DIR, GPIO.OUT)
GPIO.setup(FRONT_STEP, GPIO.OUT)
GPIO.setup(BACK_DIR, GPIO.OUT)
GPIO.setup(BACK_STEP, GPIO.OUT)
GPIO.setup(RIGHT_SOLEN, GPIO.OUT)
GPIO.setup(LEFT_SOLEN, GPIO.OUT)
GPIO.setup(FRONT_SOLEN, GPIO.OUT)
GPIO.setup(BACK_SOLEN, GPIO.OUT)

# ---------- IMPLEMENTATIONS ----------
def rightClawC():
	GPIO.output(RIGHT_DIR, CW)
	for x in range(SPR/4):
		GPIO.output(RIGHT_STEP, GPIO.HIGH)
		sleep(delay)
		GPIO.output(RIGHT_STEP, GPIO.LOW)
		sleep(delay)
	sleep(interMoveDelay)
	
def rightClawCC():
	GPIO.output(RIGHT_DIR, CCW)
	for x in range(SPR/4):
		GPIO.output(RIGHT_STEP, GPIO.HIGH)
		sleep(delay)
		GPIO.output(RIGHT_STEP, GPIO.LOW)
		sleep(delay)
	sleep(interMoveDelay)
	
def rightClawDetach():
	GPIO.output(RIGHT_SOLEN, DETACH)
	sleep(interMoveDelay)
	
def rightClawAttach():
	GPIO.output(RIGHT_SOLEN, ATTACH)
	sleep(interMoveDelay)
	
def leftClawC():
	GPIO.output(LEFT_DIR, CW)
	for x in range(SPR/4):
		GPIO.output(LEFT_STEP, GPIO.HIGH)
		sleep(delay)
		GPIO.output(LEFT_STEP, GPIO.LOW)
		sleep(delay)
	sleep(interMoveDelay)
	
def leftClawCC():
	GPIO.output(LEFT_DIR, CCW)
	for x in range(SPR/4):
		GPIO.output(LEFT_STEP, GPIO.HIGH)
		sleep(delay)
		GPIO.output(LEFT_STEP, GPIO.LOW)
		sleep(delay)
	sleep(interMoveDelay)
	
def leftClawDetach():
	GPIO.output(LEFT_SOLEN, DETACH)
	sleep(interMoveDelay)
	
def leftClawAttach():
	GPIO.output(LEFT_SOLEN, ATTACH)
	sleep(interMoveDelay)
	
def frontClawC():
	GPIO.output(FRONT_DIR, CW)
	for x in range(SPR/4):
		GPIO.output(FRONT_STEP, GPIO.HIGH)
		sleep(delay)
		GPIO.output(FRONT_STEP, GPIO.LOW)
		sleep(delay)
	sleep(interMoveDelay)
	
def frontClawCC():
	GPIO.output(FRONT_DIR, CCW)
	for x in range(SPR/4):
		GPIO.output(FRONT_STEP, GPIO.HIGH)
		sleep(delay)
		GPIO.output(FRONT_STEP, GPIO.LOW)
		sleep(delay)
	sleep(interMoveDelay)
	
def frontClawDetach():
	GPIO.output(FRONT_SOLEN, DETACH)
	sleep(interMoveDelay)
	
def frontClawAttach():
	GPIO.output(FRONT_SOLEN, ATTACH)
	sleep(interMoveDelay)
	
def backClawC():
	GPIO.output(BACK_DIR, CW)
	for x in range(SPR/4):
		GPIO.output(BACK_STEP, GPIO.HIGH)
		sleep(delay)
		GPIO.output(BACK_STEP, GPIO.LOW)
		sleep(delay)
	sleep(interMoveDelay)
	
def backClawCC():
	GPIO.output(BACK_DIR, CCW)
	for x in range(SPR/4):
		GPIO.output(BACK_STEP, GPIO.HIGH)
		sleep(delay)
		GPIO.output(BACK_STEP, GPIO.LOW)
		sleep(delay)
	sleep(interMoveDelay)
	
def backClawDetach():
	GPIO.output(BACK_SOLEN, DETACH)
	sleep(interMoveDelay)
	
def backClawAttach():
	GPIO.output(BACK_SOLEN, ATTACH)
	sleep(interMoveDelay)
	
def leftCCAndRightC():
	GPIO.output(LEFT_DIR, CCW)
	GPIO.output(RIGHT_DIR, CW)
	for x in range(SPR/4):
		GPIO.output(LEFT_STEP, GPIO.HIGH)
		GPIO.output(RIGHT_STEP, GPIO.HIGH)
		sleep(delay)
		GPIO.output(LEFT_STEP, GPIO.LOW)
		GPIO.output(RIGHT_STEP, GPIO.LOW)
		sleep(delay)
	sleep(interMoveDelay)
	
def leftCAndRightCC():
	GPIO.output(LEFT_DIR, CW)
	GPIO.output(RIGHT_DIR, CCW)
	for x in range(SPR/4):
		GPIO.output(LEFT_STEP, GPIO.HIGH)
		GPIO.output(RIGHT_STEP, GPIO.HIGH)
		sleep(delay)
		GPIO.output(LEFT_STEP, GPIO.LOW)
		GPIO.output(RIGHT_STEP, GPIO.LOW)
		sleep(delay)
	sleep(interMoveDelay)
	
def frontCAndBackCC():
	GPIO.output(FRONT_DIR, CW)
	GPIO.output(BACK_DIR, CCW)
	for x in range(SPR/4):
		GPIO.output(FRONT_STEP, GPIO.HIGH)
		GPIO.output(BACK_STEP, GPIO.HIGH)
		sleep(delay)
		GPIO.output(FRONT_STEP, GPIO.LOW)
		GPIO.output(BACK_STEP, GPIO.LOW)
		sleep(delay)
	sleep(interMoveDelay)
	
def frontCCAndBackC():
	GPIO.output(FRONT_DIR, CCW)
	GPIO.output(BACK_DIR, CW)
	for x in range(SPR/4):
		GPIO.output(FRONT_STEP, GPIO.HIGH)
		GPIO.output(BACK_STEP, GPIO.HIGH)
		sleep(delay)
		GPIO.output(FRONT_STEP, GPIO.LOW)
		GPIO.output(BACK_STEP, GPIO.LOW)
		sleep(delay)
	sleep(interMoveDelay)

# ---------- USAGES -------------------
def executeOneMove(move):
	if move == "R":
		rightClawC()
		rightClawDetach()
		rightClawCC()
		rightClawAttach()
	elif move == "R'":
		rightClawCC()
		rightClawDetach()
		rightClawC()
		rightClawAttach()
	elif move == "R2":
		rightClawC()
		rightClawC()
	elif move == "L":
		leftClawC()
		leftClawDetach()
		leftClawCC()
		leftClawAttach()
	elif move == "L'":
		leftClawCC()
		leftClawDetach()
		leftClawC()
		leftClawAttach()
	elif move == "L2":
		leftClawC()
		leftClawC()
	elif move == "F":
		frontClawC()
		frontClawDetach()
		frontClawCC()
		frontClawAttach()
	elif move == "F'":
		frontClawCC()
		frontClawDetach()
		frontClawC()
		frontClawAttach()
	elif move == "F2":
		frontClawC()
		frontClawC()
	elif move == "B":
		backClawC()
		backClawDetach()
		backClawCC()
		backClawAttach()
	elif move == "B'":
		backClawCC()
		backClawDetach()
		backClawC()
		backClawAttach()
	elif move == "B2":
		backClawC()
		backClawC()
	elif move == "U":
		upFaceBack()
		backClawC()
		backClawDetach()
		backClawCC()
		backClawAttach()
		backFaceUp()
	elif move == "U'":
		upFaceBack()
		backClawCC()
		backClawDetach()
		backClawC()
		backClawAttach()
		backFaceUp()
	elif move == "U2":
		upFaceBack()
		backClawC()
		backClawC()
		backFaceUp()
	elif move == "D":
		downFaceFront()
		frontClawC()
		frontClawDetach()
		frontClawCC()
		frontClawAttach()
		frontFaceDown()
	elif move == "D'":
		downFaceFront()
		frontClawCC()
		frontClawDetach()
		frontClawC()
		frontClawAttach()
		frontFaceDown()
	elif move == "D2":
		downFaceFront()
		frontClawC()
		frontClawC()
		frontFaceDown()

def upFaceBack():
	frontClawDetach()
	backClawDetach()
	leftCCAndRightC()
	frontClawAttach()
	backClawAttach()
	leftClawDetach()
	leftClawC()
	leftClawAttach()
	rightClawDetach()
	rightClawCC()
	rightClawAttach()

def downFaceFront():
	upFaceBack()

def backFaceUp():
	frontClawDetach()
	backClawDetach()
	leftCAndRightCC()
	frontClawAttach()
	backClawAttach()
	leftClawDetach()
	leftClawCC()
	leftClawAttach()
	rightClawDetach()
	rightClawC()
	rightClawAttach()

def frontFaceDown():
	backFaceUp()
