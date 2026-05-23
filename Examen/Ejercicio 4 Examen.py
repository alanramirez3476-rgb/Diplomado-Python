from tkinter import messagebox, ttk
import tkinter as tk

Ventana=tk.Tk()
Ventana.geometry("300x250")
Ventana.title("Calculadora de IMC")

ttk.Label(Ventana, text="Peso (Kg):").place(x=10, y=10)

# IMC < 18.5 = "Peso Bajo"
# IMC < 25 = "Normal"
# IMC < 30 = "Sobrepeso"
# IMC > 30 = "Obesidad"

#[ \text{IMC} = \frac{\text{peso}}{\text{altura}^2} ]

Ventana.mainloop()