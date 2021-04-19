import cv2 as cv

'''
This method works only for live videos. 
Here we are going to change the resolution of the video that we feed using the cameras to a set width and height
'''


def changeRes(frame, width, height):
    frame.set(3, width)
    frame.set(4, height)

    return frame


# Sample code to show the running of the function
capture = cv.VideoCapture(0)
changeRes(capture, 1, 0.02)
while True:
    isTrue, frame = capture.read()
    cv.imshow('Webcam', frame)

    if cv.waitKey(20) & 0xFF == ord('d'):
        break

capture.release()
cv.destroyAllWindows()
