from flask import Response
from flask import Flask
from flask import render_template
import threading
import argparse
import cv2
import sys
from imutils.video import VideoStream


source = "rtsp://192.168.1.115:554/ch1/main/av_stream"
outputFrame = None
lock = threading.Lock()
app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


def cell_8():
    cap5 = VideoStream(source).start()

    if cap5.isOpened():
        cv2.namedWindow("demo", cv2.WINDOW_AUTOSIZE)
        while True:
            success, frame8 = cap5.read()
            image8 = cv2.imread('cover8.jpg')
            alpha = 0.4
            added_img8 = cv2.addWeighted(frame8, alpha, image8, 1 - alpha, 0)
            img8 = cv2.resize(added_img8, (0, 0), fx=0.69, fy=0.65)

            font = cv2.FONT_HERSHEY_SIMPLEX
            cv2.putText(img8, 'Cell 8', (350, 150), font, 5.0, (0, 0, 0), 5, cv2.LINE_AA)

            cv2.imshow('demo', img8)
            if not success:
                break
            else:
                ret, buffer = cv2.imencode('.jpg', frame8)
                frame = buffer.tobytes()
                yield (b'--frame\r\n'
                       b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')
            k = cv2.waitKey(10)
            if k & 0xFF == ord('q'):
                break

    else:
        print("camera open failed")

    cap5.release()
    cv2.destroyAllWindows()

if __name__ == '__main__':

    while True:
        option = input("Input : ")

        app.run(host="192.168.0.60", port="5000", debug=True,
                threaded=True, use_reloader=False)

        switch = {

            "8": cell_8,
            "e": sys.exit
        }
        switch[option]()

