import cv2 as cv
import numpy as np

image = cv.imread('Images/img.png')
cv.imshow('Cat', image)

cv.waitKey(0)