from tkinter import messagebox, ttk, END
import tkinter as tk

Ventana=tk.Tk()
Ventana.geometry("300x250")
Ventana.title("Calculadora de IMC")

ttk.Label(Ventana, text="Peso (Kg):").pack(pady=5)
entry1 = ttk.Entry(Ventana, width=20)
entry1.pack(pady=5)
ttk.Label(Ventana, text="Altura (m):").pack(pady=5)
entry2 = ttk.Entry(Ventana, width=20)
entry2.pack(pady=5)
ttk.Label(Ventana, text="Resultado")
entry3 = tk.Entry(Ventana, state= "readonly")
entry3.pack(pady=5)

def calcular_imc():
    try:
        peso = float(entry1.get())
        altura = float(entry2.get())
        entry3.config(state="normal")
        entry3.delete(0,END)
        imc = peso / (altura ** 2)
        if imc < 18.5:
            Estatus = "Peso Bajo"
        elif imc < 25:
            Estatus = "Normal"
        elif imc < 30:
            Estatus = "Sobrepeso"
        elif imc > 30:
            Estatus = "Obesidad"
            
        entry3.insert(0,Estatus)
        entry3.config(state="readonly")
    except ValueError:
        messagebox.showerror("Inserta un valor valido")

ttk.Button(Ventana, text="Calcular IMC", command=calcular_imc).pack(pady=10)

Ventana.mainloop()