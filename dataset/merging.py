import cv2
import multiprocessing


def camera1():
    global cap1
    cap1 = cv2.VideoCapture(0)
    while True:
        _, frame1 = cap1.read()
        cv2.imshow('frame1', frame1)

        k = cv2.waitKey(5)
        if k == 27:
            break
    cap1.release()


def camera2():
    global cap2
    cap2 = cv2.VideoCapture(0)
    while True:
        _, frame2 = cap2.read()
        cv2.imshow('frame2', frame2)

        k = cv2.waitKey(5)
        if k == 27:
            break
    cap2.release()


def cap_images():
    _, img1 = cap1.read()
    _, img2 = cap2.read()
    cv2.imwrite("Image1.png", img1)
    cv2.imwrite("Image2.png", img2)


if __name__ == '__main__':
    p1 = multiprocessing.Process(target=camera1)
    p1.start()
    p2 = multiprocessing.Process(target=camera2)
    p2.start()

cap1.release()
cap2.release()
cv2.destroyAllWindows()