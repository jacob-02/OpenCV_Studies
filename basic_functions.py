import cv2 as cv

image = cv.imread('/home/jacob3006/Pictures/Screenshot from 2021-03-28 23-13-03.png')
cv.imshow('Anime', image)

# Converting an image into a greyscale

grey = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
cv.imshow('Anime Grey', grey)

# Blurring an image

blur = cv.GaussianBlur(image, (9, 9), cv.BORDER_DEFAULT)
cv.imshow('Anime Blurred', blur)

# Finding the edges in an image

edged = cv.Canny(image, 125, 175)
cv.imshow('Edged Version', edged)

# Sharpening the images formed due to use of canny

dilated = cv.dilate(edged, (3, 3), iterations=1)
cv.imshow('Dilated', dilated)

# Eroding an image. It gets back the original edge cascaded image from the dilated image which thickens the edges to make them sharper or more visible

eroded = cv.erode(dilated, (3, 3), iterations=1)
cv.imshow('Eroded', eroded)

# Resizing an image using the cv.resize function. It doesn't give a damn about the aspect ratio of the image and just cuts it off

resized = cv.resize(image, (2000, 2000), interpolation=cv.INTER_AREA)
cv.imshow('Resized', resized)

# Cropping

cropped = image[50:200, 200:500]
cv.imshow('Cropped', cropped)

cv.waitKey(0)
