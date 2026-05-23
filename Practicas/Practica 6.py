from tkinter import END, messagebox, ttk
import tkinter as tk 

Ventana= tk.Tk()
Ventana.config(width=300,height=350)
Ventana.title("Practica 6 listas desplegables")

ttk.Label(Ventana,text="Seleciona una Opcion").place(x=20,y=20)
cbCategorias = ttk.Combobox(Ventana,state="readonly",values=["A","B","C","D"])
cbCategorias.place(x=20,y=50)

def Evaluar():
    opcion=cbCategorias.get()
    if opcion == "A":
        messagebox.showinfo(message="Elegiste la Opcion A")
    elif opcion == "B":
        messagebox.showinfo(message="Elegiste la Opcion B")
    elif opcion == "C":
        messagebox.showinfo(message="Elegiste la Opcion C")
    elif opcion ==  "D":
        messagebox.showinfo(message=f"Elegiste la Opcion D")

ttk.Button(Ventana,text="Aceptar",command=Evaluar).place(x=20,y=80)

Ventana.mainloop()
