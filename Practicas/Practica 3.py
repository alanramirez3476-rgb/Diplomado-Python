#importatr las librerias para generar ventanas y sus objetos 
from tkinter import END, messagebox, ttk
import tkinter as tk 

#crear la ventana
ventana = tk.Tk() #Esta linea crea la ventana
ventana.config(width=235, height=200) #Configura el tamaño de la ventana
ventana.title("practica 3") #Configura el titulo de la ventana


#crea una etiqueta para pedir el precio al usuario
ttk.Label(ventana, text="ingresa el precio").place(x=20,y=20)

#Entry nos sirve para crear cajas 
txPrecio = ttk.Entry(ventana)
txPrecio.place(x=20,y=40)

txResultado = tk.Entry(ventana)
txResultado.place(x=20, y=80)

def aumentaPorcentaje():
    Precio = 0.0
    Resultado = 0.0 
    Precio = float(txPrecio.get())
    Resultado = Precio * 1.16 #Aumenta el iva o al 16%

    txResultado.delete(0,END) #Limpia el resultado anterior
    txResultado.insert(0,f"{Resultado:.2f}") #Muestra el resultado en la caja de texto

btcalcular=ttk.Button(ventana,width=10, text = "calcular", command= aumentaPorcentaje) 
btcalcular.place (x=20, y =110) 
ventana.mainloop() #Esta linea hace que la ventana se mantenga abierta