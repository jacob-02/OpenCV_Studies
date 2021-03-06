import cv2 as cv
import numpy as np

image = cv.imread('/home/jacob3006/Pictures/tokuchi.jpeg')
blank = np.zeros((500, 500, 3), dtype='uint8')

cv.imshow('Anime', image)

grey = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
cv.imshow('Grey', grey)

edge = cv.Canny(image, 125, 175)
cv.imshow('Edge', edge)

ret, threshold = cv.threshold(grey, 125, 255,
                              cv.THRESH_BINARY)  # Any pixel values below 125 is white and those above 255 is black
cv.imshow('Threshold', threshold)

contours = cv.findContours(threshold, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)[0]
print("Number of contours is ", len(contours))

cv.drawContours(blank, contours, -1, (0, 0, 255), 2)
cv.imshow('Contours Drawn', blank)

cv.waitKey(0)
cv.destroyAllWindows()
