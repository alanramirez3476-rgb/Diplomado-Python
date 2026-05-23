import tkinter as tk
from tkinter import ttk, messagebox, END 

class Calculadora:
    def __init__(self,n1,n2):
        self.n1 = n1
        self.n2 = n2
    def sumar(self):
        return self.n1 + self.n2

ventana = tk.Tk()
ventana.geometry("300x250")
ventana.title("Calculadora de Sumas")
ttk.Label(ventana, text="Número 1:").place(x=10, y=10)
entry1 = ttk.Entry(ventana, width=20)
entry1.place(x=10, y=40)    
ttk.Label(ventana, text="Número 2:").place(x=10, y=80)
entry2 = ttk.Entry(ventana, width=20)
entry2.place(x=10, y=110)
entry3 = ttk.Entry(ventana, width=20, state="readonly")
entry3.place(x=10, y=190)
def calcular_suma():
    try:
        n1 = float(entry1.get())
        n2 = float(entry2.get())
        calculadora = Calculadora(n1, n2)
        resultado = calculadora.sumar()
        entry3.config(state="normal")
        entry3.delete(0, tk.END)
        entry3.insert(0, str(resultado))
        entry3.config(state="readonly")

    except ValueError:
        messagebox.showerror("Error", "Ingrese un valor valido")

ttk.Button(ventana, text="Calcular Suma", command=calcular_suma).place(x=10, y=150)

ventana.mainloop()