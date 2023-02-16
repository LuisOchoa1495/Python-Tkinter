"""
FORMULARIO DE REGISTRO DE USUARIO
-Registro de usuario y contraseña
-Guardar en bd SQlite

"""
from tkinter import *
from tkinter import ttk
from tkinter import messagebox 
#Python image Library
from PIL import ImageTk, Image
from subprocess import call
import sys

import sqlite3

class Login:
    db_name='database_proyecto.db'
    
    def __init__(self,ventana_login):
        self.window=ventana_login  
        self.window.title("INGRESAR AL SISTEMA")
        self.window.geometry("330x370")
        self.window.resizable(0,0)
        self.window.config(bd=10)
        
        "--------------- Titulo --------------------"
        titulo= Label(ventana_login, text="INICIAR SESION",fg="black",font=("Comic Sans", 13,"bold"),pady=10).pack()

        "--------------- Nuevo usuario logo --------------------"
        imagen_calculadora=Image.open("D:/EIGHTA/PYTHON-TKINTER/SISTEMA DESKTOP/login.png")
        nueva_imagen=imagen_calculadora.resize((40,40))
        render=ImageTk.PhotoImage(nueva_imagen)
        label_imagen= Label(ventana_login, image= render)
        label_imagen.image=render
        label_imagen.pack(pady=5)


        "--------------- Marco --------------------"
        marco = LabelFrame(ventana_login, text="Ingrese sus datos",font=("Comic Sans", 10,"bold"))
        marco.config(bd=2)
        marco.pack()

        "--------------- Formulario --------------------"
        label_dni=Label(marco,text="DNI: ",font=("Comic Sans", 10,"bold")).grid(row=0,column=0,sticky='s',padx=5,pady=10)
        self.dni=Entry(marco,width=25)
        self.dni.grid(row=0, column=1, padx=5, pady=10)

        label_nombres=Label(marco,text="Contraseña: ",font=("Comic Sans", 10,"bold")).grid(row=1,column=0,sticky='s',padx=10,pady=10)
        self.nombres=Entry(marco,width=25,show="*")
        self.nombres.grid(row=1, column=1, padx=10, pady=10)
        
        "--------------- Frame botones --------------------"
        frame_botones=Frame(ventana_login)
        frame_botones.pack()

        "--------------- Botones --------------------"
        boton_ingresar=Button(frame_botones,text="INGRESAR",command=ventana_login.quit,height=2,width=12,bg="green",fg="white",font=("Comic Sans", 10,"bold")).grid(row=0, column=1, padx=10, pady=15)
        boton_registrar=Button(frame_botones,text="REGISTRAR",command=self.LLamar_registro,height=2,width=12,bg="blue",fg="white",font=("Comic Sans", 10,"bold")).grid(row=0, column=2, padx=10, pady=15)
        label_=Label(frame_botones,text="⬇ ¿Olvido su contraseña? ⬇",font=("Comic Sans", 10,"bold")).grid(row=1,column=1,columnspan=2,sticky='s')
        boton_olvido=Button(frame_botones,text="RECUPERAR CONTRASEÑA",command=ventana_login.quit ,height=2,width=24,bg="gray",fg="white",font=("Comic Sans", 10,"bold")).grid(row=2, column=1, columnspan=2, padx=10, pady=8)
    
    def LLamar_registro(self):
        ventana_login.destroy()    
        call([sys.executable, 'D:/EIGHTA/PYTHON-TKINTER/SISTEMA DESKTOP/Formulario_registro.py', 'htmlfilename.htm'])

if __name__ == '__main__':
    ventana_login=Tk()
    application=Login(ventana_login)
    ventana_login.mainloop()
