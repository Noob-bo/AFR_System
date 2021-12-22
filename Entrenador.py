import cv2
import os
import numpy as np
from datetime import date
import shutil
import errno

dataPath = 'C:/Users/PolRuizTorras/PycharmProjects/TDR/website/static/Persones'
peopleList = os.listdir(dataPath)

data = date.today()

existents = os.listdir('C:/Users/PolRuizTorras/PycharmProjects/TDR/website/modelsFisherFace_persones')
arxius = "".join(existents)
print(arxius)

labels = []
faceData = []
label = 0

for nameDir in peopleList:
    personPath = dataPath + '/' + nameDir

    for fileName in os.listdir(personPath):
        labels.append(label)
        faceData.append(cv2.imread(personPath + '/' + fileName, 0))
        image = cv2.imread(personPath + '/' + fileName, 0)
        # cv2.imshow('image', image)
        cv2.waitKey(10)
    label += 1

Fisherface = 'modelFisherFace_alumnes_' + str(data) + '.xml'

face_recognizer = cv2.face.FisherFaceRecognizer_create()

face_recognizer.train(faceData, np.array(labels))

face_recognizer.write(Fisherface)

try:
    shutil.move(Fisherface, 'C:/Users/PolRuizTorras/PycharmProjects/TDR/website/modelsFisherFace_persones')
except OSError as e:
    if e.errno != errno.EEXIST:
        raise