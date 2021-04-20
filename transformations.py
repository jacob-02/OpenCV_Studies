import cv2 as cv
import numpy as np


# translation
def translate(img, x, y):
    transMat = np.float32([[1, 0, x], [0, 1, y]])
    dimensions = (img.shape[1], img.shape[0])

    return cv.warpAffine(img, transMat, dimensions)


# rotation

def rotate(img, angle, rotPoint=None):
    (height, width) = img.shape[:2]

    if rotPoint is None:
        rotPoint = (width // 2, height // 2)

    rotMat = cv.getRotationMatrix2D(rotPoint, angle, scale=1.0)

    dimensions = (width, height)

    return cv.warpAffine(img, rotMat, dimensions)


# negative values of x translates to the left
# negative values of y translates to the top

image = cv.imread('/home/jacob3006/Pictures/Screenshot from 2021-03-28 23-13-03.png')

translated = translate(image, 1000, 100)
cv.imshow('Translated', translated)

rotated = rotate(image, 45)
cv.imshow('Rotated', rotated)

cv.waitKey(0)
