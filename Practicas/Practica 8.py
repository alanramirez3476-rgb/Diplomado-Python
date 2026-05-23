from tkinter import END, messagebox,ttk
import tkinter as tk

ventana=tk.Tk()
ventana.geometry("250x300")
ventana.title("Practica 8 Ciclos")

cbOpciones=ttk.Combobox(ventana, values=["Libros","Cuadernos","Reglas"])
cbOpciones.place(x=20,y=30)

listaDatos=tk.Listbox(ventana,width=20, height=10)
listaDatos.place(x=20, y=60)


def agregar():
    listaDatos.delete(0,END)
    var1=cbOpciones.get()

    for i in range(0,5):
        listaDatos.insert(i, str(i) + " " + var1 + " de 4")

btAgregar=tk.Button(ventana, text="Agregar", command=agregar)
btAgregar.place(x=150,y=60)

ventana.mainloop() 