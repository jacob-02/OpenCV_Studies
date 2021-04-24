import cv2 as cv

image = cv.imread('/home/jacob3006/Pictures/My Photos/IMG-20200207-WA0146.jpg')

grey = cv.cvtColor(image, cv.COLOR_BGR2GRAY)

haar_cascade = cv.CascadeClassifier('haar_face.xml')    # Reads the lines of code and stores in the variable declared

faces_rect = haar_cascade.detectMultiScale(grey, scaleFactor=1.8)   # This scale factor is perfect. Tested for more than one image

print('Number of people ', len(faces_rect))

for (x, y, w, h) in faces_rect:
    cv.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), thickness=2)

cv.imshow('Detected Faces', image)

cv.waitKey(0)

capture = cv.VideoCapture(0)

haar_cascade = cv.CascadeClassifier('haar_face.xml')  # Reads the lines of code and stores in the variable declared

while True:
    isTrue, frames = capture.read()

    grey = cv.cvtColor(frames, cv.COLOR_BGR2GRAY)

    faces_rect = haar_cascade.detectMultiScale(grey,
                                               scaleFactor=1.6)  # This scale factor is perfect. Tested for more than one image

    print('Number of people ', len(faces_rect))

    for (x, y, w, h) in faces_rect:
        cv.rectangle(frames, (x, y), (x + w, y + h), (0, 255, 0), thickness=2)

    cv.imshow('Detected Faces', frames)

    if cv.waitKey(20) & 0xFF == ord('d'):
        break

capture.release()
cv.destroyAllWindows()
