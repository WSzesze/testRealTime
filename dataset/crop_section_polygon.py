import cv2
import numpy as np
import imutils

source = "rtsp://192.168.1.106:554/ch1/main/av_stream"
cap = cv2.VideoCapture(source)

if cap.isOpened():
    cv2.namedWindow("demo", cv2.WINDOW_AUTOSIZE)

    while True:
        ret_val, frame = cap.read()
        # filled polygon
        image = cv2.imread('cover1.jpg')
        #frame = imutils.resize(image, width=200)
        alpha = 0.4 # Transparency factor.
        #rectangle = np.array([[0, 0], [320, 0], [1200, 1000], [0, 1980]])
        #cover = cv2.fillConvexPoly(img, rectangle, (0, 0, 0), 4)
        added_image = cv2.addWeighted(frame, alpha, image, 1-alpha, 0)
        img = cv2.resize(added_image, (0, 0), fx=0.69, fy=0.65)  # resize image half
        # Cell 1
        # hollow polygon
        #pts = np.array([[475, 158], [509, 195], [743, 191], [680, 150]], np.int32)
        #cv2.polylines(img, [pts], True, (0, 255, 255), 3)
        # text
        #font = cv2.FONT_HERSHEY_SIMPLEX
        #cv2.putText(img, 'Cell 1', (480, 168), font, 0.6, (0, 0, 0), 2, cv2.LINE_AA)

        # Cell 2
        # hollow polygon
        #pts = np.array([[509, 195], [553, 248], [824, 247], [743, 191]], np.int32)
        #cv2.polylines(img, [pts], True, (0, 255, 255), 3)
        # text
        #font = cv2.FONT_HERSHEY_SIMPLEX
        #cv2.putText(img, 'Cell 2', (515, 210), font, 0.6, (0, 0, 0), 2, cv2.LINE_AA)

        cv2.imshow('demo', img)
        k = cv2.waitKey(10)

        # press a to increase alpha by 0.1
        if k == ord('a'):
            alpha += 0.1
            if alpha >= 1.0:
                alpha = 1.0
        # press d to decrease alpha by 0.1
        elif k == ord('d'):
            alpha -= 0.1
            if alpha <= 0.0:
                alpha = 0.0

        if k & 0xFF == ord('q'):
            break


else:
    print("camera open failed")

cap.release()
cv2.destroyAllWindows()
