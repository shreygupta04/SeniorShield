import cv2
from picamera.array import PiRGBArray
from picamera import PiCamera
import numpy as np 
import pickle
import RPi.GPIO as GPIO
from time import sleep
import pyrebase

config = {
    "apiKey": "AIzaSyDP0mHM4XP-us0a3sHd5QojTSObnwXJDQo",
    "authDomain": "seniorshield-84d95.firebaseapp.com",
    "databaseURL": "https://seniorshield-84d95-default-rtdb.firebaseio.com",
    "projectId": "seniorshield-84d95",
    "storageBucket": "seniorshield-84d95.appspot.com",
    "messagingSenderId": "475934775503",
    "appId": "1:475934775503:web:077a1a5614ed4c2c63bfba"
}

firebase = pyrebase.initialize_app(config)
db = firebase.database()


with open('labels', 'rb') as f:
	dicti = pickle.load(f)
	f.close()

camera = PiCamera()
camera.resolution = (640, 480)
camera.framerate = 30
rawCapture = PiRGBArray(camera, size=(640, 480))


faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read("trainer.yml")

font = cv2.FONT_HERSHEY_SIMPLEX

tick = 0  

for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
    tick+=1
    frame = frame.array
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = faceCascade.detectMultiScale(gray, scaleFactor = 1.5, minNeighbors = 5)
    for (x, y, w, h) in faces:
        roiGray = gray[y:y+h, x:x+w]

        id_, conf = recognizer.predict(roiGray)

        for name, value in dicti.items():
            if value == id_:
                print(name)

        if conf <= 70:
            # GPIO.output(relay_pin, 1)
            # print("Open the door, this person is there: " + name)
            db.update({"name": name})
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
            cv2.putText(frame, name + str(conf), (x, y), font, 2, (0, 0 ,255), 2,cv2.LINE_AA)


    cv2.imshow('frame', frame)
    key = cv2.waitKey(1)

    rawCapture.truncate(0)

    if key == 27 or tick==45:
        break

db.update({"name": ""})
cv2.destroyAllWindows()