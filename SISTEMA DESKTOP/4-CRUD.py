"""
CRUD-PRODUCTOS
-Registro de Prouctos
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

class Producto:
    db_name='database_proyecto.db'
    
    def __init__(self, ventana_recuperar):
        self.window=ventana_recuperar   
        self.window.title("APLICACION")
        self.window.geometry("520x600")
        self.window.resizable(0,0)
        self.window.config(bd=10)
        
        "--------------- Titulo --------------------"
        titulo= Label(ventana_recuperar, text="PRODUCTOS ELECTRONICOS",fg="black",font=("Comic Sans", 17,"bold"),pady=10).pack()

        "--------------- Logos productos --------------------"
        frame_logo_productos = LabelFrame(ventana_recuperar)
        frame_logo_productos.config(bd=0)
        frame_logo_productos.pack()

        #Logo arduino
        imagen_arduino=Image.open("D:/EIGHTA/PYTHON-TKINTER/SISTEMA DESKTOP/Imagenes/arduino-logo.png")
        nueva_imagen=imagen_arduino.resize((60,60))
        render=ImageTk.PhotoImage(nueva_imagen)
        label_imagen= Label(frame_logo_productos, image= render)
        label_imagen.image=render
        label_imagen.grid(row=0, column=0,padx=15,pady=5)


        #Logo nodemcu
        imagen_nodemcu=Image.open("D:/EIGHTA/PYTHON-TKINTER/SISTEMA DESKTOP/Imagenes/nodemcu-logo.png")
        nueva_imagen=imagen_nodemcu.resize((60,60))
        render=ImageTk.PhotoImage(nueva_imagen)
        label_imagen= Label(frame_logo_productos, image= render)
        label_imagen.image=render
        label_imagen.grid(row=0, column=1,padx=15,pady=5)
        
        #Logo raspberry
        imagen_raspberry=Image.open("D:/EIGHTA/PYTHON-TKINTER/SISTEMA DESKTOP/Imagenes/raspberry-logo.png")
        nueva_imagen=imagen_raspberry.resize((60,60))
        render=ImageTk.PhotoImage(nueva_imagen)
        label_imagen= Label(frame_logo_productos, image= render)
        label_imagen.image=render
        label_imagen.grid(row=0, column=2,padx=15,pady=5)

        "--------------- Frame marco --------------------"
        marco = LabelFrame(ventana_recuperar, text="Registro del producto",font=("Comic Sans", 10,"bold"),pady=5)
        marco.config(bd=2)
        marco.pack()

        "--------------- Formulario --------------------"
        label_nombre=Label(marco,text="Nombre del producto: ",font=("Comic Sans", 10,"bold")).grid(row=0,column=0,sticky='s',padx=5,pady=8)
        self.nombre=Entry(marco,width=25)
        self.nombre.grid(row=0, column=1, padx=5, pady=8)
        
        label_nota=Label(marco,text="*Seleccione una pregunta y brinde la respuesta correcta.",font=("Comic Sans", 9,"bold"),foreground="blue").grid(row=1,column=0,columnspan=2,sticky='s',padx=8)

        label_pregunta=Label(marco,text="Pregunta: ",font=("Comic Sans", 10,"bold")).grid(row=2,column=0,sticky='s',padx=5,pady=8)
        self.combo_pregunta=ttk.Combobox(marco,values=["¿Nombre de tu primera mascota?","¿Lugar dónde fuiste al colegio?","¿En que ciudad naciste?","¿Cómo se llama tu equipo favorito?"], width=30,state="readonly")
        self.combo_pregunta.current(0)
        self.combo_pregunta.grid(row=2,column=1,padx=5,pady=8)

        label_respuesta=Label(marco,text="Respuesta: ",font=("Comic Sans", 10,"bold")).grid(row=3,column=0,sticky='s',padx=5,pady=8)
        self.respuesta=Entry(marco,width=33)
        self.respuesta.grid(row=3, column=1, padx=5, pady=8)

        label_password=Label(marco,text="Nueva Contraseña: ",font=("Comic Sans", 10,"bold")).grid(row=4,column=0,sticky='s',padx=5,pady=8)
        self.nuevo_password=Entry(marco,width=25,show="*")
        self.nuevo_password.grid(row=4, column=1, padx=5, pady=8)

        label_password=Label(marco,text="Repetir contraseña: ",font=("Comic Sans", 10,"bold")).grid(row=5,column=0,sticky='s',padx=10,pady=8)
        self.repetir_password=Entry(marco,width=25,show="*")
        self.repetir_password.grid(row=5, column=1, padx=5, pady=8)

        "--------------- Frame botones --------------------"
        frame_botones=Frame(ventana_recuperar)
        frame_botones.pack()

        "--------------- Botones --------------------"
        boton_recuperar=Button(frame_botones,text="REGISTRAR",command=self.Restablecer_contraseña ,height=2,width=10,bg="green",fg="white",font=("Comic Sans", 10,"bold")).grid(row=0, column=1, padx=10, pady=10)
        boton_cancelar=Button(frame_botones,text="LIMPIAR",command=self.LLamar_login ,height=2,width=10,bg="red",fg="white",font=("Comic Sans", 10,"bold")).grid(row=0, column=3, padx=10, pady=10)
        
    def Ejecutar_consulta(self, query, parameters=()):
        with sqlite3.connect(self.db_name) as conexion:
            cursor=conexion.cursor()
            result=cursor.execute(query,parameters)
            conexion.commit()
        return result 
    
    def Limpiar_formulario(self):
        self.dni.delete(0, END)
        self.respuesta.delete(0, END)
        self.nuevo_password.delete(0, END)
        self.repetir_password.delete(0, END)     
        
    def Validar_formulario_completo(self):
        if len(self.dni.get()) !=0 and len(self.nuevo_password.get()) !=0 and len(self.repetir_password.get()) !=0 and len(self.respuesta.get()) !=0:
            return True
        else:
             messagebox.showerror("ERROR", "Complete todos los campos del formulario")
             
    def Validar_contraseña(self):
        if(str(self.nuevo_password.get()) == str(self.repetir_password.get())):
            return True
        else:
            messagebox.showerror("ERROR DE RECUPERACION", "Contraseñas no coinciden")
 
    def Buscar_usuario(self, dni, respuesta):
        with sqlite3.connect(self.db_name) as conexion:
            cursor=conexion.cursor()
            sql=f"SELECT * FROM Usuarios WHERE DNI = {dni} AND Respuesta = '{respuesta}'"
            cursor.execute(sql)
            busqueda= cursor.fetchall() # obtener respuesta como lista
            cursor.close()
            return busqueda

    def Validar_datos_usuario(self):
        dni= self.dni.get()
        respuesta=self.respuesta.get()
        busqueda = self.Buscar_usuario(dni, respuesta)
        if (busqueda != []):
            return True
        else:
            messagebox.showerror("ERROR DE RECUPERACION", "Datos de recuperacion no son correctos")

    def Restablecer_contraseña(self):
        if self.Validar_formulario_completo() and self.Validar_datos_usuario() and self.Validar_contraseña():
            query='UPDATE Usuarios SET Contraseña = (?) WHERE DNI= (?)'
            parameters = (self.nuevo_password.get(), self.dni.get())
            self.Ejecutar_consulta(query, parameters)
            messagebox.showinfo("CONTRASEÑA RECUPERADA", f'Contraseña actualizada correctamente: {self.nuevo_password.get()}')
            print('DATOS ACTUALIZADO')
            self.Limpiar_formulario()
     
    def LLamar_login(self):
        ventana_recuperar.destroy()    
        call([sys.executable, 'D:/EIGHTA/PYTHON-TKINTER/SISTEMA DESKTOP/2-Login.py', 'htmlfilename.htm'])

            
if __name__ == '__main__':
    ventana_recuperar=Tk()
    application=Producto(ventana_recuperar)
    ventana_recuperar.mainloop()