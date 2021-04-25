import numpy as np
import cv2 as cv
import os

haar_cascade = cv.CascadeClassifier('haar_face.xml')

people = []

for i in os.listdir('Images'):
    people.append(i)

features = np.load('features.npy')
labels = np.load('labels.npy')

face_recognizer = cv.face.createLBPHFaceRecognizer()
face_recognizer.read('face_trainer.yml')

image = cv.imread('Images/1/IMG_20201206_174519.jpg')

grey = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
cv.imshow('Random Person', grey)