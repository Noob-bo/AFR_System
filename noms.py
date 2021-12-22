from tkinter import *

num = 0


def sumar():
    r.append(un.get())
    r.append(dos.get())
    r.append(tres.get())
    Strr = " ".join(r)
    persona.append(Strr)
    r.clear()
    root.destroy()

def resta():
    un.set("")
    dos.set("")
    tres.set("")
    r.clear()


# Configuración de la raíz
root = Tk()
root.title("Nom")

un = StringVar()
dos = StringVar()
tres = StringVar()


r = []
persona = []


label = Label(root, text="Nom")
label.grid(row=0, column=0, sticky=W, padx=5, pady=5)

entry = Entry(root, textvariable=un)
entry.grid(row=0, column=1, padx=5, pady=5)

label2 = Label(root, text="cognom")
label2.grid(row=1, column=0, sticky=W, padx=5, pady=5)

entry2 = Entry(root, textvariable=dos)
entry2.grid(row=1, column=1, padx=5, pady=5)

label3 = Label(root, text="2n cognom")
label3.grid(row=2, column=0, sticky=W, padx=5, pady=5)

entry3 = Entry(root, textvariable=tres)
entry3.grid(row=2, column=1, padx=5, pady=5)

label4 = Label(root, text="")

label5 = Button(root, text="Ok", command=sumar)
label5.grid(row=3, column=0, sticky=W, padx=5, pady=5)

label6 = Button(root, text="No", command=resta)
label6.grid(row=3, column=1, sticky=W, padx=5, pady=5)

# Finalmente bucle de la aplicación
root.mainloop()

nom = ' '.join([str(item) for item in persona])

