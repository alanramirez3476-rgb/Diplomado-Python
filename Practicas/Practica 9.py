from tkinter import END,messagebox,ttk
import tkinter as tk

ventana=tk.Tk()
ventana.config(width=300,height=300)
ventana.title("Practica 10")

#crear las variables para los checks
var1=tk.BooleanVar()
var2=tk.BooleanVar()
var3=tk.IntVar()
textoEtiqueta="Hola"


#crear los checks
check1 = tk.Checkbutton(ventana, text="Opcion 1", variable=var1, command=lambda:ocultar(lbtexto))
check1.place(x=20, y=30)
check2 = tk.Checkbutton(ventana, text="Opcion 2", variable=var2, command=lambda:ocultar(lbtexto))
check2.place(x=20, y=50)

#crear los radios
radio1 = tk.Radiobutton(ventana, text="Opcion 1", variable=var3, value=1, command=lambda:calcular(lbtexto))
radio1.place(x=20, y=90)
radio2 = tk.Radiobutton(ventana, text="Opcion 2", variable=var3, value=2, command=lambda:calcular(lbtexto))
radio2.place(x=20, y=110)
radio3 = tk.Radiobutton(ventana, text="Opcion 3", variable=var3, value=3, command=lambda:calcular(lbtexto))
radio3.place(x=20, y=130)


lbtexto = ttk.Label(ventana, text=textoEtiqueta)
#lbtexto.place(x=90, y=210)

def calcular(et):
    opcionSel = var3.get()
    global textoEtiqueta

    if opcionSel == 1:
        messagebox.showinfo(message="Elegiste 1")
        textoEtiqueta="Bienvenido"
        et.place(x=150, y=250)
    elif opcionSel == 2:
        messagebox.showinfo(message="Elegiste 2")
        textoEtiqueta="Buenas tardes"
        et.place(x=150, y=250)
    elif opcionSel == 3:
        messagebox.showinfo(message="Elegiste 3")
        textoEtiqueta="Buenas noches"
        et.place(x=150, y=250)

    et.config(text= textoEtiqueta)

def ocultar(et):
    acti=var1.get()



    if acti==True:
        et.place(x=100,y=200)
    else:
        et.place_forget()
    
   
ventana.mainloop()