# Ejercicio 8 Escribir un script python con la libreria tkinder para colocar:
#  1.-Una caja de texto 
# 2.-Un boton para imprimir un mensaje en la caja de texto 
# 3.-Un boton para borrar la caja de texto 4.-Un boton para salir del script

import tkinter as tk
from tkinter import *

def mostrar():
    txtC1.set("Hola mundo")

def borrar():
    txtC1.set("")

def salir():
    wv.destroy()

# Programa principal 

# Creamos las ventana
wv = tk.Tk()
wv.config(bd=15)
# Modificamos el tamaño de la ventana
wv.geometry("250x100")

wv.title("Ejercicio 7")

# creamos los campos de texto
txtC1 = StringVar()

Entry(wv, justify="left",textvariable=txtC1,state="disabled").pack()

#Creamos los botones
be = Button(wv, text="Mostrar", command=mostrar).pack(side="left")
bb = Button(wv, text="Borrar", command=borrar).pack(side="left")
bs = Button(wv, text="Salir", command=salir).pack(side="left")


# Ciclo de espera de eventos
wv.mainloop()