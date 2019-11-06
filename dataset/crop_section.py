import cv2
import numpy as np
import os,sqlite3

# Record faces
conn = sqlite3.connect('database.db')

if not os.path.exists('./dataset'):
    os.makedirs('./dataset')

c = conn.cursor()
cap = cv2.VideoCapture("rtsp://192.168.1.115:554/ch1/main/av_stream")
sampleNum = 0

while True:
  ret, img = cap.read()
  sampleNum = sampleNum + 1
  cv2.imwrite("dataset/Image." + str(sampleNum) + ".jpg", img)
  cv2.imshow('img', img)
  cv2.waitKey(1)

  if sampleNum > 1:
      break

  if cv2.waitKey(1) & 0xff == ord('q'):
    break

cap.release()
conn.commit()
conn.close()
cv2.destroyAllWindows()

