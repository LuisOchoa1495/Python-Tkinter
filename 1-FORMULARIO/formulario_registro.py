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

import sqlite3

class Registro:
    db_name='database.db'
    def __init__(self,ventana):
        self.window=ventana   
        self.window.title("FORMULARIO DE REGISTRO")
        self.window.geometry("390x540")
        self.window.resizable(0,0)
        self.window.config(bd=10)
        
        "--------------- Titulo --------------------"
        titulo= Label(ventana, text="REGISTRO DE USUARIO",fg="black",font=("Comic Sans", 13,"bold"),pady=10).pack()

        "--------------- Nuevo usuario logo --------------------"
        imagen_calculadora=Image.open("D:/EIGHTA/PYTHON-TKINTER/1-FORMULARIO/nuevo_usuario.png")
        nueva_imagen=imagen_calculadora.resize((40,40))
        render=ImageTk.PhotoImage(nueva_imagen)
        label_imagen= Label(ventana, image= render)
        label_imagen.image=render
        label_imagen.pack(pady=5)


        "--------------- Marco --------------------"
        marco = LabelFrame(ventana, text="Datos personales",font=("Comic Sans", 10,"bold"))
        marco.config(bd=2)
        marco.pack()

        "--------------- Formulario --------------------"
        label_dni=Label(marco,text="DNI: ",font=("Comic Sans", 10,"bold")).grid(row=0,column=0,sticky='s',padx=5,pady=10)
        self.dni=Entry(marco,width=25)
        self.dni.grid(row=0, column=1, padx=5, pady=10)

        label_nombres=Label(marco,text="Nombre: ",font=("Comic Sans", 10,"bold")).grid(row=1,column=0,sticky='s',padx=10,pady=10)
        self.nombres=Entry(marco,width=25)
        self.nombres.grid(row=1, column=1, padx=10, pady=10)

        label_apellidos=Label(marco,text="Apellidos: ",font=("Comic Sans", 10,"bold")).grid(row=2,column=0,sticky='s',padx=10,pady=10)
        self.apellidos=Entry(marco,width=25)
        self.apellidos.grid(row=2, column=1, padx=10, pady=10)

        label_sexo=Label(marco,text="Sexo: ",font=("Comic Sans", 10,"bold")).grid(row=3,column=0,sticky='s',padx=10,pady=10)
        self.combo_sexo=ttk.Combobox(marco,values=["Masculino", "Femenino"], width=22)
        self.combo_sexo.grid(row=3,column=1,padx=10,pady=10)

        label_edad=Label(marco,text="Edad: ",font=("Comic Sans", 10,"bold")).grid(row=4,column=0,sticky='s',padx=10,pady=10)
        self.edad=Entry(marco,width=25)
        self.edad.grid(row=4, column=1, padx=10, pady=10)

        label_correo=Label(marco,text="Correo electronico: ",font=("Comic Sans", 10,"bold")).grid(row=5,column=0,sticky='s',padx=10,pady=10)
        self.correo=Entry(marco,width=25)
        self.correo.grid(row=5, column=1, padx=10, pady=10)

        label_password=Label(marco,text="Contraseña: ",font=("Comic Sans", 10,"bold")).grid(row=6,column=0,sticky='s',padx=10,pady=10)
        self.password=Entry(marco,width=25,show="*")
        self.password.grid(row=6, column=1, padx=10, pady=10)

        label_password=Label(marco,text="Repetir contraseña: ",font=("Comic Sans", 10,"bold")).grid(row=7,column=0,sticky='s',padx=10,pady=10)
        self.repetir_password=Entry(marco,width=25,show="*")
        self.repetir_password.grid(row=7, column=1, padx=10, pady=10)

        "--------------- Frame botones --------------------"
        frame_botones=Frame(ventana)
        frame_botones.pack()

        "--------------- Botones --------------------"
        boton_registrar=Button(frame_botones,text="REGISTRAR",command=self.Registrar_usuario ,height=2,width=10,bg="green",fg="white",font=("Comic Sans", 10,"bold")).grid(row=0, column=1, padx=10, pady=15)
        boton_limpiar=Button(frame_botones,text="LIMPIAR",command=self.Limpiar_formulario ,height=2,width=10,bg="gray",fg="white",font=("Comic Sans", 10,"bold")).grid(row=0, column=2, padx=10, pady=15)
        boton_cancelar=Button(frame_botones,text="CERRAR",command=ventana.quit ,height=2,width=10,bg="red",fg="white",font=("Comic Sans", 10,"bold")).grid(row=0, column=3, padx=10, pady=15)
        
    def Ejecutar_consulta(self, query, parameters=()):
        with sqlite3.connect(self.db_name) as conexion:
            cursor=conexion.cursor()
            result=cursor.execute(query,parameters)
            conexion.commit()
        return result
    
    def Limpiar_formulario(self):
        self.dni.delete(0, END)
        self.nombres.delete(0, END)
        self.apellidos.delete(0, END)
        self.combo_sexo.delete(0, END)
        self.edad.delete(0, END)
        self.correo.delete(0, END)
        self.password.delete(0, END)
        self.repetir_password.delete(0, END)
        
    def Registrar_usuario(self):
        query='INSERT INTO Usuario VALUES(NULL, ?, ?, ?, ?, ?, ?, ?)'
        parameters = (self.dni.get(),self.nombres.get(),self.apellidos.get(),self.combo_sexo.get(),self.edad.get(),self.correo.get(),self.password.get())
        self.Ejecutar_consulta(query, parameters)
        messagebox.showinfo("Registro Exitoso", f'Bienvenido {self.nombres.get()} {self.apellidos.get()}')
        print('USUARIO CREADO')
        self.Limpiar_formulario()
              
if __name__ == '__main__':
    ventana=Tk()
    application=Registro(ventana)
    ventana.mainloop()
