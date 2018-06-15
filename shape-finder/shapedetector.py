# import the necessary packages
import cv2

class ShapeDetector:
	def __init__(self):
		pass

	def detect(self, c):
		# initialize the shape name and approximate the contour
		shape = "unidentified"
		# print c.shape
		# circles = cv2.HoughCircles(c, cv2.HOUGH_GRADIENT, 1, 20)
		# print circles
		peri = cv2.arcLength(c, True)
		approx = cv2.approxPolyDP(c, 0.04 * peri, True) #.04

		# if the shape is a triangle, it will have 3 vertices
		if len(approx) == 3:
			shape = "triangle"
			print "triangle"
		#can also be quarter circle

		# if the shape has 4 vertices, it is either a square or
		# a rectangle
		elif len(approx) == 4:
			# compute the bounding box of the contour and use the
			# bounding box to compute the aspect ratio
			(x, y, w, h) = cv2.boundingRect(approx)
			ar = w / float(h)

			# a square will have an aspect ratio that is approximately
			# equal to one, otherwise, the shape is a rectangle
			if ar >= 0.95 and ar <= 1.05:
				shape = "square"
				print "square"
			else:
				shape = "rectangle"
				print "rectangle"
			#need trapezoid

		# if the shape is a pentagon, it will have 5 vertices
		elif len(approx) == 5:
			shape = "pentagon"
			print "pentagon"

		elif len(approx) == 6:
			shape = "hexagon"
			print "hexagon"

		elif len(approx) == 7:
			shape = "heptagon"
			print "heptagon"

		elif len(approx) == 8:
			shape = "octagon"
			print "octagon"

		elif len(approx) == 10:
			shape = "star"
			print "star"

		elif len(approx) == 12:
			shape = "cross"
			print "cross"
		# otherwise, we assume the shape is a circle
		else:
			shape = "circle"
			print "circle"

		# return the name of the shape
		return shape
