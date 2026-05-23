from tkinter import END, messagebox, ttk
import tkinter as tk

#Ventana Principal
Ventana=tk.Tk()
Ventana.geometry("180x180")
Ventana.title("Practica 10.5")

ttk.Label(Ventana, text= "Itroduce un numero a buscar").pack(pady=5)
Caja=ttk.Entry (Ventana)
Caja.pack(pady=5)

Lista=[12,45,7,23,89,4,56,17]

def buscar_valor():
    try:
        Buscado=int(Caja.get())
        i = 0
        Encontrado=False
        while i < len(Lista):
            if Lista[i] == Buscado:
                Encontrado=True
                break
            i+=1
        if Encontrado==True:
            messagebox.showinfo("Resultado", f"El valor {Buscado} se encuentra en la posicion {i}")
        else:
            messagebox.showwarning("No encontrado", "El valor no esta en la lista")
    except:
        messagebox.showerror("Error","Introduce un numero valido")

def mostrar_maximo():
    Maximo=max(Lista)
    #messagebox.showinfo("Maximo",f"El valor maximode la lista es:{Maximo}")
    messagebox.showinfo(message="El valor maximo de la lista es" + str (Maximo))

def abrir_modal():
    modal=tk.Toplevel(Ventana)
    modal.title("Añade un valor")
    modal.grab_set()

    ttk.Label(modal, text="Introduce un valor:").pack(pady=5)
    entrada_modal=ttk.Entry(modal)
    entrada_modal.pack(pady=5)

    def agregar():
        try:

            nuevo=int(entrada_modal.get())
            Lista.append(nuevo)
            messagebox.showinfo("Exito", f"Valor {nuevo} agregado a la lista")
            modal.destroy()
        except:
            messagebox.showerror("Error", "Introduce un numero valido")

    ttk.Button(modal, text="Agregar", command=agregar).pack(pady=10)

ttk.Button(Ventana, text="Buscar", command= buscar_valor).pack(pady=5)
ttk.Button(Ventana, text= "Mostrar Maximo", command= mostrar_maximo).pack(pady=5)
ttk.Button(Ventana, text= "Añadir un valor",command=abrir_modal).pack(pady=5)

Ventana.mainloop()