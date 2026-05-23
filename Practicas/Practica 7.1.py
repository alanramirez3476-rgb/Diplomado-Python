
from tkinter import END,messagebox,ttk
import tkinter as tk


ventana=tk.Tk()
#venta. config(width= 220,heigth=260)
ventana.geometry ("229x280")
ventana.title("practica 7")

ttk.Label(ventana, text="Ingresa valor 1").place(x=20,y=30)
ttk.Label(ventana, text="Ingresa valor 2").place(x=20,y=80)
ttk.Label(ventana, text="Resultado").place(x=20,y=180)
ttk.Label(ventana,text="Seleciona la operacion").place(x=20,y=130)

cbCategorias = ttk.Combobox(ventana,state="readonly",values=["Sumar","Restar","Multiplicar","Dividir"])
cbCategorias.place(x=20,y=200)

txIngresavalor1 = ttk.Entry(ventana)
txIngresavalor1.place(x=20,y=50)

txIngresavalor2 = ttk.Entry(ventana)
txIngresavalor2.place(x=20,y=100)

txResultado = ttk.Entry(ventana)
txResultado.place(x=20,y=150)

def Limpiar():
    pass

def Resultado():
    pass

btLimpiar = ttk.Button(ventana,width=10, text = "Limpiar", command= Limpiar)
btLimpiar.place(x= 100, y=240)

btResultado = ttk.Button(ventana,width=10, text = "Resultado", command= Resultado)
btResultado.place(x=20,y=240)


ventana.mainloop()


