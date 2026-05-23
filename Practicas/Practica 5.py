from tkinter import END, ttk, messagebox
import tkinter as tk

ventana = tk.Tk()
ventana.config(width=200, height=300)
ventana.title("Calculadora")

ttk.Label(ventana, text="Ingresa valor 1").place(x=20,y=30)
ttk.Label(ventana, text="Ingresa valor 2").place(x=20,y=80)
ttk.Label(ventana, text="Ingresa valor 3").place(x=20,y=130)
ttk.Label(ventana, text= "Resultado").place(x=20,y=180)

txIngresavalor1 = ttk.Entry(ventana)
txIngresavalor1.place(x=20,y=50)

txIngresavalor2 = ttk.Entry(ventana)
txIngresavalor2.place(x=20,y=100)

txIngresavalor3 = ttk.Entry(ventana)
txIngresavalor3.place(x=20,y=150)

txResultado = ttk.Entry(ventana,state="readonly")
txResultado.place (x=20, y=200)

def Maximo():
    try:
        valor1 = float(txIngresavalor1.get())
        valor2 = float(txIngresavalor2.get())
        valor3 = float(txIngresavalor3.get())
        txResultado.config(state="normal")

        if valor1 > valor2 and valor1 > valor3:
            Resultado = valor1
        elif valor2 > valor1 and valor2 > valor3:
            Resultado = valor2
        else:
            Resultado = valor3
            
        txResultado.delete(0,END)
        txResultado.insert(0,str(Resultado))
        txResultado.config(state="readonly")
    except:
        messagebox.showinfo(message= "Escibe un valor valido")



def Minimo ():
    valor1 = float(txIngresavalor1.get())
    valor2 = float(txIngresavalor2.get())
    valor3 = float(txIngresavalor3.get())
    txResultado.config(state="normal")

    if valor1 < valor2 and valor1 < valor3:
        Resultado = valor1
    elif valor2 < valor1 and valor2 < valor3:
        Resultado = valor2
    else:
        Resultado = valor3
    txResultado.delete(0,END)
    txResultado.insert(0,str(Resultado))
    txResultado.config(state="readonly")

def Limpiar():

    txIngresavalor1.delete(0,END)
    txIngresavalor2.delete(0,END)
    txIngresavalor3.delete(0,END)
    txResultado.config(state="normal")
    txResultado.delete(0,END)
    txResultado.config(state="readonly")
    txIngresavalor1.focus()

btMinimo=ttk.Button(ventana,width=8, text = "Minimo", command= Minimo) 
btMinimo.place (x=70, y =240)

btCalcular=ttk.Button(ventana,width=8, text = "Maximo", command= Maximo ) 
btCalcular.place (x=10, y =240) 

btLimpiar=ttk.Button(ventana,width=8, text = "Limpiar", command= Limpiar) 
btLimpiar.place (x=130, y =240)

ventana.mainloop()