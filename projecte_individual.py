
import cv2
# pip install opencv-python
import os
# pip install os-win
import errno
import imutils
# pip install imutils
import glob
import shutil
# pip install pytest-shutil
import random
# pip install random
from persones_a_afegir import nums
from noms import *

exec(open("noms.py").read())

alumne = "".join(nom)
alumne = alumne.upper()
persona = str(nums) + "_" + alumne

dataPath = 'C:/Users/PolRuizTorras/PycharmProjects/TDR/website/static/Persones'
personPath = dataPath + '/' + persona
# perfilPath = dataPath + '/' + alumne + 'perfil'



# crea la carpeta de la persona
try:
    os.makedirs(persona)
    # os.makedirs(alumne + 'perfil')
except OSError as e:
    if e.errno != errno.EEXIST:
        raise

# missatge  X S'AFEGIRÀ A LA LLISTA D'ALUMNES
import Persona

cap = cv2.VideoCapture(1)

# mou la carpeta de la persona que s'ha creat abans i la mou al directori de Persones
shutil.move(persona, dataPath)
# shutil.move(alumne + 'perfil', dataPath)

faceClassif = cv2.CascadeClassifier(cv2.data.haarcascades+'haarcascade_frontalface_default.xml')
count = 0   # porta la conta del numero d'imatges que es fan
Numero = 0   # conta el numero de imatges que hi ha dins de la carpeta
lloc = 'C:/Users/PolRuizTorras/PycharmProjects/TDR/website/static/Persones'
lloc_perfil = 'C:/Users/PolRuizTorras/PycharmProjects/TDR/website/static/Persones/'

# hauria de fer una sola foto mentre el numero de fotos fetes sigui 0
'''if count == 0:

    ret, frame = cap.read()

    frame = imutils.resize(frame, width=640)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    auxFrame = frame.copy()
    faces = faceClassif.detectMultiScale(gray)
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
        rostro = auxFrame[y:y+h, x:x+w]
        rostro = cv2.resize(rostro, (150, 150), interpolation=cv2.INTER_CUBIC)
        cv2.imwrite(perfilPath + '/' + alumne + '.jpg', rostro)

    k = cv2.waitKey(1)
'''

# mentre el numero d'imatges que hi ha dins de la carpeta és inferior a 150 s'aniran fent fotos
while Numero < 40:
    Numero = len(glob.glob("C:/Users/PolRuizTorras/PycharmProjects/TDR/website/static/Persones/" + persona + "/*.jpg"))

    ret, frame = cap.read()

    frame = imutils.resize(frame, width=640)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    auxFrame = frame.copy()
    faces = faceClassif.detectMultiScale(gray)
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
        rostro = auxFrame[y:y+h, x:x+w]
        rostro = cv2.resize(rostro, (150, 150), interpolation=cv2.INTER_CUBIC)
        cv2.imwrite(personPath + '/rostro_{}.jpg'.format(count), rostro)
        count = count + 1

    k = cv2.waitKey(1)
    # si el numero de fotos que hi ha a la carpeta ja és de 150 llavors pararà el programa
    if Numero > 40:
        lloc = os.path.realpath(lloc)
        os.startfile(lloc)
        break
cap.release()

# crea un archiu JavaScript amb l'informacio de la persona que s'acaba d'afegir
try:

    archiuJS = len(glob.glob('C:/Users/PolRuizTorras/PycharmProjects/TDR/website/static/batxjs/*.js'))

    numeros = ['Uno',
'Dos',
'Tres',
'Cuatro',
'Cinco',
'Seis',
'Siete',
'Ocho',
'Nueve',
'Diez',
'Once',
'Doce',
'Trece',
'Catorce',
'Quince',
'Dieciséis',
'Diecisiete',
'Dieciocho',
'Diecinueve',
'Veinte',
'Veintiuno',
'Veintidos',
'Veintitres',
'Veinticuatro',
'Veinticinco',
'Veintiseis',
'Veintisiete',
'Veintiocho',
'Veintinueve',
'Treinta',
'Treintauno',
'Treintados',
'Treintatres',
'Treintacuatro',
'Treintacinco',
'Treintaseis',
'Treintasiete',
'Treintaocho',
'Treintanueve',
'Cuarenta',
'Cuarentauno',
'Cuarentados',
'Cuarentatres',
'Cuarentacuatro',
'Cuarentacinco',
'Cuarentaseis',
'Cuarentasiete',
'Cuarentaocho',
'Cuarentanueve',
'Cincuenta',
'Cincuentauno',
'Cincuentados',
'Cincuentatres',
'Cincuentacuatro',
'Cincuentacinco',
'Cincuentaseis',
'Cincuentasiete',
'Cincuentaocho',
'Cincuentanueve',
'Sesenta',
'Sesentauno',
'Sesentados',
'Sesentatres',
'Sesentacuatro',
'Sesentacinco',
'Sesentaseis',
'Sesentasiete',
'Sesentaocho',
'Sesentanueve',
'Setenta',
'Setentauno',
'Setentados',
'Setentatres',
'Setentacuatro',
'Setentacinco',
'Setentaseis',
'Setentasiete',
'Setentaocho',
'Setentanueve',
'Ochenta',
'Ochentauno',
'Ochentados',
'Ochentatres',
'Ochentacuatro',
'Ochentacinco',
'Ochentaseis',
'Ochentasiete',
'Ochentaocho',
'Ochentanueve',
'Noventa',
'Noventauno',
'Noventados',
'Noventatres',
'Noventacuatro',
'Noventacinco',
'Noventaseis',
'Noventasiete',
'Noventaocho',
'Noventanueve',
'Cien',
'Cientouno',
'Cientodos',
'Cientotres',
'Cientocuatro',
'Cientocinco',
'Cientoseis',
'Cientosiete',
'Cientoocho',
'Cientonueve',
'Cientodiez',
'Cientoonce',
'Cientodoce',
'Cientotrece',
'Cientocatorce',
'Cientoquince',
'Cientodieciséis',
'Cientodiecisiete',
'Cientodieciocho',
'Cientodiecinueve',
'Cientoveinte',
'Cientoveintiuno',
'Cientoveintidos',
'Cientoveintitres',
'Cientoveinticuatro',
'Cientoveinticinco',
'Cientoveintiseis',
'Cientoveintisiete',
'Cientoveintiocho',
'Cientoveintinueve',
'Cientotreinta',
'Cientotreintauno',
'Cientotreintados',
'Cientotreintatres',
'Cientotreintacuatro',
'Cientotreintacinco',
'Cientotreintaseis',
'Cientotreintasiete',
'Cientotreintaocho',
'Cientotreintanueve',
'Cientocuarenta',
'Cientocuarentauno',
'Cientocuarentados',
'Cientocuarentatres',
'Cientocuarentacuatro',
'Cientocuarentacinco',
'Cientocuarentaseis',
'Cientocuarentasiete',
'Cientocuarentaocho',
'Cientocuarentanueve',
'Cientocincuenta',
'Cientocincuentauno',
'Cientocincuentados',
'Cientocincuentatres',
'Cientocincuentacuatro',
'Cientocincuentacinco',
'Cientocincuentaseis',
'Cientocincuentasiete',
'Cientocincuentaocho',
'Cientocincuentanueve',
'Cientosesenta',
'Cientosesentauno',
'Cientosesentados',
'Cientosesentatres',
'Cientosesentacuatro',
'Cientosesentainco',
'Cientosesentaseis',
'Cientosesentasiete',
'Cientosesentaocho',
'Cientosesentanueve',
'Cientosetenta',
'Cientosetentauno',
'Cientosetentados',
'Cientosetentatres',
'Cientosetentacuatro',
'Cientosetentacinco',
'Cientosetentaseis',
'Cientosetentasiete',
'Cientosetentaocho',
'Cientosetentanueve',
'Cientoochenta',
'Cientoochentauno',
'Cientoochentados',
'Cientoochentatres',
'Cientoochentacuatro',
'Cientoochentacinco',
'Cientoochentaseis',
'Cientoochentasiete',
'Cientoochentaocho',
'Cientoochentanueve',
'Cientonoventa',
'Cientonoventauno',
'Cientonoventados',
'Cientonoventatres',
'Cientonoventacuatro',
'Cientonoventacinco',
'Cientonoventaseis',
'Cientonoventaisete',
'Cientonoventaocho',
'Cientonoventanueve']
    # escull un numero aleratori
    const = random.choice(numeros)
    let = random.choice(numeros)

    f = open('C:/Users/PolRuizTorras/PycharmProjects/TDR/website/static/batxjs/batx' + str(archiuJS) + '.js', 'w')

    # missatge a escriure
    mensaje = '''const ''' + const + ''' = [{
        img: 'static/Persones/''' + persona + '''/rostro_0.jpg',
        desc: ' ''' + alumne + ''' '
    }]

    let ''' + let + ''' = document.querySelector('#persones''' + str(archiuJS) + '''')

    function dinamico(src, desc) {
        let colm = document.createElement("div");
        let img = document.createElement("img");
        img.src = src;
        let a = document.createElement("a");
        a.innerHTML = desc;
        colm.appendChild(img);
        colm.appendChild(a);
        ''' + let + '''.appendChild(colm);
    }

    ''' + const + '''.forEach(({img, desc}) => dinamico(img, desc));'''

    f.write(mensaje)
    f.close()

except OSError as e:
    if e.errno != errno.EEXIST:
        raise

try:

    archiuJS = len(glob.glob('C:/Users/PolRuizTorras/PycharmProjects/TDR/website/static/batxjs/*.js'))


    patata = nums - 1

    f = open('C:/Users/PolRuizTorras/PycharmProjects/TDR/website/static/batxcss/batx_' + str(patata) + '.css', 'w')

    # missatge a escriure
    mensaje = '''
    #persones''' + str(nums) + '''{
    background: indianred;
    }'''

    f.write(mensaje)
    f.close()

    alumne = None

# en cas d'error l'ignOrarà i es crearà de totes formes
except OSError as e:
    if e.errno != errno.EEXIST:
        raise