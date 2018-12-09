import kociemba
import MechanicalAPI # to access the varaibles in the file
import numpy as numpy
import pycuber as pc
import PyCuberColorScheme
import Queue
import sys
from MechanicalAPI import * # to access the functions in the file
from PIL import Image
from picamera import PiCamera
from time import sleep

# statics definition
TILE_PER_SIDE = 3
FACET_NUMBER = 6
FILE_NAMES = ["facet0.jpg", "facet1.jpg", "facet2.jpg", "facet3.jpg", "facet4.jpg", "facet5.jpg"]
#DEFAULT # D
#UNKNOWN # U
BLUE = [190, 210] # B
WHITE_H = [50, 80] # W
WHITE_S = [0, 0.5]
GREEN = [100, 120] # G
ORANGE_H = [340, 360, 0, 10] # O
ORANGE_V = [0.7, 1]
RED_H = [340, 360, 0, 10] # R
RED_V = [0.4, 0.7]
YELLOW_H = [50, 80] # Y
YELLOW_S = [0.5, 1]
SOLVED_STATE = "UUUUUUUUURRRRRRRRRFFFFFFFFFDDDDDDDDDLLLLLLLLLBBBBBBBBB"

# global variables definition
xoff = 0
yoff = 0
widthScale = 1
width = 100
tileWidth = width/TILE_PER_SIDE
camera = PiCamera() # the camera object
tempFacetNumber = 0
myCube = pc.Cube()

# a mapping from the color to the side
colorToSideDict = {
	"B": "UnknownSide",
	"W": "UnknownSide",
	"Y": "UnknownSide",
	"G": "UnknownSide",
	"O": "UnknownSide",
	"R": "UnknownSide"
}

# a mapping from the side to the index of it in the 6x3x3 array
sideToIndexDict = {
	"U": 1,
	"R": 5,
	"F": 0,
	"D": 3,
	"L": 4,
	"B": 2
}

# a mapping from the index to the side
indexToSideDict = {
	1: "U",
	5: "R",
	0: "F",
	3: "D",
	4: "L",
	2: "B"
}

def toStrRep(rubikMatrices):
	rubikStringRep = ""
	rubikStringRep = rubikStringRep + facetToStrRep(rubikMatrices[sideToIndexDict["U"]])
	rubikStringRep = rubikStringRep + facetToStrRep(rubikMatrices[sideToIndexDict["R"]])
	rubikStringRep = rubikStringRep + facetToStrRep(rubikMatrices[sideToIndexDict["F"]])
	rubikStringRep = rubikStringRep + facetToStrRep(rubikMatrices[sideToIndexDict["D"]])
	rubikStringRep = rubikStringRep + facetToStrRep(rubikMatrices[sideToIndexDict["L"]])
	rubikStringRep = rubikStringRep + facetToStrRep(rubikMatrices[sideToIndexDict["B"]])
	return rubikStringRep

def facetToStrRep(matrix):
	result = ""
	for i in range(TILE_PER_SIDE):
		for j in range(TILE_PER_SIDE):
			result = result + str(colorToSideDict[matrix[i][j]])
	return result

# take a picture and store it as a .jpg file in the current directory
def takePicture(facetNumber):
	camera.start_preview()
	sleep(2)
	camera.stop_preview()
	camera.capture("facet" + str(facetNumber) + ".jpg")
	
def cameraRotate(facetNumber):
	if facetNumber == 0:
		backClawDetach()
		frontClawDetach()
		sleep(1)
		leftCAndRightCC()
	elif facetNumber == 1:
		leftCAndRightCC()
	elif facetNumber == 2:
		leftCAndRightCC()
	elif facetNumber == 3:
		leftCAndRightCC()
	elif facetNumber == 4:
		leftCAndRightCC()
		sleep(1)
		frontClawAttach()
		backClawAttach()
		sleep(2)
		leftClawDetach()
		rightClawDetach()
		sleep(1)
		leftCAndRightCC()
		sleep(1)
		frontCAndBackCC()
		sleep(1)
	elif facetNumber == 5:
		frontCAndBackCC()
		frontCAndBackCC()
	else:
		pass
	
# take pictures on all facets and store them as .jpg files
def takeAllPictures():
	camera.resolution = (640, 480)
	frontClawAttach()
	backClawAttach()
	rightClawAttach()
	leftClawAttach()
	sleep(1)
	for i in range(6):
		cameraRotate(i)
		sleep(2)
		takePicture(i)
	
# read in the .jpg file specified by facetNumber and return a 3x3 matrix
def recognizeColorFacet(facetNumber):
	img = Image.open(FILE_NAMES[facetNumber])
	arr = numpy.array(img)
	color = [["U" for x in range(TILE_PER_SIDE)] for y in range(TILE_PER_SIDE)]
	for i in range(TILE_PER_SIDE):
		for j in range(TILE_PER_SIDE):
			color[i][j] = recognizeColorTile(arr, xoff + i*tileWidth, yoff + j*tileWidth)
	return color
	
# convert rgb to hsv TODO: reference this code???
def rgb2hsv(r, g, b):
    r, g, b = r/255.0, g/255.0, b/255.0
    mx = max(r, g, b)
    mn = min(r, g, b)
    df = mx-mn
    if mx == mn:
        h = 0
    elif mx == r:
        h = (60 * ((g-b)/df) + 360) % 360
    elif mx == g:
        h = (60 * ((b-r)/df) + 120) % 360
    elif mx == b:
        h = (60 * ((r-g)/df) + 240) % 360
    if mx == 0:
        s = 0
    else:
        s = df/mx
        v = mx
    return h, s, v
	
# return a string that represents the color of the tile specified
def recognizeColorTile(arr, ioff, joff):
	tileRgb = arr[ioff + tileWidth/2][joff + tileWidth/2]
	tileHsv = rgb2hsv(tileRgb[0], tileRgb[1], tileRgb[2])
	#print(str(tileHsv))
	h = tileHsv[0]
	s = tileHsv[1]
	v = tileHsv[2]
	if BLUE[0] <= h <= BLUE[1]: # if h is in between the lower and upper bound of blue
		return "B"
	elif GREEN[0] <= h <= GREEN[1]: # if h is in between the lower and upper bound of green
		return "G"
	elif WHITE_H[0] <= h <= WHITE_H[1]: # if h is in between the lower and upper bound of white
		# white and yellow's H value overlaps, check for S value
		if WHITE_S[0] <= s <= WHITE_S[1]:
			return "W"
		else:
			return "Y"
	elif RED_H[0] <= h <= RED_H[1] or RED_H[2] <= h <= RED_H[3]: # if h is in between the lower and upper bound of red
		# red and orange's H value overlaps, check for V value
		if RED_V[0] <= v <= RED_V[1]:
			return "R"
		else:
			return "O"
	else:
		return "U"
	
# return a 6x3x3 array that represents the colors of each facet
def recognizeColor():
	colorMatrices = [[["U" for k in range(3)] for j in range(3)] for i in range(6)]
	for i in range(6):
		colorMatrices[i] = recognizeColorFacet(i)
		colorToSideDict[colorMatrices[i][TILE_PER_SIDE/2][TILE_PER_SIDE/2]] = indexToSideDict[i]
		print(recognizeColorFacet(i))
	return colorMatrices
	
# mark the boundary on a single facet and store it as a .jpg file
def markOneFacetBoundary(facetNumber):
	img = Image.open(FILE_NAMES[facetNumber])
	arr = numpy.array(img)
	for i in range(4):
		for y in range(yoff, yoff + width):
			arr[xoff + i*tileWidth][y][0] = 173
			arr[xoff + i*tileWidth][y][1] = 66
			arr[xoff + i*tileWidth][y][2] = 244
	for i in range(4):
		for x in range(xoff, xoff + width):
			arr[x][yoff + i*tileWidth][0] = 173
			arr[x][yoff + i*tileWidth][1] = 66
			arr[x][yoff + i*tileWidth][2] = 244
	newImg = Image.fromarray(arr)
	newImg.save("facet" + str(facetNumber) + "Marked.jpg")

# mark the boundaries on all facet files
def markBoundary():
	for i in range(6):
		markOneFacetBoundary(i)
		
def execute(algo):
	algoQ = Queue.Queue()
	for move in algo.split(" "):
		algoQ.put(move)
	while not algoQ.empty():
		sleep(0.5)
		nextMove = algoQ.get()
		myCube(nextMove)
		printRubik(myCube)
		executeOneMove(nextMove)
		
def startup():
	leftClawDetach()
	rightClawDetach()
	frontClawDetach()
	backClawDetach()
	sleep(3)
	leftClawAttach()
	rightClawAttach()
	frontClawAttach()
	backClawAttach()
	sleep(3)
	rightClawC()
	rightClawC()
	rightClawC()
	rightClawC()
	leftClawC()
	leftClawC()
	leftClawC()
	leftClawC()
	frontClawC()
	frontClawC()
	frontClawC()
	frontClawC()
	backClawC()
	backClawC()
	backClawC()
	backClawC()
	
# ---------- MAIN FUNCTION ----------
if "-h" in sys.argv:
	print("-xoff")
	print("-yoff")
	print("-ws Pass in a float to rescale the width\n A width that's too big will cause errors")
	print("-f Pass in a facet number for testing purposes")
	print("-s Pass in a integer from 1 to 10 specify the speed")
	exit(0)

# command line parsing
if "-xoff" in sys.argv:
	xoff = int(sys.argv[sys.argv.index("-xoff") + 1])
	
if "-yoff" in sys.argv:
	yoff = int(sys.argv[sys.argv.index("-yoff") + 1])
	
if "-ws" in sys.argv:
	widthScale = float(sys.argv[sys.argv.index("-ws") + 1])
	width = int(widthScale*width)
	tileWidth = width/TILE_PER_SIDE
	
if "-f" in sys.argv:
	tempFacetNumber = int(sys.argv[sys.argv.index("-f") + 1])

if "-s" in sys.argv:
	mechanicalAPI.speed = int(sys.argv[sys.argv.index("-s") + 1])
	mechanicalAPI.delay = delay = (53/21)/800/2/mechanicalAPI.speed
	
startup()
takeAllPictures()
markBoundary()
currentState = toStrRep(recognizeColor())
myCube(str(kociemba.solve(SOLVED_STATE, currentState)))
printRubik(myCube)
solution = str(kociemba.solve(currentState, SOLVED_STATE))
print(solution)
execute(solution)
