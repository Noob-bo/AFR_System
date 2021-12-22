from tkinter import *

num = 0

def ok():
    index = 1
    r.append(un.get()) # tipo llista
    Strr = " ".join(r) # tipo text
    llista.append(Strr)
    numero = int(Strr) # num
    while index < numero:
        llista.append(index)
        index += 1
    root.destroy()

def no():
    un.set("")
    r.clear()

# Configuración de la raíz
root = Tk()
root.title("Afegir")

un = StringVar()


r = []
llista = []


label = Label(root, text="Numero de persones a afegir: ")
label.grid(row=0, column=1, sticky=W, padx=5, pady=5)

entry = Entry(root, textvariable=un)
entry.grid(row=1, column=1, padx=5, pady=5)

label4 = Label(root, text="")

label5 = Button(root, text="Ok", command=ok)
label5.grid(row=3, column=0, sticky=W, padx=5, pady=5)

label6 = Button(root, text="No", command=no)
label6.grid(row=3, column=2, sticky=W, padx=5, pady=5)

# Finalmente bucle de la aplicación
root.mainloop()

patata = llista

nums = 1

for i in patata:
    exec(open("projecte_individual.py").read())
    nums += 1
