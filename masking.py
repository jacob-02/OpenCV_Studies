import cv2 as cv
import numpy as np

capture = cv.VideoCapture(0)

while True:
    isTrue, frame = capture.read()

    blank = np.zeros(frame.shape[:2], dtype='uint8')
    cv.imshow('Blank', blank)

    mask = cv.circle(blank, (frame.shape[1] // 2, frame.shape[0] // 2), 100, 255, -1)
    cv.imshow('Mask', mask)

    masked1 = cv.bitwise_and(frame, frame, mask=mask)
    cv.imshow('Anime', masked1)

    if cv.waitKey(20) & 0xFF == ord('d'):
        break

capture.release()
cv.destroyAllWindows()

cv.waitKey(0)