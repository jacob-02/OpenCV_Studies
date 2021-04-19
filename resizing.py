import cv2 as cv


def resize(frame, scale=0.75):          # The scale refers to the size wanted by the original size into 1
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)

    dimensions = (width, height)

    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)


