import cv2
import numpy as np

source = "rtsp://192.168.1.112:554/ch1/main/av_stream"
cap = cv2.VideoCapture(source)

if cap.isOpened():
        cv2.namedWindow("demo", cv2.WINDOW_AUTOSIZE)
        while True:
            ret_val, img = cap.read()
            #cv2.rectangle(img,(0,0),(500,1080),(0,0,0),-1)
            #filled polygon
            rectangle = np.array([[0,0],[320,0],[1200,1000],[0,1980]])
            cv2.fillConvexPoly(img, rectangle, (0,0,0))

            # Cell 1
            #hollow polygon
            pts = np.array([[475, 158], [509, 195], [743, 191], [680, 150]], np.int32)
            cv2.polylines(img, [pts], True, (0, 255, 255), 3)
            #text
            font = cv2.FONT_HERSHEY_SIMPLEX
            cv2.putText(img, 'Cell 1', (480, 168), font, 0.6, (0,0,0), 2, cv2.LINE_AA)

            # Cell 2
            #hollow polygon
            pts = np.array([[509, 195], [553, 248], [824, 247], [743, 191]], np.int32)
            cv2.polylines(img, [pts], True, (0, 255, 255), 3)
            #text
            font = cv2.FONT_HERSHEY_SIMPLEX
            cv2.putText(img, 'Cell 2', (515, 210), font, 0.6, (0,0,0), 2, cv2.LINE_AA)


            cv2.imshow('demo',img)
            if cv2.waitKey(10) & 0xFF == ord('q'):
                break

else:
        print ("camera open failed")

cap.release()
cv2.destroyAllWindows()

