import tkinter as tk
from tkinter import ttk, messagebox

Ventana = tk.Tk()
Ventana.geometry("300x250")
Ventana.title("Verificador de años bisiestos")

ttk.Label(Ventana, text="Ingrese un año:").place(x=10, y=10)

entry = ttk.Entry(Ventana, width=20)
entry.place(x=10, y=40)

def calcular():
        año = entry.get()
        if not año.isdigit():
            messagebox.showerror("Error", "Ingrese un valor valido")
            return
        if (int(año) % 4 == 0 and int(año) % 100 != 0) or (int(año) % 400 == 0):
            messagebox.showinfo("Resultado", "El año es bisiesto")
        else:
            messagebox.showinfo("Resultado", "El año no es bisiesto")
            
ttk.Button(Ventana,text="Verificar",command=calcular).pack(pady=5)

Ventana.mainloop()