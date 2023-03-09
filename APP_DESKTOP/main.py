"""
FORMULARIO DE LOGIN
Ingresar al sistema con su dni y contraseña
Mostrar messagebox
"""
from tkinter import *
from tkinter import ttk
from tkinter import messagebox 
#Python image Library
from PIL import ImageTk, Image
import sqlite3
from Buscador import *

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

        "--------------- Loginlogo --------------------"
        imagen_login=Image.open("D:/EIGHTA/PYTHON-TKINTER/SISTEMA DESKTOP/Imagenes/login.png")
        nueva_imagen=imagen_login.resize((40,40))
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
        self.dni_login=Entry(marco,width=25)
        self.dni_login.focus()
        self.dni_login.grid(row=0, column=1, padx=5, pady=10)

        label_nombres=Label(marco,text="Contraseña: ",font=("Comic Sans", 10,"bold")).grid(row=1,column=0,sticky='s',padx=10,pady=10)
        self.password_login=Entry(marco,width=25,show="*")
        self.password_login.grid(row=1, column=1, padx=10, pady=10)
        
        "--------------- Frame botones --------------------"
        frame_botones=Frame(ventana_login)
        frame_botones.pack()

        "--------------- Botones --------------------"
        boton_ingresar=Button(frame_botones,text="INGRESAR",command=self.Login,height=2,width=12,bg="green",fg="white",font=("Comic Sans", 10,"bold")).grid(row=0, column=1, padx=10, pady=15)
        boton_registrar=Button(frame_botones,text="REGISTRAR",command=self.Ventana_registrar_usuario,height=2,width=12,bg="blue",fg="white",font=("Comic Sans", 10,"bold")).grid(row=0, column=2, padx=10, pady=15)
        label_=Label(frame_botones,text="⬇ ¿Olvido su contraseña? ⬇",font=("Comic Sans", 10,"bold")).grid(row=1,column=1,columnspan=2,sticky='s')
        boton_olvido=Button(frame_botones,text="RECUPERAR CONTRASEÑA",command=self.Ventana_recuperar_password ,height=2,width=24,bg="gray",fg="white",font=("Comic Sans", 10,"bold")).grid(row=2, column=1, columnspan=2, padx=10, pady=8)
    
    def Validar_login(self, dni, password):
        with sqlite3.connect(self.db_name) as conexion:
            cursor=conexion.cursor()
            sql= f"SELECT * FROM Usuarios WHERE DNI = {dni} AND Contraseña = '{password}'"
            cursor.execute(sql)
            validacion= cursor.fetchall() # obtener respuesta como lista
            cursor.close()
            return validacion
        
    def Validar_formulario_completo(self):
        if len(self.dni_login.get()) !=0 and len(self.password_login.get()) !=0:
            return True
        else:
             messagebox.showerror("ERROR DE INGRESO", "Ingrese su DNI y contraseña!!!")
        self.Limpiar_login()    
    
    def Limpiar_login(self):
            self.dni_login.delete(0, END)
            self.password_login.delete(0, END)

    def Login(self):
        try:
            if(self.Validar_formulario_completo()):
                dni= self.dni_login.get()
                password= self.password_login.get()
                dato = self.Validar_login(dni, password)
                if (dato != []):
                    #Producto.__init__(ventana_login)
                    messagebox.showinfo("BIENVENIDO", "Datos ingresados correctamente") 
                else:
                    messagebox.showerror("ERROR DE INGRESO", "DNI o contraseña incorrecto") 
                self.Limpiar_login()
        except:
            messagebox.showerror("ERROR", "Ha ocurrido un error, reinicie el programa")
            self.Limpiar_login()
    "--------------------------------------------- REGISTRAR USUARIO --------------------------------------------------"
    def Ventana_registrar_usuario(self):
        self.Ventana_registrar=Toplevel()
        self.Ventana_registrar.title("FORMULARIO DE REGISTRO")
        self.Ventana_registrar.geometry("390x630")
        self.Ventana_registrar.resizable(0,0)
        self.Ventana_registrar.config(bd=10)
        
        "--------------- Titulo --------------------"
        titulo= Label(self.Ventana_registrar, text="REGISTRO DE USUARIO",fg="black",font=("Comic Sans", 13,"bold"),pady=5).pack()

        "--------------- Nuevo usuario logo --------------------"
        imagen_registro=Image.open("D:/EIGHTA/PYTHON-TKINTER/SISTEMA DESKTOP/Imagenes/nuevo_usuario.png")
        nueva_imagen=imagen_registro.resize((40,40))
        render=ImageTk.PhotoImage(nueva_imagen)
        label_imagen= Label(self.Ventana_registrar, image= render)
        label_imagen.image=render
        label_imagen.pack(pady=5)


        "--------------- Marco --------------------"
        marco = LabelFrame(self.Ventana_registrar, text="Datos personales",font=("Comic Sans", 10,"bold"))
        marco.config(bd=2,pady=5)
        marco.pack()

        "--------------- Formulario --------------------"
        label_dni=Label(marco,text="DNI: ",font=("Comic Sans", 10,"bold")).grid(row=0,column=0,sticky='s',padx=5,pady=8)
        self.dni=Entry(marco,width=25)
        self.dni.focus()
        self.dni.grid(row=0, column=1, padx=5, pady=8)

        label_nombres=Label(marco,text="Nombre: ",font=("Comic Sans", 10,"bold")).grid(row=1,column=0,sticky='s',padx=10,pady=8)
        self.nombres=Entry(marco,width=25)
        self.nombres.grid(row=1, column=1, padx=10, pady=8)

        label_apellidos=Label(marco,text="Apellidos: ",font=("Comic Sans", 10,"bold")).grid(row=2,column=0,sticky='s',padx=10,pady=8)
        self.apellidos=Entry(marco,width=25)
        self.apellidos.grid(row=2, column=1, padx=10, pady=8)

        label_sexo=Label(marco,text="Sexo: ",font=("Comic Sans", 10,"bold")).grid(row=3,column=0,sticky='s',padx=10,pady=8)
        self.combo_sexo=ttk.Combobox(marco,values=["Masculino", "Femenino"], width=22,state="readonly")
        self.combo_sexo.current(0)
        self.combo_sexo.grid(row=3,column=1,padx=10,pady=8)

        label_edad=Label(marco,text="Edad: ",font=("Comic Sans", 10,"bold")).grid(row=4,column=0,sticky='s',padx=10,pady=8)
        self.edad=Entry(marco,width=25)
        self.edad.grid(row=4, column=1, padx=10, pady=8)

        label_correo=Label(marco,text="Correo electronico: ",font=("Comic Sans", 10,"bold")).grid(row=5,column=0,sticky='s',padx=10,pady=8)
        self.correo=Entry(marco,width=25)
        self.correo.grid(row=5, column=1, padx=10, pady=8)

        label_password=Label(marco,text="Contraseña: ",font=("Comic Sans", 10,"bold")).grid(row=6,column=0,sticky='s',padx=10,pady=8)
        self.password=Entry(marco,width=25,show="*")
        self.password.grid(row=6, column=1, padx=10, pady=8)

        label_password=Label(marco,text="Repetir contraseña: ",font=("Comic Sans", 10,"bold")).grid(row=7,column=0,sticky='s',padx=10,pady=8)
        self.repetir_password=Entry(marco,width=25,show="*")
        self.repetir_password.grid(row=7, column=1, padx=10, pady=8)
        
        "--------------- Marco pregunta --------------------"
        marco_pregunta = LabelFrame(self.Ventana_registrar, text="Si olvidas tu contraseña",font=("Comic Sans", 10,"bold"),pady=10)
        marco_pregunta.config(bd=2,pady=5)
        marco_pregunta.pack()
        "--------------- Pregunta --------------------"
        label_pregunta=Label(marco_pregunta,text="Pregunta: ",font=("Comic Sans", 10,"bold")).grid(row=0,column=0,sticky='s',padx=10,pady=8)
        self.combo_pregunta=ttk.Combobox(marco_pregunta,values=["¿Nombre de tu primera mascota?","¿Lugar dónde fuiste al colegio?","¿En que ciudad naciste?","¿Cómo se llama tu equipo favorito?"], width=30,state="readonly")
        self.combo_pregunta.current(0)
        self.combo_pregunta.grid(row=0,column=1,padx=10,pady=8)
  
        label_respuesta=Label(marco_pregunta,text="Respuesta: ",font=("Comic Sans", 10,"bold")).grid(row=1,column=0,sticky='s',padx=10,pady=8)
        self.respuesta=Entry(marco_pregunta,width=33)
        self.respuesta.grid(row=1, column=1, padx=10, pady=8)        
        
        label_nota=Label(marco_pregunta,text="*Esta respuesta te permitira recuperar tu contraseña.",font=("Comic Sans", 9,"bold"),foreground="blue").grid(row=2,column=0,columnspan=2,sticky='s',padx=10)

        "--------------- Frame botones --------------------"
        frame_botones=Frame(self.Ventana_registrar)
        frame_botones.pack()

        "--------------- Botones --------------------"
        boton_registrar=Button(frame_botones,text="REGISTRAR",command=self.Registrar_usuario ,height=2,width=10,bg="green",fg="white",font=("Comic Sans", 10,"bold")).grid(row=0, column=1, padx=10, pady=15)
        boton_limpiar=Button(frame_botones,text="LIMPIAR",command=self.Limpiar_formulario_registro ,height=2,width=10,bg="gray",fg="white",font=("Comic Sans", 10,"bold")).grid(row=0, column=2, padx=10, pady=15)
        boton_cancelar=Button(frame_botones,text="CERRAR",command=self.Ventana_registrar.destroy ,height=2,width=10,bg="red",fg="white",font=("Comic Sans", 10,"bold")).grid(row=0, column=3, padx=10, pady=15)

        self.Ventana_registrar.mainloop()

    def Ejecutar_consulta(self, query, parameters=()):
        with sqlite3.connect(self.db_name) as conexion:
            cursor=conexion.cursor()
            result=cursor.execute(query,parameters)
            conexion.commit()
        return result 
    
    def Limpiar_formulario_registro(self):
            self.dni.delete(0, END)
            self.nombres.delete(0, END)
            self.apellidos.delete(0, END)
            self.combo_sexo.delete(0, END)
            self.edad.delete(0, END)
            self.correo.delete(0, END)
            self.password.delete(0, END)
            self.repetir_password.delete(0, END)
            self.combo_pregunta.delete(0, END)
            self.respuesta.delete(0, END)
        
    def Validar_formulario_completo_registro(self):
        if len(self.dni.get()) !=0 and len(self.nombres.get()) !=0 and len(self.apellidos.get()) !=0 and len(self.combo_sexo.get()) !=0 and len(self.edad.get()) !=0 and len(self.password.get()) !=0 and len(self.repetir_password.get()) !=0 and len(self.correo.get()) !=0 and len(self.respuesta.get()) !=0:
            return True
        else:
             messagebox.showerror("ERROR EN REGISTRO", "Complete todos los campos del formulario")

    def Validar_contraseña_registro(self):
        if(str(self.password.get()) == str(self.repetir_password.get())):
            return True
        else:
            messagebox.showerror("ERROR EN REGISTRO", "Contraseñas no coinciden")
 
    def Buscar_dni(self, dni):
        with sqlite3.connect(self.db_name) as conexion:
            cursor=conexion.cursor()
            sql="SELECT * FROM Usuarios WHERE DNI = {}".format(dni)
            cursor.execute(sql)
            dnix= cursor.fetchall() # obtener respuesta como lista
            cursor.close()
            return dnix
    
    def Validar_dni(self):
        dni= self.dni.get()
        dato = self.Buscar_dni(dni)
        if (dato == []):
            return True
        else:
            messagebox.showerror("ERROR EN REGISTRO", "DNI registrado anteriormente")

    def Registrar_usuario(self):
        if self.Validar_formulario_completo_registro() and self.Validar_contraseña_registro() and self.Validar_dni():
            query='INSERT INTO Usuarios VALUES(NULL, ?, ?, ?, ?, ?, ?, ?, ?)'
            parameters = (self.dni.get(),self.nombres.get(),self.apellidos.get(),self.combo_sexo.get(),self.edad.get(),self.correo.get(),self.password.get(),self.respuesta.get())
            self.Ejecutar_consulta(query, parameters)
            messagebox.showinfo("REGISTRO EXITOSO", f'Bienvenido {self.nombres.get()} {self.apellidos.get()}')
            print('USUARIO CREADO')
            self.Limpiar_formulario_registro()

    "--------------------------------------------- RECUPERAR CONTRASEÑA --------------------------------------------------"  
    def Ventana_recuperar_password(self):
        self.Ventana_recuperar = Toplevel()
        self.Ventana_recuperar.geometry("410x420")
        self.Ventana_recuperar.title('RECUPERAR CONTRASEÑA')
        self.Ventana_recuperar.resizable(0,0)
        self.Ventana_recuperar.config(bd=10)

        "--------------- Titulo --------------------"
        titulo= Label(self.Ventana_recuperar, text="RECUPERAR CONTRASEÑA",fg="black",font=("Comic Sans", 13,"bold"),pady=8).pack()

        "--------------- Recuperar password logo --------------------"
        imagen_password=Image.open("D:/EIGHTA/PYTHON-TKINTER/SISTEMA DESKTOP/Imagenes/recuperar_contraseña.png")
        nueva_imagen=imagen_password.resize((60,60))
        render=ImageTk.PhotoImage(nueva_imagen)
        label_imagen= Label(self.Ventana_recuperar, image= render)
        label_imagen.image=render
        label_imagen.pack(pady=5)

        "--------------- Marco --------------------"
        marco = LabelFrame(self.Ventana_recuperar, text="Datos de recuperacion",font=("Comic Sans", 10,"bold"))
        marco.config(bd=2)
        marco.pack()

        "--------------- Formulario --------------------"
        label_dni=Label(marco,text="DNI: ",font=("Comic Sans", 10,"bold")).grid(row=0,column=0,sticky='s',padx=5,pady=8)
        self.dni=Entry(marco,width=25)
        self.dni.focus()
        self.dni.grid(row=0, column=1, padx=5, pady=8)
        
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
        frame_botones=Frame(self.Ventana_recuperar)
        frame_botones.pack()

        "--------------- Botones --------------------"
        boton_recuperar=Button(frame_botones,text="RECUPERAR",command=self.Restablecer_contraseña ,height=2,width=10,bg="green",fg="white",font=("Comic Sans", 10,"bold")).grid(row=0, column=1, padx=10, pady=10)
        boton_cancelar=Button(frame_botones,text="CANCELAR",command=self.Ventana_recuperar.destroy ,height=2,width=10,bg="red",fg="white",font=("Comic Sans", 10,"bold")).grid(row=0, column=3, padx=10, pady=10)

        self.Ventana_recuperar.mainloop()

    def Limpiar_formulario_recuperar(self):
        self.dni.delete(0, END)
        self.respuesta.delete(0, END)
        self.nuevo_password.delete(0, END)
        self.repetir_password.delete(0, END)     
        
    def Validar_formulario_completo_recuperar(self):
        if len(self.dni.get()) !=0 and len(self.nuevo_password.get()) !=0 and len(self.repetir_password.get()) !=0 and len(self.respuesta.get()) !=0:
            return True
        else:
             messagebox.showerror("ERROR", "Complete todos los campos del formulario")
             
    def Validar_contraseña_recuperar(self):
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
        if self.Validar_formulario_completo_recuperar() and self.Validar_datos_usuario() and self.Validar_contraseña_recuperar():
            query='UPDATE Usuarios SET Contraseña = (?) WHERE DNI= (?)'
            parameters = (self.nuevo_password.get(), self.dni.get())
            self.Ejecutar_consulta(query, parameters)
            messagebox.showinfo("CONTRASEÑA RECUPERADA", f'Contraseña actualizada correctamente: {self.nuevo_password.get()}')
            print('DATOS ACTUALIZADO')
            self.Limpiar_formulario_recuperar()
            self.Ventana_recuperar.destroy()

#verificar si el modulo ha sido ejecutado correctamente  
if __name__ == '__main__':
    ventana_login=Tk()
    application=Login(ventana_login)
    ventana_login.mainloop()

