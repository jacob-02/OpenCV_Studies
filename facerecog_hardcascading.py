import cv2 as cv
import numpy as np

image = cv.imread('/home/jacob3006/Pictures/My Photos/IMG-20200207-WA0146.jpg')
cv.imshow('Person', image)

grey = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
cv.imshow('Grey', grey)

haar_cascade = cv.CascadeClassifier('haar_face.xml')    # Reads the lines of code and stores in the variable declared

faces_rect = haar_cascade.detectMultiScale(grey, scaleFactor=1.8)   # This scale factor is perfect. Tested for more than one image

print('Number of people ', len(faces_rect))

cv.waitKey(0)