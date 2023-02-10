""""
CALCULADORA
-Se ingresara 2 valores a traves de campos de texto.
-Se utilziara 4 botones que represente las operaciones matematicas.
-Mostrara resultados
"""

from tkinter import *
from tkinter import messagebox 
#Python image Library
from PIL import ImageTk, Image

ventana =Tk()
ventana.title("CALCULADORA")
ventana.geometry("350x360")
ventana.resizable(0,0)
ventana.config(bd=10)

#Imagen calculadora
imagen_calculadora=Image.open("D:/EIGHTA/PYTHON-TKINTER/CALCULADORA/calculadora.png")
nueva_imagen=imagen_calculadora.resize((75,75))
render=ImageTk.PhotoImage(nueva_imagen)
label_imagen= Label(ventana, image= render)
label_imagen.image=render
label_imagen.pack(pady=5)

def cfloat(numero):
    try:
        result=float(numero)
    except:
        messagebox.showerror("ERROR","INTRODUCE BIEN LOS DATOS")
    return result

def sumar():
    
    resultado.set(cfloat(numero1.get())+cfloat(numero2.get()))
    mostrarResultado()
   
def restar():
   
    resultado.set(cfloat(numero1.get())-cfloat(numero2.get()))
    mostrarResultado()
    
 
def multiplicar():
    resultado.set(cfloat(numero1.get())*cfloat(numero2.get()))
    mostrarResultado()   

 
def dividir():
    resultado.set(cfloat(numero1.get())/cfloat(numero2.get()))
    mostrarResultado()   


def mostrarResultado():
    messagebox.showinfo("RESULTADO",f"El resultado de la operacion es: {resultado.get()}")

numero1=StringVar()
numero2=StringVar()
resultado = StringVar()

marco = Frame(ventana, width=300, heigh=200)
marco.config(bd=4,
            padx=15,
            pady=15,    
            relief=SOLID)
marco.pack(side=TOP,anchor=CENTER)
#No alterar su posicionamiento
marco.pack_propagate(False)


Label(marco, text="Primer numero:",fg="black",font=("Arial", 10,"bold")).pack()
Entry(marco,textvariable=numero1,justify="center").pack()

Label(marco, text="Segundo numero:",fg="black",font=("Arial", 10,"bold")).pack()
Entry(marco,textvariable=numero2,justify="center").pack()

Button(marco,text="Sumar",command=sumar,height=1,width=8,bg="black",fg="white",font=("Arial", 9,"bold")).pack(side="left",fill=X,padx=1)
Button(marco,text="Restar",command=restar,height=1,width=8,bg="black",fg="white",font=("Arial", 9,"bold")).pack(side="left",fill=X,padx=1)
Button(marco,text="Multiplicar",command=multiplicar,height=1,width=8,bg="black",fg="white",font=("Arial", 9,"bold")).pack(side="left",fill=X,padx=1)
Button(marco,text="Dividir",command=dividir,height=1,width=8,bg="black",fg="white",font=("Arial", 9,"bold")).pack(side="left",fill=X,padx=1)


Button(ventana,text="Cerrar",command=ventana.quit ,height=2,width=10,bg="red",fg="white",font=("Arial", 9,"bold")).pack(side=BOTTOM)

ventana.mainloop()