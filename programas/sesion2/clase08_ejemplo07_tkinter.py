import tkinter as tk
import threading as th
import time

def aumentar():
    contador = 0
    while True:
        time.sleep(1)
        etiqueta2.set(contador)
        contador = contador + 1
    

def cambio(valor):
    etiqueta1.set(valor)
    #intentar que los cambios no sean tan bruscos

w = tk.Tk()
w.title("Demo")

etiqueta1 =tk.StringVar()
etiqueta1.set(0)
etiqueta2 =tk.StringVar()
etiqueta2.set(0)

hilo =th.Thread(target =aumentar)
hilo.start()


fm= tk.Frame(w)
fm.grid(row=0, column=0)
#Definimos el slider
sl= tk.Scale(fm, from_=0, to=20, orient=tk.HORIZONTAL, length=200, command=cambio)
sl.grid(row=1, column=0)

lb1= tk.Label(fm, textvariable=etiqueta1, height=2)
lb1.grid(row=2, column=0)

lb2= tk.Label(fm, textvariable=etiqueta2, height=2)
lb2.grid(row=3, column=0)

w.mainloop()
