import cv2 as cv
import numpy as np


def translate(image, x, y):
    transMat = np.float32([[1, 0, x], [0, 1, y]])
    dimensions = (image.shape[1], image.shape[0])

    return cv.warpAffine(image, transMat, dimensions)


# negative values of x translates to the left
# negative values of y translates to the top

image = cv.imread('/home/jacob3006/Pictures/Screenshot from 2021-03-28 23-13-03.png')

translated = translate(image, 1000, 100)

cv.imshow('Translated', translated)

cv.waitKey(0)
