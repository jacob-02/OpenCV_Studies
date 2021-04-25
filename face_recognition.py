import numpy as np
import cv2 as cv
import os

haar_cascade = cv.CascadeClassifier('haar_face.xml')

people = []

for i in os.listdir('Images'):
    people.append(i)

face_recognizer = cv.face.createLBPHFaceRecognizer()
face_recognizer.load('face_trainer.yml')

capture = cv.VideoCapture(0)

while True:
    isTrue, image = capture.read()
    cv.imshow('Webcam', image)

    grey = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    cv.imshow('Random Person', grey)

    # Detect the face in the image

    face_rect = haar_cascade.detectMultiScale(grey, scaleFactor=1.3)

    for (x, y, w, h) in face_rect:
        faces_roi = grey[y:y+h, x:x+w]

        label, confidence = face_recognizer.predict(faces_roi)
        print(f'Label = {people[label]} with confidence of {confidence}')

        cv.putText(image, str(people[label]), (20, 20), cv.FONT_HERSHEY_COMPLEX, 1.0, (0, 255, 0), thickness=2)
        cv.putText(image, str(confidence), (100, 100), cv.FONT_HERSHEY_COMPLEX, 1.0, (0, 255, 0), thickness=2)
        cv.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), thickness=2)

    cv.imshow('Detected Face', image)
    if cv.waitKey(20) & 0xFF == ord('d'):
        break

capture.release()
cv.destroyAllWindows()