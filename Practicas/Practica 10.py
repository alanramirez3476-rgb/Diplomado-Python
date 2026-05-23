import tkinter as tk
from tkinter import ttk, messagebox, END
import math

ventana = tk.Tk()
ventana.config(width=290, height=300)
ventana.title("Practica 10")
textoEtiqueta = "Lado"
textoEtiqueta2 = ""

var1 = tk.IntVar()
var2 = tk.BooleanVar()
var3 = tk.BooleanVar()

ttk.Label(ventana, text="Tipo de Figura").place(x=20, y=20)
ttk.Label(ventana, text="Tipo de Calculo").place(x=20, y=180)
ttk.Label(ventana, text="Valores").place(x=160, y=20)
ttk.Label(ventana, text="Resultados").place(x=160, y=180)
ttk.Label(ventana, text="Area").place(x=160, y=210)
ttk.Label(ventana, text="Perimetro").place(x=160, y=240)

txvalor1 = tk.Entry(ventana, width=10)
txvalor1.place(x=200, y=50)
txvalor2 = tk.Entry(ventana, width=10)
# txvalor2.place(x=200, y=80)
txresul1 = tk.Entry(ventana, width=10, state="readonly")
txresul1.place(x=220, y=210)
txresul2 = tk.Entry(ventana, width=10, state="readonly")
txresul2.place(x=220, y=240)


radio1 = tk.Radiobutton(ventana, text="Cuadrado", variable=var1, value=1, command=lambda: calcular(lbtexto, lbtexto2))
radio1.place(x=20, y=50)
radio2 = tk.Radiobutton(ventana, text="Triangulo", variable=var1, value=2, command=lambda: calcular(lbtexto, lbtexto2))
radio2.place(x=20, y=80)
radio3 = tk.Radiobutton(ventana, text="Rectangulo", variable=var1, value=3, command=lambda: calcular(lbtexto, lbtexto2))
radio3.place(x=20, y=110)
radio4 = tk.Radiobutton(ventana, text="Circulo", variable=var1, value=4, command=lambda: calcular(lbtexto, lbtexto2))
radio4.place(x=20, y=140)

check1 = tk.Checkbutton(ventana, text="Area", variable=var2, command=lambda: calcular2())
check1.place(x=20, y=210)
check1 = tk.Checkbutton(ventana, text="Perimetro", variable=var3, command=lambda: calcular2())
check1.place(x=20, y=240)

lbtexto = ttk.Label(ventana, text=textoEtiqueta)
lbtexto.place(x=160, y=50)
lbtexto2 = ttk.Label(ventana, text=textoEtiqueta2)
# lbtexto2.place(x=160, y=80)


def calcular(et, et2):
    opcionSel = var1.get()

    if opcionSel == 1:  # Cuadrado
        et.config(text="Lado")
        et2.config(text="")
        txvalor2.place_forget()
        txvalor1.place(x=200, y=50)
        lbtexto2.place_forget()
    elif opcionSel == 3:  # Rectangulo
        et.config(text="Base")
        et2.config(text="Altura")
        txvalor1.place(x=200, y=50)
        txvalor2.place(x=200, y=80)
        lbtexto2.place(x=160, y=80)
    elif opcionSel == 2:  # Triangulo
        et.config(text="Base")
        et2.config(text="Altura")
        txvalor1.place(x=200, y=50)
        txvalor2.place(x=200, y=80)
        lbtexto2.place(x=160, y=80)
    elif opcionSel == 4:  # Circulo
        et.config(text="Radio")
        et2.config(text="")
        txvalor2.place_forget()
        txvalor1.place(x=200, y=50)
        lbtexto2.place_forget()

    calcular2()


def calcular2():
    opcionSel = var1.get()
    calcArea = var2.get()
    calcPerim = var3.get()

    try:
        val1 = float(txvalor1.get())
    except ValueError:
        val1 = 0
    try:
        val2 = float(txvalor2.get())
    except ValueError:
        val2 = 0

    area = 0
    perimetro = 0

    if opcionSel == 1:  # Cuadrado
        area = val1 ** 2
        perimetro = val1 * 4
    elif opcionSel == 3:  # Rectangulo
        area = val1 * val2
        perimetro = 2 * (val1 + val2)
    elif opcionSel == 2:  # Triangulo
        area = (val1 * val2) / 2
        perimetro = val1 + val2 + math.sqrt(val1*2 + val2*2)
    elif opcionSel == 4:  # Circulo
        area = math.pi * val1 ** 2
        perimetro = 2 * math.pi * val1

    txresul1.config(state="normal")
    txresul2.config(state="normal")

    if calcArea:
        txresul1.delete(0, tk.END)
        txresul1.insert(0, round(area, 2))
    else:
        txresul1.delete(0, tk.END)

    if calcPerim:
        txresul2.delete(0, tk.END)
        txresul2.insert(0, round(perimetro, 2))
    else:
        txresul2.delete(0, tk.END)

    txresul1.config(state="readonly")
    txresul2.config(state="readonly")


# messagebox.showinfo(message= "Escriba un valor valido para el valor 1")
# messagebox.showinfo(message= "Escriba un valor valido para el valor 2")
# txvalor1.focus

# except:
    # if pos ==1:
    #     messagebox.showinfo(message="Escribe un valor valido para el valor 1")
    #     txvalor1.focus()
    #     txvalor1.select_range(0,END)
    # elif pos == 2:
    #     messagebox.showinfo(message="Escribe un valor valido para el valor 2")
    #     txvalor2.focus()
    #     txvalor2.select_range(0,END)
    # if act2 == False and act3 == False:
    #         messagebox.showinfo(message="Selecciona el area o el perimetro")
    # elif opcionSe2 == False:
    #     messagebox.showinfo(message="Selecciona una figura")

            

ventana.mainloop()



