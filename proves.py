# -*- coding: utf-8 -*-
import webbrowser
from tkinter import *

def si():
    root.destroy()


def no():
    root.destroy()

# Configuración de la raíz
root = Tk()
root.title("WEB")

label = Label(root, text="Vols iniciar la pàgina?")
label.grid(row=0, column=1, sticky=W, padx=5, pady=5)

label4 = Label(root, text="")

label5 = Button(root, text="Si", command=si)
label5.grid(row=3, column=0, sticky=W, padx=5, pady=5)

label6 = Button(root, text="No", command=no)
label6.grid(row=3, column=2, sticky=W, padx=5, pady=5)

# Finalmente bucle de la aplicación
root.mainloop()

