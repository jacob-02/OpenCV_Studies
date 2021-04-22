import cv2 as cv

image = cv.imread('/home/jacob3006/PycharmProjects/OpenCV_Studies/Images/img.png')
cv.imshow('Cats', image)

# Averaging blurring method

average = cv.blur(image, (7, 7))
cv.imshow('Average Blur', average)

# Gaussian Blur - does the same as averaging, it takes the 'weight' of the surrounding pixels - causes less blurring but is more natural

gaussian = cv.GaussianBlur(image, (7, 7), 0)
cv.imshow('Gaussian', gaussian)

# Median blur but instead of finding the average, it finds the median. It removes the noise better than both other methods

median = cv.medianBlur(image, 7)
cv.imshow('Median', median)

# Bilateral blurring - most effective technique of the all methods

bilateral = cv.bilateralFilter(image, 10, sigmaColor=35, sigmaSpace=25)
cv.imshow('Bilateral', bilateral)

cv.waitKey(0)
