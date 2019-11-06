import cv2
import sys


def cell_1():
    cap = cv2.VideoCapture("rtsp://192.168.1.106:554/ch1/main/av_stream")

    if cap.isOpened():
        cv2.namedWindow("demo", cv2.WINDOW_AUTOSIZE)
        while True:
            ret_val, frame1 = cap.read()
            image1 = cv2.imread('dataset/cover1.jpg')
            alpha = 0.6
            added_image1 = cv2.addWeighted(frame1, alpha, image1, 1 - alpha, 0)
            img1 = cv2.resize(added_image1, (0, 0), fx=0.69, fy=0.65)

            cv2.imshow('demo', img1)
            k = cv2.waitKey(10)
            if k & 0xFF == ord('q'):
                 break

    else:
        print("camera open failed")

    cap.release()
    cv2.destroyAllWindows()

def cell_2():
    cap = cv2.VideoCapture("rtsp://192.168.1.106:554/ch1/main/av_stream")

    if cap.isOpened():
        cv2.namedWindow("demo", cv2.WINDOW_AUTOSIZE)
        while True:
            ret_val, frame2 = cap.read()
            image2 = cv2.imread('dataset/cover2.jpg')
            alpha = 0.6
            added_image2 = cv2.addWeighted(frame2, alpha, image2, 1 - alpha, 0)
            img2 = cv2.resize(added_image2, (0, 0), fx=0.69, fy=0.65)

            cv2.imshow('demo', img2)
            k = cv2.waitKey(10)
            if k & 0xFF == ord('q'):
                break

    else:
        print("camera open failed")

    cap.release()
    cv2.destroyAllWindows()

def cell_3():
    cap = cv2.VideoCapture("rtsp://192.168.1.106:554/ch1/main/av_stream")

    if cap.isOpened():
        cv2.namedWindow("demo", cv2.WINDOW_AUTOSIZE)
        while True:
            ret_val, frame3 = cap.read()
            image3 = cv2.imread('dataset/cover3.jpg')
            alpha = 0.6
            added_image3 = cv2.addWeighted(frame3, alpha, image3, 1 - alpha, 0)
            img3 = cv2.resize(added_image3, (0, 0), fx=0.69, fy=0.65)

            cv2.imshow('demo', img3)
            k = cv2.waitKey(10)
            if k & 0xFF == ord('q'):
                break

    else:
        print("camera open failed")

    cap.release()
    cv2.destroyAllWindows()

def cell_4():
    cap = cv2.VideoCapture("rtsp://192.168.1.109:554/ch1/main/av_stream")

    if cap.isOpened():
        cv2.namedWindow("demo", cv2.WINDOW_AUTOSIZE)
        while True:
            ret_val, frame4 = cap.read()
            image4 = cv2.imread('dataset/cover4.jpg')
            alpha = 0.6
            added_img4 = cv2.addWeighted(frame4, alpha, image4, 1 - alpha, 0)
            img4 = cv2.resize(added_img4, (0, 0), fx=0.69, fy=0.65)

            cv2.imshow('demo', img4)
            k = cv2.waitKey(10)
            if k & 0xFF == ord('q'):
                 break

    else:
        print("camera open failed")

    cap.release()
    cv2.destroyAllWindows()

def cell_5():
    cap = cv2.VideoCapture("rtsp://192.168.1.112:554/ch1/main/av_stream")

    if cap.isOpened():
        cv2.namedWindow("demo", cv2.WINDOW_AUTOSIZE)
        while True:
            ret_val, frame5 = cap.read()
            image5 = cv2.imread('dataset/cover5.jpg')
            alpha = 0.6
            added_img5 = cv2.addWeighted(frame5, alpha, image5, 1 - alpha, 0)
            img5 = cv2.resize(added_img5, (0, 0), fx=0.69, fy=0.65)

            cv2.imshow('demo', img5)
            k = cv2.waitKey(10)
            if k & 0xFF == ord('q'):
                break

    else:
        print("camera open failed")

    cap.release()
    cv2.destroyAllWindows()

def cell_6():
    cap = cv2.VideoCapture("rtsp://192.168.1.102:554/ch1/main/av_stream")

    if cap.isOpened():
        cv2.namedWindow("demo", cv2.WINDOW_AUTOSIZE)
        while True:
            ret_val, frame6 = cap.read()
            image6 = cv2.imread('dataset/cover6.jpg')
            alpha = 0.6
            added_img6 = cv2.addWeighted(frame6, alpha, image6, 1 - alpha, 0)
            img6 = cv2.resize(added_img6, (0, 0), fx=0.69, fy=0.65)

            cv2.imshow('demo', img6)
            k = cv2.waitKey(10)
            if k & 0xFF == ord('q'):
                break

    else:
        print("camera open failed")

    cap.release()
    cv2.destroyAllWindows()

def cell_7():
    cap = cv2.VideoCapture("rtsp://192.168.1.102:554/ch1/main/av_stream")

    if cap.isOpened():
        cv2.namedWindow("demo", cv2.WINDOW_AUTOSIZE)
        while True:
            ret_val, frame7 = cap.read()
            image7 = cv2.imread('dataset/cover7.jpg')
            alpha = 0.6
            added_img7 = cv2.addWeighted(frame7, alpha, image7, 1 - alpha, 0)
            img7 = cv2.resize(added_img7, (0, 0), fx=0.69, fy=0.65)

            cv2.imshow('demo', img7)
            k = cv2.waitKey(10)
            if k & 0xFF == ord('q'):
                break

    else:
        print("camera open failed")

    cap.release()
    cv2.destroyAllWindows()

def cell_8():
    cap = cv2.VideoCapture("rtsp://192.168.1.115:554/ch1/main/av_stream")

    if cap.isOpened():
        cv2.namedWindow("demo", cv2.WINDOW_AUTOSIZE)
        while True:
            ret_val, frame8 = cap.read()
            image8 = cv2.imread('dataset/cover8.jpg')
            alpha = 0.6
            added_img8 = cv2.addWeighted(frame8, alpha, image8, 1 - alpha, 0)
            img8 = cv2.resize(added_img8, (0, 0), fx=0.69, fy=0.65)

            cv2.imshow('demo', img8)
            k = cv2.waitKey(10)
            if k & 0xFF == ord('q'):
                break

    else:
        print("camera open failed")

    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":

    while True:
        option = input("Input : ")
        switch = {
            "1": cell_1,
            "2": cell_2,
            "3": cell_3,
            "4": cell_4,
            "5": cell_5,
            "6": cell_6,
            "7": cell_7,
            "8": cell_8,
            "e": sys.exit
        }
        switch[option]()

