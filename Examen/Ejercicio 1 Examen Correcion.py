
from tkinter import END, ttk
import tkinter as tk

Ventana = tk.Tk()
Ventana.geometry("450x350")
Ventana.title("Convertidor de Grados")

ttk.Label(Ventana, text="Elige una opción de conversión").place(x=15, y=15)

selector = tk.IntVar()

ttk.Label(Ventana, text="Valores").place(x=260, y=20)
ttk.Label(Ventana, text="Resultado").place(x=260, y=190)

Etiqueta1 = ttk.Label(Ventana, text="")
Etiqueta2 = ttk.Label(Ventana, text="")
Etiqueta1.place(x=250, y=40)
Etiqueta2.place(x=250, y=20)

Entrada1 = tk.Entry(Ventana, width=10, state="normal")
Entrada1.place(x=320, y=40)
Entrada2 = tk.Entry(Ventana, width=10, state="readonly")
Entrada2.place(x=320, y=230)

# Radios para elegir conversión
radio1 = tk.Radiobutton(Ventana, text="Celsius - Kelvin", variable=selector, value=1,
                        command=lambda: selector_Etiquetas(Etiqueta1, Etiqueta2))
radio1.place(x=20, y=50)
radio2 = tk.Radiobutton(Ventana, text="Celsius - Fahrenheit", variable=selector, value=2,
                        command=lambda: selector_Etiquetas(Etiqueta1, Etiqueta2))
radio2.place(x=20, y=80)
radio3 = tk.Radiobutton(Ventana, text="Kelvin - Celsius", variable=selector, value=3,
                        command=lambda: selector_Etiquetas(Etiqueta1, Etiqueta2))
radio3.place(x=20, y=110)
radio4 = tk.Radiobutton(Ventana, text="Fahrenheit - Celsius", variable=selector, value=4,
                        command=lambda: selector_Etiquetas(Etiqueta1, Etiqueta2))
radio4.place(x=20, y=140)

def selector_Etiquetas(Etiqueta1, Etiqueta2):
    opcion = selector.get()
    if opcion == 1:
        Etiqueta1.config(text="Celsius")
        Etiqueta2.config(text="Kelvin")
    elif opcion == 2:
        Etiqueta1.config(text="Celsius")
        Etiqueta2.config(text="Fahrenheit")
    elif opcion == 3:
        Etiqueta1.config(text="Kelvin")
        Etiqueta2.config(text="Celsius")
    elif opcion == 4:
        Etiqueta1.config(text="Fahrenheit")
        Etiqueta2.config(text="Celsius")

def Calcular():
    opcion = selector.get()
    try:
        Valor = float(Entrada1.get())
    except ValueError:
        Valor = 0.0

    resultado = None
    if opcion == 1:  # Celsius-Kelvin
        resultado = Valor + 273.15
    elif opcion == 2:  # Celsius-Fahrenheit
        resultado = (Valor * 9/5) + 32
    elif opcion == 3:  # Kelvin-Celsius
        resultado = Valor - 273.15
    elif opcion == 4:  # Fahrenheit-Celsius
        resultado = (Valor - 32) * 5/9

    if resultado is not None:
        Entrada2.config(state="normal")
        Entrada2.delete(0, END)
        Entrada2.insert(0, round(resultado, 2))
        Entrada2.config(state="readonly")

def Limpiar():
    Entrada1.delete(0, END)
    Entrada2.config(state="normal")
    Entrada2.delete(0, END)
    Entrada2.config(state="readonly")

btCalcular = ttk.Button(Ventana, width=10, text="Calcular", command=Calcular)
btCalcular.place(x=250, y=150)

btLimpiar = ttk.Button(Ventana, width=10, text="Limpiar", command=Limpiar)
btLimpiar.place(x=340, y=150)

Ventana.mainloop()