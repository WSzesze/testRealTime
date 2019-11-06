# import the necessary packages
import numpy as np
import imutils
import cv2


class SingleMotionDetector:
	def __init__(self, accumWeight=0.7):
		# store the accumulated weight factor
		self.accumWeight = accumWeight

		# initialize the background model
		self.bg = None

	def update(self, image):
		# if the background model is None, initialize it
		if self.bg is None:
			self.bg = image.copy().astype("float")
			return

		# update the background model by accumulating the weighted

		# average
		cv2.accumulateWeighted(image, self.bg, self.accumWeight)

	def detect(self, image, tVal=25):
		# compute the absolute difference between the background model
		# and the image passed in, then threshold the delta image
		delta = cv2.absdiff(self.bg.astype("uint8"), image)
		thresh = cv2.threshold(delta, tVal, 255, cv2.THRESH_BINARY)[1]
		# perform a series of erosions and dilations to remove small
		# blobs
		thresh = cv2.erode(thresh, None, iterations=2)
		thresh = cv2.dilate(thresh, None, iterations=2)


		# area1 = np.array([[250, 200], [300, 100], [750, 800], [100, 50]])
		# area2 = np.array([[1000, 200], [1500, 200], [1500, 400], [1000, 400]])

		# cv2.fillPoly(image, [area1], (255, 255, 255))

		# find contours in the thresholded image and initialize the
		# minimum and maximum bounding box regions for motion
		cnts = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
		cnts = imutils.grab_contours(cnts)
		(minX, minY) = (np.inf, np.inf)
		(maxX, maxY) = (-np.inf, -np.inf)

		# if no contours were found, return None
		if len(cnts) == 0:
			return None

		# otherwise, loop over the contours
		for c in cnts:
			# compute the bounding box of the contour and use it to
			# update the minimum and maximum bounding box regions
			(x, y, w, h) = cv2.boundingRect(c)
			(minX, minY) = (min(minX, x), min(minY, y))
			(maxX, maxY) = (max(maxX, x + w), max(maxY, y + h))

		# otherwise, return a tuple of the thresholded image along
		# with bounding box
		return (thresh, (minX, minY, maxX, maxY))

	# def drawrect(self, image):
	# 	# hollow polygon
	# 	pts = np.array([[475, 158], [509, 195], [743, 191], [680, 150]], np.int32)
	# 	cv2.polylines(image, [pts], True, (0, 255, 255), 3)
	#
	# 	# text
	# 	font = cv2.FONT_HERSHEY_SIMPLEX
	# 	cv2.putText(image, 'Cell 1', (480, 168), font, 0.6, (0, 0, 0), 2, cv2.LINE_AA)
	#
	# 	return


