import cv2

def generate_dataset(img, id, img_id):
    cv2.imwrite("data/user." + str(id) + "." + str(img_id) + ".jpg", img)


def draw_boundary(img, classifier, scaleFactor, minNeighbour, color, text):
    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    features = classifier.detectMultiScale(gray_img, scaleFactor, minNeighbour)
    coords = []
    for (x, y, w, h) in features:
        cv2.rectangle(img, (x, y), (x+w, y+h), color, 2)
        cv2.putText(img, text, (x, y-4), cv2.FONT_HERSHEY_SIMPLEX, 0.0, color, 1, cv2.LINE_AA)
        coords = [x, y, w, h]

    return coords

def detect(img, faceCascade, eyesCascade):
    color = {"blue":(255,0,0), "red":(0,0,255), "green": (0,255,0), "white":(255,255,255)}
    coords = draw_boundary(img, faceCascade, 1.1, 10, color['blue'], "Face")

    if len(coords) == 4 :
        roi_img = img[coords[0]:coords[0] + coords [2], coords[1]:coords[1] + coords[3]]
        user_id = 1
        generate_dataset(roi_img, user_id, img_id)


        #roi_img = img[coords[0]:coords[0] + coords [2], coords[1]:coords[1] + coords[3]]
        #coords = draw_boundary(roi_img, eyesCascade, 1.1, 14, color['red'], "Eyes")
        #coords = draw_boundary(roi_img, noseCascade, 1.1, 5, color['green'], "Nose")
        #coords = draw_boundary(roi_img, mouthCascade, 1.1, 20, color['red'], "Mouth")
    return img

faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
eyesCascade = cv2.CascadeClassifier("haarcascade_eye.xml")

vid_cap = cv2.VideoCapture(0)

img_id = 0

while True :
    ret, img = vid_cap.read()
    img = detect(img, faceCascade, eyesCascade)
    cv2.imshow("face detection", img)
    img_id += 1


    if cv2.waitKey(0) & 0xFF == ord('q'):
        break

vid_cap.release()
cv2.destroyAllWindows()