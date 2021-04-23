import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np

image = cv.imread('/home/jacob3006/PycharmProjects/OpenCV_Studies/Images/img.png')
cv.imshow('Cats', image)

blank = np.zeros(image.shape[:2], dtype='uint8')
cv.imshow('Blank', blank)

circle = cv.circle(blank.copy(), (image.shape[1] // 2, image.shape[0] // 2), 60, 255, -1)

grey = cv.cvtColor(image, cv.COLOR_BGR2GRAY)

mask = cv.bitwise_and(grey, grey, mask=circle)
cv.imshow('Grey', mask)

# GreyScale Histogram
grey_hist = cv.calcHist([grey], [0], mask, histSize=[256], ranges=[0, 256])

plt.figure()
plt.title('GreyScale Histogram')
plt.xlabel('Bins')
plt.ylabel('# of pixels')
plt.plot(grey_hist)
plt.xlim([0, 256])
plt.show()

# Computing histograms for colored images

plt.figure()
plt.title('Color Histogram')
plt.xlabel('Bins')
plt.ylabel('# of pixels')

colors = ('b', 'g', 'r')
for i, col in enumerate(colors):
    hist = cv.calcHist([image], [i], None, [256], [0, 256])
    plt.plot(hist, color=col)
    plt.xlim([0, 256])

plt.show()

mask = cv.bitwise_and(grey, grey, mask=circle)
cv.imshow('Grey', mask)

cv.waitKey(0)
