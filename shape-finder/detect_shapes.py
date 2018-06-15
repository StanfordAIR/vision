# import the necessary packages
# python detect_shape.py --image example_shapes.png
from shapedetector import ShapeDetector
import argparse
import imutils
import cv2
import numpy as np

# construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True,
	help="path to the input image")
args = vars(ap.parse_args())

# load the image and resize it to a smaller factor so that
# the shapes can be approximated better
image = cv2.imread(args["image"], 1)
image = cv2.bitwise_not(image) #assume shape is passed in as lighter color, background darker
resized = imutils.resize(image, width=300)
ratio = image.shape[0] / float(resized.shape[0])

# convert the resized image to grayscale, blur it slightly,
# and threshold it
gray = cv2.cvtColor(resized, cv2.COLOR_BGR2GRAY)
blurred = cv2.GaussianBlur(gray, (5, 5), 0)
#smoothed = cv2.boxFilter(blurred, -1, (10, 10))
bilateral = cv2.bilateralFilter(blurred, 9,75,75)
thresh = cv2.threshold(bilateral, 60, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]
# cv2.imshow("original", image)
# cv2.waitKey(0)
# cv2.imshow("blur", blurred)
# cv2.waitKey(0)
# # cv2.imshow("smooth", smoothed)
# # cv2.waitKey(0)
# cv2.imshow("bilateral", bilateral)
# cv2.waitKey(0)
# cv2.imshow("thresh", thresh)
# cv2.waitKey(0)

#use houghcircles to find circles, then find polygons

# find contours in the thresholded image and initialize the
# shape detector
cnts = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL,
	cv2.CHAIN_APPROX_SIMPLE)
cnts = cnts[0] if imutils.is_cv2() else cnts[1]
sd = ShapeDetector()

# loop over the contours
for c in cnts:
	#print c
	# compute the center of the contour, then detect the name of the
	# shape using only the contour
	M = cv2.moments(c)
	cX = int((M["m10"] / M["m00"]) * ratio)
	cY = int((M["m01"] / M["m00"]) * ratio)
	shape = sd.detect(c)
	# multiply the contour (x, y)-coordinates by the resize ratio,
	# then draw the contours and the name of the shape on the image
	# can comment out, uncomment to debug
	# c = c.astype("float")
	# c *= ratio
	# c = c.astype("int")
	# cv2.drawContours(image, [c], -1, (0, 255, 0), 2)
	# cv2.putText(image, shape, (cX, cY), cv2.FONT_HERSHEY_SIMPLEX,
	# 	0.5, (255, 255, 255), 2)
	# # show the output image
	# cv2.imshow("Image", image)
	# cv2.waitKey(0)
