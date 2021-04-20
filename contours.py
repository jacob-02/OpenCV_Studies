import cv2 as cv

image = cv.imread('/home/jacob3006/Pictures/Screenshot from 2021-03-28 23-13-03.png')

cv.imshow('Anime', image)

grey = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
edge = cv.Canny(image, 125, 175)

contours, hierarchy = cv.findContours(image, cv.RETR_LIST, cv.CHAIN_APPROX_NONE)

cv.waitKey(0)