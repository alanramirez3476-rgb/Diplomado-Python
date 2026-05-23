from tkinter import END, ttk
import tkinter as tk

ventana = tk.Tk()
ventana.config(width=200, height=300)
ventana.title("Contador de edad")
ttk.Label(ventana, text="Ingresa la edad").place(x=20,y=30)
ttk.Label(ventana, text="Resultado").place(x=20,y=90)

txEdad = ttk.Entry(ventana)
txEdad.place(x=20,y=60)

txResultado = tk.Entry(ventana,width=25,state="readonly")
txResultado.place(x=20,y=120)


def Rangodeedad():
    Edad = 0
    Edad = int(txEdad.get())
    txResultado.config(state="normal")

    if Edad < 18:
        Resultado = "Menor de edad"
    elif Edad < 59:
        Resultado = "Adulto"
    elif Edad < 125:
        Resultado = "Adulto mayor"
    else:
        Resultado = "Edad no valida"

    txResultado.delete(0,END)
    txResultado.insert(0,str(Resultado))
    txResultado.config(state="readonly")
    txEdad.focus()

def Limpiar():
    txResultado.config(state="normal")
    txEdad.delete(0,END)
    txResultado.delete(0,END)
    txResultado.config(state="readonly")
btLimpiar=ttk.Button(ventana,width=10, text = "Limpiar", command= Limpiar) 
btLimpiar.place (x=100, y =150)

btCalcular=ttk.Button(ventana,width=10, text = "Calcular", command= Rangodeedad) 
btCalcular.place (x=20, y =150) 

ventana.mainloop()

