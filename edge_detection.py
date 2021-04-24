import cv2
import cv2 as cv
import numpy as np

image = cv.imread('/home/jacob3006/PycharmProjects/OpenCV_Studies/Images/img.png')
cv.imshow('Image', image)

grey = cv.cvtColor(image, cv.COLOR_BGR2GRAY)

# Laplacian Method
lap = cv.Laplacian(grey, cv.CV_64F)
lap = np.uint8(np.absolute(lap))

cv.imshow('Laplacian', lap)

# Sobel
sobelx = cv2.Sobel(grey, cv.CV_64F, 1, 0)
sobely = cv2.Sobel(grey, cv.CV_64F, 0, 1)

combined_sobel = cv.bitwise_or(sobelx, sobely)

cv.imshow('SobelX', sobelx)
cv.imshow('SobelY', sobely)

cv.imshow('Combined Sobel', combined_sobel)

canny = cv.Canny(grey, 150, 175)
cv.imshow('Canny', canny)

cv.waitKey(0)