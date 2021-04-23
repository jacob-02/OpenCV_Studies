import cv2 as cv
import matplotlib.pyplot as plt

image = cv.imread('/home/jacob3006/PycharmProjects/OpenCV_Studies/Images/img.png')
cv.imshow('Cats', image)

grey = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
cv.imshow('Grey', grey)

# GreyScale Histogram
grey_hist = cv.calcHist([grey], [0], None, histSize=[256], ranges=[0, 256])

plt.figure()
plt.title('GreyScale Histogram')
plt.xlabel('Bins')
plt.ylabel('# of pixels')
plt.plot(grey_hist)
plt.xlim([0, 256])
plt.show()

cv.waitKey(0)
