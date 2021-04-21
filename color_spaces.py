import cv2 as cv
import matplotlib.pyplot as plt

image = cv.imread('/home/jacob3006/Pictures/Screenshot from 2021-03-28 23-13-03.png')
cv.imshow('Anime', image)

plt.imshow(image)
plt.show()

# Direct conversions from one scale to another without converting it into bgr in between is not possible
# Converting to greyscale

grey = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
cv.imshow('Grey', grey)

# Converting to HSV

hsv = cv.cvtColor(image, cv.COLOR_BGR2HSV)
cv.imshow('HSV', hsv)

# Converting to L*a*b

lab = cv.cvtColor(image, cv.COLOR_BGR2Lab)
cv.imshow("LAB", lab)

# Showing the images in RGB

rgb = cv.cvtColor(image, cv.COLOR_BGR2RGB)
cv.imshow("RGB", rgb)


cv.waitKey(0)