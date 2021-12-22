import cv2
import os
import imutils
import glob
import errno

dataPath = './static/Persones'
imagePaths = os.listdir(dataPath)
countImage = len(os.listdir(dataPath))

Fisher = os.listdir('modelsFisherFace_persones')
modelFisher = "".join(Fisher)

face_recognizer = cv2.face.FisherFaceRecognizer_create()
face_recognizer.read("./modelsFisherFace_persones/{}".format(modelFisher))

cap = cv2.VideoCapture(1)

faceClassif = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

contador = 0
persones = len(glob.glob('./static/Persones'))
llista2 = []


while True:
    ret, frame = cap.read()
    frame = imutils.resize(frame, width=600)
    if ret == False: break
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    auxFrame = gray.copy()

    faces = faceClassif.detectMultiScale(gray, 1.3, 5)

    for (x, y, w, h) in faces:
        rostro = auxFrame[y:y+h, x:x+w]
        rostro = cv2.resize(rostro, (150, 150), interpolation = cv2.INTER_CUBIC)
        result = face_recognizer.predict(rostro)

        # cv2.putText(frame, '{}'.format(result), (x, y-5), 1, 1.3, (255, 155, 0), 1, cv2.LINE_AA)
        # cv2.rectangle(frame, (x, y), (x + w, y + h), (159, 231, 249), 2)

        # detecta una cara amb un grau de confiança inferior a 700
        if result[1] < 700:
            # si la persona que detecta és igual a la persona que indica el contador...
            if imagePaths[result[0]] == imagePaths[contador]:
                # no deixa que a la llista s'afegeixin més numeros dels que toca
                if llista2.count(contador) == 2:
                    break
                llista2.append(contador)
                patata = contador + 1
                # ... crea un arxiu css
                try:
                    f = open('C:/Users/PolRuizTorras/PycharmProjects/TDR/website/static/batxcss/batx_' + str(contador) + '.css', 'w')

                    # missatge a escriure
                    mensaje = '''
                    #persones''' + str(patata) + '''{
                    background: lightgreen;
                    }'''

                    f.write(mensaje)
                    f.close()

                except OSError as e:
                    if e.errno != errno.EEXIST:
                        raise


                if contador != persones:
                    if contador >= persones:
                        contador = 0
                    else:
                        contador += 1
            else:
                if contador >= persones:
                    contador = 0
                else:
                    contador += 1

        # if result[1] < 6000:
            # cv2.putText(frame, '{}'.format(imagePaths[result[0]]), (x, y - 10), 2, 0.6, (241, 238, 30), 1, cv2.LINE_AA)
            # cv2.rectangle(frame, (x, y), (x + w, y + h), (159, 231, 249), 2)
        # else:
            # cv2.putText(frame, '', (x, y-20), 2, 0.8, (0, 0, 255), 1, cv2.LINE_AA)
            # cv2.rectangle(frame, (x, y), (x+w, y+h), (53, 67, 203), 2)
    # mostra la camera
    cv2.imshow('frame', frame)
    # es para amb l'Esc
    k = cv2.waitKey(1)
    if k == 27:
        break