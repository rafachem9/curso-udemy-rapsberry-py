import tkinter as tk
import time

def cambio(valor):
    etiqueta.set(valor)
    #intentar que los cambios no sean tan bruscos
    time.sleep(0.2)

w = tk.Tk()
w.title("Demo")

etiqueta =tk.StringVar()
etiqueta.set(0)

fm= tk.Frame(w)
fm.grid(row=0, column=0)
#Definimos el slider
sl= tk.Scale(fm, from_=0, to=20, orient=tk.HORIZONTAL, length=200, command=cambio)
sl.grid(row=1, column=0)

lb= tk.Label(fm, textvariable=etiqueta, height=2)
lb.grid(row=2, column=0)

w.mainloop()

