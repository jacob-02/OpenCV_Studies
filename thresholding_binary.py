import cv2 as cv

image = cv.imread('/home/jacob3006/PycharmProjects/OpenCV_Studies/Images/img.png')
cv.imshow('image', image)

grey = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
cv.imshow('GREY', grey)

# Simple Thresholding
threshold, thresh = cv.threshold(grey, 225, 225, cv.THRESH_BINARY)  # Makes the values of the pixels above the maxval to maxl val and others to 0
cv.imshow('Threshold', thresh)

# Inverse Thresholding
threshold1, thresh1 = cv.threshold(grey, 225, 225, cv.THRESH_BINARY_INV)
cv.imshow('Inverse Thresholding', thresh1)

cv.waitKey(0)