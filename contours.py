import cv2 as cv

image = cv.imread('/home/jacob3006/Pictures/Screenshot from 2021-03-28 23-13-03.png')

cv.imshow('Anime', image)

grey = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
cv.imshow('Grey', grey)

edge = cv.Canny(image, 125, 175)
cv.imshow('Edge', edge)

ret, threshold = cv.threshold(grey, 125, 255,
                              cv.THRESH_BINARY)  # Any pixel values below 125 is white and those above 255 is black
cv.imshow('Threshold', threshold)

contours = cv.findContours(threshold, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)
print("Number of contours is ", len(contours))

cv.waitKey(0)
