"""
FORMULARIO DE RECUPERACION DE CONTRASEÑA
-Registro de usuario y contraseña
-Guardar en bd SQlite

"""
from tkinter import *
from tkinter import ttk
from tkinter import messagebox 
#Python image Library
from PIL import ImageTk, Image

import sqlite3

class Recuperar_contraseña:
    db_name='database_proyecto.db'
    
    def __init__(self,vetana):
        self.window=ventana   
        self.window.title("RECUPERAR CONTASEÑA")
        self.window.geometry("390x470")
        self.window.resizable(0,0)
        self.window.config(bd=10)
        
        "--------------- Titulo --------------------"
        titulo= Label(ventana, text="RECUPERAR CONTRASEÑA",fg="black",font=("Comic Sans", 13,"bold"),pady=10).pack()

        "--------------- Nuevo usuario logo --------------------"
        imagen_calculadora=Image.open("D:/EIGHTA/PYTHON-TKINTER/SISTEMA DESKTOP/recuperar_contraseña.png")
        nueva_imagen=imagen_calculadora.resize((60,60))
        render=ImageTk.PhotoImage(nueva_imagen)
        label_imagen= Label(ventana, image= render)
        label_imagen.image=render
        label_imagen.pack(pady=5)


        "--------------- Marco --------------------"
        marco = LabelFrame(ventana, text="Datos de recuperacion",font=("Comic Sans", 10,"bold"))
        marco.config(bd=2)
        marco.pack()

        "--------------- Formulario --------------------"
        label_dni=Label(marco,text="DNI: ",font=("Comic Sans", 10,"bold")).grid(row=0,column=0,sticky='s',padx=5,pady=10)
        self.dni=Entry(marco,width=25)
        self.dni.grid(row=0, column=1, padx=5, pady=10)

        label_nombres=Label(marco,text="Nombres: ",font=("Comic Sans", 10,"bold")).grid(row=1,column=0,sticky='s',padx=10,pady=10)
        self.nombres=Entry(marco,width=25)
        self.nombres.grid(row=1, column=1, padx=10, pady=10)

        label_apellidos=Label(marco,text="Apellidos: ",font=("Comic Sans", 10,"bold")).grid(row=2,column=0,sticky='s',padx=10,pady=10)
        self.apellidos=Entry(marco,width=25)
        self.apellidos.grid(row=2, column=1, padx=10, pady=10)

        label_correo=Label(marco,text="Correo electronico: ",font=("Comic Sans", 10,"bold")).grid(row=3,column=0,sticky='s',padx=10,pady=10)
        self.correo=Entry(marco,width=25)
        self.correo.grid(row=3, column=1, padx=10, pady=10)

        label_password=Label(marco,text="Nueva Contraseña: ",font=("Comic Sans", 10,"bold")).grid(row=4,column=0,sticky='s',padx=10,pady=10)
        self.nuevo_password=Entry(marco,width=25,show="*")
        self.nuevo_password.grid(row=4, column=1, padx=10, pady=10)

        label_password=Label(marco,text="Repetir contraseña: ",font=("Comic Sans", 10,"bold")).grid(row=5,column=0,sticky='s',padx=10,pady=10)
        self.repetir_password=Entry(marco,width=25,show="*")
        self.repetir_password.grid(row=5, column=1, padx=10, pady=10)

        "--------------- Frame botones --------------------"
        frame_botones=Frame(ventana)
        frame_botones.pack()

        "--------------- Botones --------------------"
        boton_registrar=Button(frame_botones,text="RECUPERAR",command=self.Registrar_usuario ,height=2,width=10,bg="green",fg="white",font=("Comic Sans", 10,"bold")).grid(row=0, column=1, padx=10, pady=15)
        boton_cancelar=Button(frame_botones,text="CANCELAR",command=ventana.quit ,height=2,width=10,bg="red",fg="white",font=("Comic Sans", 10,"bold")).grid(row=0, column=3, padx=10, pady=15)
        
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
        self.correo.delete(0, END)
        self.nuevo_password.delete(0, END)
        self.repetir_password.delete(0, END)
        
        
    def Validar_formulario_completo(self):
        if len(self.dni.get()) !=0 and len(self.nombres.get()) !=0 and len(self.apellidos.get()) !=0 and len(self.nuevo_password.get()) !=0 and len(self.repetir_password.get()) !=0 and len(self.correo.get()) !=0:
            return True
        else:
             messagebox.showerror("ERROR", "Complete todos los campos del formulario")
             
    def Validar_contraseña(self):
        if(str(self.nuevo_password.get()) == str(self.repetir_password.get())):
            return True
        else:
            messagebox.showerror("ERROR DE RECUPERACION", "Contraseñas no coinciden")
 
    def Buscar_usuario(self, dni,nombres,apellidos):
        with sqlite3.connect(self.db_name) as conexion:
            cursor=conexion.cursor()
            sql="SELECT * FROM Usuarios WHERE DNI = {} AND Nombres = {} AND Apellidos = {}".format(dni,nombres,apellidos)
            cursor.execute(sql)
            busqueda= cursor.fetchall() # obtener respuesta como lista
            cursor.close()
            return busqueda
    """    
    def Buscar_usuario2(self,query,parameters):
        with sqlite3.connect(self.db_name) as conexion:
            cursor=conexion.cursor()
            cursor.execute(query,parameters)
            busqueda=cursor.fetchall()
            cursor.close()
            return busqueda 
    """
    def Validar_datos_usuario(self):
        dni= self.dni.get()
        nombres=self.nombres.get()
        apellidos=self.apellidos.get()
        dato = self.Buscar_usuario(dni,nombres,apellidos)
        if (dato != []):
            return True
        else:
            messagebox.showerror("ERROR DE RECUPERACION", "Datos de recuperacion no son correctos")

    def Registrar_usuario(self):
        if self.Validar_formulario_completo() and self.Validar_datos_usuario() and self.Validar_contraseña():
            query='UPDATE Usuarios SET Contraseña = (?) WHERE DNI= (?)'
            parameters = (self.nuevo_password.get(), self.dni.get())
            self.Ejecutar_consulta(query, parameters)
            messagebox.showinfo("CONTRASEÑA ACTUALIZADA", f'Contraseña actualizada correctamente: {self.nuevo_password.get()}')
            print('DATOS ACTUALIZADO')
            self.Limpiar_formulario()
            
if __name__ == '__main__':
    ventana=Tk()
    application=Recuperar_contraseña(ventana)
    ventana.mainloop()
