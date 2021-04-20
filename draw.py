import cv2 as cv
import numpy as np

img = np.zeros((500, 500, 3), dtype='uint8')

img[200:300, 300:400] = 0, 255, 255  # This is the array values for the color green
cv.rectangle(img, (0, 0), (250, 250), (255, 255, 0),
             thickness=-1)  # Draws a rectangle on the image "img", from point (0,0) to (250,250) of the color from the array (255,255,0) with a line of thickness 2 or -1 which fills the rectangle
cv.rectangle(img, (0, 0), (img.shape[1] // 2, img.shape[0] // 2), (250, 250, 200), thickness=-1)    # This is used to cut the image in half and stuff like that

cv.circle(img, (250, 250), 40, (0, 250, 0), thickness=2)    # This is used to create the circle on the image following almost the same pattern as the rectangle

cv.line(img, (0, 0), (300, 300), (0, 100, 0), thickness=4)  # This follows the exact same syntax as the rectangle which kinda makes sense and makes this function redundant as we could actually just use the rectangle wala with the appropriate thickness

cv.putText(img, "Hello darkness smile friend", (0, 300), cv.FONT_HERSHEY_TRIPLEX, 1.0, (0, 255, 0), thickness=2)    # This is used to put texts on the screen. Basically I have to google a bit for values regarding the font face and if I want a specific color that too. The syntax for the functions are just popping up due to the IDE being sick. So this is all pretty chill

cv.imshow('Random', img)

cv.waitKey(0)
