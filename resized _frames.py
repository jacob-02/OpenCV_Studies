import cv2 as cv
from resizing import *

capture = cv.VideoCapture(
    '/home/jacob3006/Videos/st23_naruto-shippuuden-dub-episode-476.1618454201.mp4')  # We can also use integers instead of the path file. Those reference cameras.
while True:
    isTrue, frame = capture.read()
    frame_resized = resize(frame, 2)
    cv.imshow('Anime', frame_resized)
    if cv.waitKey(20) & 0xFF == ord('d'):
        break
capture.release()
cv.destroyAllWindows()

# -215 assertion failed error occurs due to lack of the file being present at the specified location
