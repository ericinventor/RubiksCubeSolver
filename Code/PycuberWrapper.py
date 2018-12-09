class color:
	black = '\033[40m' + " " + '\033[49m'
	red = '\033[41m' + " " + '\033[49m'
	green = '\033[42m' + " " + '\033[49m'
	yellow = '\033[103m' + " " + '\033[49m'
	blue = '\033[44m' + " " + '\033[49m'
	white = '\033[107m' + " " + '\033[49m'
	orange = '\033[43m' + " " + '\033[49m'

def printRubik(rubikCube):
	colorRubik = ""
	for c in str(rubikCube):
		if c is 'y':
			colorRubik = colorRubik + color.yellow
		elif c is 'r':
			colorRubik = colorRubik + color.red
		elif c is 'g':
			colorRubik = colorRubik + color.green
		elif c is 'o':
			colorRubik = colorRubik + color.orange
		elif c is 'b':
			colorRubik = colorRubik + color.blue
		elif c is 'w':
			colorRubik = colorRubik + color.white
		elif c == ' ':
			colorRubik = colorRubik + " "
		elif c == '\n':
			colorRubik = colorRubik + '\n'
		else:
			pass
	print(coloRubik)
