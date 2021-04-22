import cv2 as cv
import numpy as np

blank = np.zeros((400, 400), dtype='uint8')

rectangle = cv.rectangle(blank.copy(), (30, 30), (370, 370), 255, -1)

circle = cv.circle(blank.copy(), (200, 200), 200, 255, -1)

cv.imshow('Rectangle', rectangle)
cv.imshow('Circle', circle)

# BITWISE And

bitwise_and = cv.bitwise_and(circle, rectangle)
cv.imshow('AND', bitwise_and)

# BITWISE Or

bitwise_or = cv.bitwise_or(circle, rectangle)
cv.imshow('OR', bitwise_or)

# BITWISE XOR

bitwise_xor = cv.bitwise_xor(circle, rectangle)
cv.imshow('XOR', bitwise_xor)

# BITWISE NOT

bitwise_nor = cv.bitwise_not(circle)
bitwise_nor1 = cv.bitwise_not(rectangle)
cv.imshow('NOR 1', bitwise_nor)
cv.imshow('NOR 2', bitwise_nor1)

cv.waitKey(0)