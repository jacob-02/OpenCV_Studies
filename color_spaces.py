import cv2 as cv

image = cv.imread('/home/jacob3006/Pictures/Screenshot from 2021-03-28 23-13-03.png')
cv.imshow('Anime', image)

# Converting to greyscale

grey = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
cv.imshow('Grey', grey)

# Converting to HSV

hsv = cv.cvtColor(image, cv.COLOR_BGR2HSV)
cv.imshow('HSV', hsv)

cv.waitKey(0)