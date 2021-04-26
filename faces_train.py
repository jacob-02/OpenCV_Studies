import cv2 as cv
import os
import numpy as np

people = []
DIR = r'Images'

haar_cascade = cv.CascadeClassifier('haar_face.xml')

for i in os.listdir('Images'):
    people.append(i)

features = []
labels = []


def create_train():
    for person in people:
        path = os.path.join(DIR, person)
        label = people.index(person)

        for image in os.listdir(path):
            image_path = os.path.join(path, image)

            image_array = cv.imread(image_path)
            grey = cv.cvtColor(image_array, cv.COLOR_BGR2GRAY)

            faces_rect = haar_cascade.detectMultiScale(grey, scaleFactor=1.8)

            for (x, y, w, h) in faces_rect:
                faces_roi = grey[y:y + h, x:x + w]

            features.append(faces_roi)
            labels.append(label)


create_train()

print('Training done ------------------')

features = np.array(features, dtype='object')
labels = np.array(labels)

face_recognizer = cv.face.LBPHFaceRecognizer_create()

# Training the model on the features and labels list

face_recognizer.train(features, labels)

face_recognizer.save('face_trainer.yml')

np.save('features.npy', features)
np.save('labels.npy', labels)

cv.waitKey(0)
