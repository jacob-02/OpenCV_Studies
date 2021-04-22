import cv2 as cv

capture = cv.VideoCapture(0)  # We can also use integers instead of the path file. Those reference cameras.
while True:
    isTrue, frame = capture.read()
    cv.imshow('Anime', frame)
    if cv.waitKey(20) & 0xFF == ord('d'):
        break
capture.release()
cv.destroyAllWindows()

# -215 assertion failed error occurs due to lack of the file being present at the specified location
