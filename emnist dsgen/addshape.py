import cv2
from scipy import ndimage
import numpy as np
from random import randint
import imutils
import csv
import random

# for reference
# BLUE = [255,0,0]
# RED = [0, 0, 255]
# GREEN = [0, 255, 0]
# YELLOW = [0, 255, 255]

imgDim = 100

emnist = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabdefghnqrt"

for m in range(0,100): # todo: parallelize, make more efficient, resize?, skew?
	ind=0
	charInd = randint(0,112000)
	char = []
	with open('emnist-balanced-train.csv', 'rb') as csvfile:
		charReader = csv.reader(csvfile, delimiter=' ', quotechar='|')
		for i, row in enumerate(charReader):
			if i == charInd:
				char = row
				break

	char = char[0].split(",")
	alphanum = int(char[0])
	randColor1 = randint(0,100)
	randColor2 = randint(0,100)
	randColor3 = randint(0,100)

	randColorIndex = randint(0,3)

	if randColorIndex == 0:
		COLOR = [255-randColor1,randColor2,randColor3]
		c = "b"

	if randColorIndex == 1:
		COLOR = [randColor2,randColor2,255-randColor1]
		c = "r"

	if randColorIndex == 2:
		COLOR = [randColor2,255-randColor1,randColor2]
		c = "g"

	if randColorIndex == 3:
		COLOR = [randColor2,255-randColor1,255-randColor1]
		c = "y"

	nums = list()
	for index in range(0,3):
		if index != randColorIndex:
			nums.append(index)

	randColor2Index = random.choice(nums)

	if randColor2Index == 0:
		COLOR2 = [255-randColor1,randColor2,randColor3]
		c2 = "b"

	if randColor2Index == 1:
		COLOR2 = [randColor2,randColor2,255-randColor1]
		c2 = "r"

	if randColor2Index == 2:
		COLOR2 = [randColor2,255-randColor1,randColor2]
		c2 = "g"

	if randColor2Index == 3:
		COLOR2 = [randColor2,255-randColor1,255-randColor1]
		c2 = "y"

	randIndex = randint(0,9)

	img = cv2.imread("shape-template/"+str(randIndex)+".jpg")
	ind = 1
	mod = randint(-2,2)
	def addChar(x,y,char) {
		if int(char[charInd]) >= 10:
				img[x+35+mod,y+35+mod][0] = 0
				img[x+35+mod,y+35+mod][1] = 0
				img[x+35+mod,y+35+mod][2] = 70
	}
	vect = np.vectorize(addChar);
	vfunc(range(28), range(28), char)
	for y in range(28):
		for x in range(28):
			if int(char[ind]) >= 10:
				
				img[x+35+mod,y+35+mod][0] = 0
				img[x+35+mod,y+35+mod][1] = 0
				img[x+35+mod,y+35+mod][2] = 70
			ind+=1
	img = imutils.rotate(img, randint(0,360))
	#img = imutils.resize(img, width=randint(100,140))
	bg = cv2.imread("backgrounds/background"+str(m)+".png")
	centerX = randint(-25,25)
	centerY = randint(-25,25)
	for x in range(imgDim):
		for y in range(imgDim):
			if img[x,y][0] >= 200 and img[x,y][1] >= 200 and img[x,y][2] >= 200:
				if x+centerX >= 0 and x+centerX < 100 and y+centerY >= 0 and y+centerY < 100:
					r = randint(-25,25)
					bg[x+centerX,y+centerY][0] = max(min(COLOR[0] + randint(-10,10) + r,255),0)
					bg[x+centerX,y+centerY][1] = max(min(COLOR[1] + randint(-10,10) + r,255),0)
					bg[x+centerX,y+centerY][2] = max(min(COLOR[2] + randint(-10,10) + r,255),0)
			if img[x,y][0] <= 10 and img[x,y][1] <= 10 and img[x,y][2] >= 55 and img[x,y][2] <= 85:
				if x+centerX >= 0 and x+centerX < 100 and y+centerY >= 0 and y+centerY < 100:
					r = randint(-25,25)
					bg[x+centerX,y+centerY][0] = max(min(COLOR2[0] + randint(-10,10) + r,255),0)
					bg[x+centerX,y+centerY][1] = max(min(COLOR2[1] + randint(-10,10) + r,255),0)
					bg[x+centerX,y+centerY][2] = max(min(COLOR2[2] + randint(-10,10) + r,255),0)
	cv2.imwrite("data/num"+str(m)+"-char"+emnist[alphanum]+"-shape"+str(randIndex)+"-c_color"+c2+"-s_color"+c+".png", bg)

	
