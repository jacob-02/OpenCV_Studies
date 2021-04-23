import cv2 as cv

image = cv.imread('/home/jacob3006/Pictures/Screenshot from 2021-04-04 23-41-07.png')
cv.imshow('Image', image)

cv.waitKey(0)