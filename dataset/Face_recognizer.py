import cv2
import numpy as np
import sqlite3
import os
from PIL import Image

# Create database
conn = sqlite3.connect('database.db')
c = conn.cursor()
sql = """
DROP TABLE IF EXISTS users;
CREATE TABLE users (
           id integer unique primary key autoincrement,
           name text
);
"""

c.executescript(sql)
conn.commit()
conn.close()


# Record faces
conn = sqlite3.connect('database.db')

if not os.path.exists('./dataset'):
    os.makedirs('./dataset')

c = conn.cursor()
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
cap = cv2.VideoCapture(0)
uname = input("Enter your name: ")
c.execute('INSERT INTO users (name) VALUES (?)', (uname,))
uid = c.lastrowid
sampleNum = 0


while True:
  ret, img = cap.read()
  gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
  faces = face_cascade.detectMultiScale(gray, 1.3, 5)

  for (x,y,w,h) in faces:
    sampleNum = sampleNum+1
    cv2.imwrite("dataset/User."+str(uid)+"."+str(sampleNum)+".jpg",gray[y:y+h,x:x+w])
    cv2.rectangle(img, (x,y), (x+w, y+h), (255,0,0), 2)
    cv2.waitKey(100)

  cv2.imshow('img',img)
  cv2.waitKey(1)

  if sampleNum > 100:
    break

cap.release()
conn.commit()
conn.close()
cv2.destroyAllWindows()

# Train recognizer
recognizer = cv2.face_LBPHFaceRecognizer.create()
path = 'dataset'

if not os.path.exists('./recognizer'):
    os.makedirs('./recognizer')


def getImagesWithID(path):
  imagePaths = [os.path.join(path,f) for f in os.listdir(path)]
  faces = []
  IDs = []

  for imagePath in imagePaths:
    faceImg = Image.open(imagePath).convert('L')
    faceNp = np.array(faceImg,'uint8')
    ID = int(os.path.split(imagePath)[-1].split('.')[1])
    faces.append(faceNp)
    IDs.append(ID)
    cv2.imshow("training",faceNp)
    cv2.waitKey(10)
  return np.array(IDs), faces

Ids, faces = getImagesWithID(path)
recognizer.train(faces,Ids)
recognizer.save('recognizer/trainingData.yml')
cv2.destroyAllWindows()

# Detector
conn = sqlite3.connect('database.db')
c = conn.cursor()
fname = "recognizer/trainingData.yml"

if not os.path.isfile(fname):
  print("Please train the data first")
  exit(0)

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
cap = cv2.VideoCapture(0)
recognizer = cv2.face_LBPHFaceRecognizer.create()
recognizer.read(fname)


while True:
  ret, img = cap.read()
  gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
  faces = face_cascade.detectMultiScale(gray, 1.3, 5)

  for (x,y,w,h) in faces:
    cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)
    ids,conf = recognizer.predict(gray[y:y+h,x:x+w])
    c.execute("select name from users where id = (?);", (ids,))
    result = c.fetchall()
    name = result[0][0]

    if conf < 50:
      cv2.putText(img, name, (x+2,y+h-5), cv2.FONT_HERSHEY_SIMPLEX, 1, (150,255,0),2)
    else:
      cv2.putText(img, 'No Match', (x+2,y+h-5), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,255),2)

  cv2.imshow('Face Recognizer',img)

  if cv2.waitKey(1) & 0xff == ord('q'):
    break


cap.release()
cv2.destroyAllWindows()