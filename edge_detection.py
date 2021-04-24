import cv2 as cv
import numpy as np

image = cv.imread('/home/jacob3006/PycharmProjects/OpenCV_Studies/Images/img.png')
cv.imshow('Image', image)

grey = cv.cvtColor(image, cv.COLOR_BGR2GRAY)

# Laplacion Method
lap = cv.Laplacian(grey, cv.CV_64F)
lap = np.uint8(np.absolute(lap))

cv.imshow('Laplacian', lap)

cv.waitKey(0)