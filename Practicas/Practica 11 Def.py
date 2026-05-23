from tkinter import END, messagebox, ttk
import tkinter as tk

ventana  =  tk.Tk()
ventana.config(width=400, height=300)
ventana.title("Practica 11")

listaDatos=tk.Listbox(ventana,width=30)
listaDatos.place(x=20, y=20)


tk.Label(ventana, text= "Promedio General").place(x=220, y=20)
Promedio = tk.Entry(ventana, width=20, state= "readonly")
Promedio.place(x=220, y=40)

 
tk.Label(ventana, text= "Numero de Reprobados").place(x=220, y=60)
Reprobados = tk.Entry(ventana, width=20, state= "readonly")
Reprobados.place(x=220, y=80)

   
tk.Label(ventana, text= "Nota Maxima").place(x=220, y = 100)
Maxima = tk.Entry(ventana, width=20, state= "readonly")
Maxima.place(x=220, y=120)


def modal():
    
    modal = tk.Toplevel(ventana)
    modal.title("Añade un Valor")
    modal.geometry("150x300")
    modal.grab_set() 
    
    
    ttk.Label(modal, text="Introduce el Nombre").pack(pady=5)
    entrada_nombre = ttk.Entry(modal)
    entrada_nombre.pack(pady=5)
    
    ttk.Label(modal, text="Introduce la Calificacion").pack(pady=5)
    entrada_calificacion = ttk.Entry(modal)
    entrada_calificacion.pack(pady=5)
    
     
    global lista_calificaciones
    lista_nombres = []
    lista_calificaciones = []

    
    
    def insertar_datos():
        nombre = str(entrada_nombre.get())
        calificacion = float(entrada_calificacion.get())
        lista_nombres.append(nombre)
        lista_calificaciones.append(calificacion)
        agregar_listbox()
        
    def agregar_listbox():
        listaDatos.delete(0,END)
        for i in range(len(lista_nombres)):
            listaDatos.insert(i, f"{lista_nombres[i]}, {lista_calificaciones[i]}")
        entrada_calificacion.delete(0,END)
        entrada_nombre.delete(0,END)
        entrada_nombre.focus()
    
    ttk.Button(modal, text="Agregar a la lista", command=insertar_datos).pack(pady=5)

def estadisticas():
    
    global lista_calificaciones
    
    
    Promedio.config(state="normal") 
    Promedio.delete(0, END) 
    
    sumatoria = sum(lista_calificaciones)
    promedio_general = sumatoria / len(lista_calificaciones)
    
    Promedio.insert(0, str(promedio_general)) 
    Promedio.config(state="readonly")

    
    Maxima.config(state = "normal")
    Maxima.delete(0,END)
    
    nota_maxima = max(lista_calificaciones)
    
    Maxima.insert(0,str(nota_maxima))
    Maxima.config(state = "readonly")
    
    
    Reprobados.config(state = "normal")
    Reprobados.delete(0, END)
    
    
    cantidad_reprobados = 0
    for i in range(len(lista_calificaciones)):
        if lista_calificaciones[i] < 60:
            cantidad_reprobados += 1
        elif i == len(lista_calificaciones):
            break 
        i+=1 
         
    Reprobados.insert(0,str(cantidad_reprobados))
    Reprobados.config(state = "readonly")

    


ttk.Button(ventana, text= "Nuevo Alumno", command=modal).place(x=220, y=150)
ttk.Button(ventana, text = "Calculo Estadisticas", command = estadisticas). place(x=220, y =180)


ventana.mainloop()



