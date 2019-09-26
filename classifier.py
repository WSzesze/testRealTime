import numpy as np
from PIL import Image
# os module for reading training data directories and path
import os
import cv2

data_dir = "C:\\Users\\Sze2\\PycharmProjects\\testRealTime\\pics"

# Method to train custom classifier to recognize face
def train_classifier(data_dir):
    #Read all the images in custom data-set
    path = [os.path.join(data_dir, f) for f in os.listdir(data_dir)]
    faces = []
    ids = []

    # Store images in a numpy format and ids of the user on the same indes in imageNp and id L=lists
    for image in path:
        img = Image.open(image).convert('L')
        imageNp = np.array(img, 'uint8')
        id = int(os.path.split(image)[1].split(".")[1])

        faces.append(imageNp)
        ids.append(id)

    ids = np.array(ids)

    # Train and save classifier
    clf = cv2.face_LBPHFaceRecognizer.create()
    clf.train(faces, ids)
    clf.write("classifier.yml")

train_classifier("data")