import cv2
import numpy as np

source = "rtsp://192.168.1.112:554/ch1/main/av_stream"
cap = cv2.VideoCapture(source)

if cap.isOpened():
        cv2.namedWindow("demo", cv2.WINDOW_AUTOSIZE)
        while True:
            ret_val, img = cap.read()
            #cv2.rectangle(img,(0,0),(500,1080),(0,0,0),-1)
            rectangle = np.array([[0,0],[320,0],[1200,1000],[0,1980]])
            cv2.fillConvexPoly(img, rectangle, (0,0,0))
            cv2.imshow('demo',img)
            if cv2.waitKey(10) & 0xFF == ord('q'):
                break

else:
        print ("camera open failed")

cap.release()
cv2.destroyAllWindows()

