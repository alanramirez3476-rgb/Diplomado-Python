import tkinter as tk
from tkinter import messagebox, END

ventana = tk.Tk()
ventana.config(width=350, height=300)
ventana.title("Practica 10")

var1 = tk.BooleanVar()
var2 = tk.BooleanVar()
var3 = tk.IntVar()

tk.Label(ventana, text="Tipo de Figura").place(x=20, y=0)
tk.Label(ventana, text="Valores").place(x=150, y=0)

# Cuadrado
frame_cuadrado = tk.Frame(ventana)
tk.Label(frame_cuadrado, text="Lado:").grid(row=0, column=0)
lado_cuadrado = tk.Entry(frame_cuadrado, width=10)
lado_cuadrado.grid(row=0, column=1)

# Rectángulo
frame_rectangulo = tk.Frame(ventana)
tk.Label(frame_rectangulo, text="Base:").grid(row=0, column=0)
base_rectangulo = tk.Entry(frame_rectangulo, width=10)
base_rectangulo.grid(row=0, column=1)
tk.Label(frame_rectangulo, text="Altura:").grid(row=1, column=0)
altura_rectangulo = tk.Entry(frame_rectangulo, width=10)
altura_rectangulo.grid(row=1, column=1)

# Triángulo
frame_triangulo = tk.Frame(ventana)
tk.Label(frame_triangulo, text="Base:").grid(row=0, column=0)
base_triangulo = tk.Entry(frame_triangulo, width=10)
base_triangulo.grid(row=0, column=1)
tk.Label(frame_triangulo, text="Altura:").grid(row=1, column=0)
altura_triangulo = tk.Entry(frame_triangulo, width=10)
altura_triangulo.grid(row=1, column=1)

# Círculo
frame_circulo = tk.Frame(ventana)
tk.Label(frame_circulo, text="Radio:").grid(row=0, column=0)
radio_circulo = tk.Entry(frame_circulo, width=10)
radio_circulo.grid(row=0, column=1)

def calcular():
    opcionSel = var3.get()
    frame_cuadrado.place_forget()
    frame_rectangulo.place_forget()
    frame_triangulo.place_forget()
    frame_circulo.place_forget()

    if opcionSel == 1:
        frame_cuadrado.place(x=150, y=30)
    elif opcionSel == 2:
        frame_triangulo.place(x=150, y=30)
    elif opcionSel == 3:
        frame_rectangulo.place(x=150, y=30)
    elif opcionSel == 4:
        frame_circulo.place(x=150, y=30)

tk.Radiobutton(ventana, text="Cuadrado", variable=var3, value=1, command=calcular).place(x=20, y=30)
tk.Radiobutton(ventana, text="Triángulo", variable=var3, value=2, command=calcular).place(x=20, y=60)
tk.Radiobutton(ventana, text="Rectángulo", variable=var3, value=3, command=calcular).place(x=20, y=90)
tk.Radiobutton(ventana, text="Círculo", variable=var3, value=4, command=calcular).place(x=20, y=120)

tk.Label(ventana, text="Resultados").place(x=20, y=150)
resultado_area = tk.Label(ventana, text="Área: ---", width=20, anchor="w")
resultado_area.place(x=20, y=180)
resultado_perimetro = tk.Label(ventana, text="Perímetro: ---", width=20, anchor="w")
resultado_perimetro.place(x=20, y=210)

def calcular_area():
    opcionSel = var3.get()
    try:
        if opcionSel == 1:
            lado = float(lado_cuadrado.get())
            area = lado ** 2
        elif opcionSel == 2:
            base = float(base_triangulo.get())
            altura = float(altura_triangulo.get())
            area = 0.5 * base * altura
        elif opcionSel == 3:
            base = float(base_rectangulo.get())
            altura = float(altura_rectangulo.get())
            area = base * altura
        elif opcionSel == 4:
            radio = float(radio_circulo.get())
            area = 3.14159 * radio ** 2
        else:
            return
        resultado_area.config(text=f"Área: {area:.2f}")
    except ValueError:
        messagebox.showerror(message="Por favor, ingresa valores numéricos válidos.")

def calcular_perimetro():
    opcionSel = var3.get()
    try:
        if opcionSel == 1:
            lado = float(lado_cuadrado.get())
            perimetro = 4 * lado
        elif opcionSel == 2:
            base = float(base_triangulo.get())
            altura = float(altura_triangulo.get())
            perimetro = base + 2 * altura  # Triángulo isósceles
        elif opcionSel == 3:
            base = float(base_rectangulo.get())
            altura = float(altura_rectangulo.get())
            perimetro = 2 * (base + altura)
        elif opcionSel == 4:
            radio = float(radio_circulo.get())
            perimetro = 2 * 3.14159 * radio
        else:
            return
        resultado_perimetro.config(text=f"Perímetro: {perimetro:.2f}")
    except ValueError:
        messagebox.showerror(message="Ingresa valor valido.")

# Selección de operaciones
def operacion_select():
    if var1.get():
        calcular_area()
    if var2.get():
        calcular_perimetro()
    if not var1.get() and not var2.get():
        messagebox.showerror(message="Elige un tipo de cálculo")

tk.Checkbutton(ventana, text="Área", variable=var1).place(x=250, y=180)
tk.Checkbutton(ventana, text="Perímetro", variable=var2).place(x=250, y=210)

tk.Button(ventana, text="Calcular", command=operacion_select).place(x=150, y=250)
tk.Button(ventana, text="Limpiar", command=lambda: limpiar()).place(x=220, y=250)

def limpiar():
    resultado_area.config(text="Área: ---")
    resultado_perimetro.config(text="Perímetro: ---")
    lado_cuadrado.delete(0, END)
    base_rectangulo.delete(0, END)
    altura_rectangulo.delete(0, END)
    base_triangulo.delete(0, END)
    altura_triangulo.delete(0, END)
    radio_circulo.delete(0, END)
    var1.set(False)
    var2.set(False)
    var3.set(0)
    frame_cuadrado.place_forget()
    frame_rectangulo.place_forget()
    frame_triangulo.place_forget()
    frame_circulo.place_forget()

ventana.mainloop()