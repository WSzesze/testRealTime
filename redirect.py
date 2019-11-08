from pyimagesearch.motion_detection import SingleMotionDetector
import argparse
import datetime
import threading
import cv2
import imutils
from imutils.video import VideoStream
from flask import Response, request
from flask import Flask
from flask import render_template
from flask_wtf import form
import time
import cv2
import numpy as np
import WebCell1
import WebCell2
import WebCell3
import WebCell4
import WebCell5
import WebCell6
import WebCell7

outputFrame = None
lock = threading.Lock()

app = Flask(__name__)

#
# @app.route("/")
# def base():
#     # return the rendered template
#     return render_template("base.html")


@app.route('/foo', methods=['POST'])
def foo():
    callable(WebCell1)
    return render_template("ïndex.html")


if __name__ == '__main__':
    # construct the argument parser and parse command line arguments
    ap = argparse.ArgumentParser()
    ap.add_argument("-i", "--ip", type=str, required=True,
                    help="ip address of the device")
    ap.add_argument("-o", "--port", type=int, required=True,
                    help="ephemeral port number of the server (1024 to 65535)")
    ap.add_argument("-f", "--frame-count", type=int, default=32,
                    help="# of frames used to construct the background model")
    args = vars(ap.parse_args())

    # start the flask app
    app.run(host=args["ip"], port=args["port"], debug=True,
            threaded=True, use_reloader=False)
