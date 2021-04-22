import cv2 as cv

image = cv.imread('/home/jacob3006/PycharmProjects/OpenCV_Studies/Images/img.png')
cv.imshow('Cats', image)

# Averaging blurring method

average = cv.blur(image, (3, 3))
cv.imshow('Average Blur', average)

cv.waitKey(0)
