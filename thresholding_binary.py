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

# Adaptive Thresholding
adaptive_thresh = cv.adaptiveThreshold(grey, 155, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, blockSize=21, C=1)   # Computes the optimal thresholding value to average of the surrounding pixels. Kinda like your blurring
cv.imshow('Adaptive Thresholding', adaptive_thresh)

# Gaussian Thresholding
gaussian_thresh = cv.adaptiveThreshold(grey, 155, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, blockSize=21, C=1)   # Computes the optimal thresholding value to average of the surrounding pixels of their weight. Kinda like your blurring
cv.imshow('Gaussian Adaptive Thresholding', gaussian_thresh)

cv.waitKey(0)