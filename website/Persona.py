from tkinter import *
from noms import persona

alumne = "".join(persona)

def resta():
    root.destroy()


root = Tk()
root.title("Nom")
root.config(bd=15)

# imagen = PhotoImage(file="static/images/image.png")
Label(root).pack(side=LEFT)

frame = Frame(root).pack(side=RIGHT)
Label(frame, text="\n" + alumne + " s'afegirà a la llista d'alumnes").pack(anchor=W)

Button(root, text="OK", command=resta).pack(side=BOTTOM)


root.mainloop()