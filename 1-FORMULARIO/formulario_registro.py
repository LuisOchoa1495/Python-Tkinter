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

"--------------- Ventana --------------------"
ventana =Tk()
ventana.title("FORMULARIO DE REGISTRO")
ventana.geometry("390x480")
ventana.resizable(0,0)
ventana.config(bd=10)

"--------------- Titulo --------------------"
titulo= Label(ventana, text="REGISTRO DE USUARIO",fg="black",font=("Fixedsys", 13,"bold"),pady=10).pack()

"--------------- Marco --------------------"
marco = LabelFrame(ventana, text="Datos personales",font=("Fixedsys", 10,))
marco.config(bd=2)
marco.pack()

"--------------- Formulario --------------------"
label_dni=Label(marco,text="DNI: ",font=("Fixedsys", 10)).grid(row=0,column=0,sticky='s',padx=5,pady=10)
dni=Entry(marco,width=25).grid(row=0, column=1, padx=5, pady=10)

label_nombres=Label(marco,text="Nombre: ",font=("Fixedsys", 10)).grid(row=1,column=0,sticky='s',padx=10,pady=10)
nombres=Entry(marco,width=25).grid(row=1, column=1, padx=10, pady=10)

label_apellidos=Label(marco,text="Apellidos: ",font=("Fixedsys", 10)).grid(row=2,column=0,sticky='s',padx=10,pady=10)
apellidos=Entry(marco,width=25).grid(row=2, column=1, padx=10, pady=10)

label_sexo=Label(marco,text="Sexo: ",font=("Fixedsys", 10)).grid(row=3,column=0,sticky='s',padx=10,pady=10)
combo_sexo=ttk.Combobox(marco,values=["Masculino", "Femenino"], width=22).grid(row=3,column=1,padx=10,pady=10)

label_edad=Label(marco,text="Edad: ",font=("Fixedsys", 10)).grid(row=4,column=0,sticky='s',padx=10,pady=10)
edad=Entry(marco,width=25).grid(row=4, column=1, padx=10, pady=10)

label_correo=Label(marco,text="Correo electronico: ",font=("Fixedsys", 10)).grid(row=5,column=0,sticky='s',padx=10,pady=10)
correo=Entry(marco,width=25).grid(row=5, column=1, padx=10, pady=10)

label_password=Label(marco,text="Contraseña: ",font=("Fixedsys", 10)).grid(row=6,column=0,sticky='s',padx=10,pady=10)
password=Entry(marco,width=25,show="*").grid(row=6, column=1, padx=10, pady=10)

label_password=Label(marco,text="Repetir contraseña: ",font=("Fixedsys", 10)).grid(row=7,column=0,sticky='s',padx=10,pady=10)
repetir_password=Entry(marco,width=25,show="*").grid(row=7, column=1, padx=10, pady=10)

"--------------- Frame botones --------------------"
frame_botones=Frame(ventana)
frame_botones.pack()

"--------------- Botones --------------------"
boton_registrar=Button(frame_botones,text="REGISTRAR",command=ventana.quit ,height=2,width=10,bg="green",fg="white",font=("Fixedsys", 10)).grid(row=0, column=1, padx=10, pady=15)
boton_limpiar=Button(frame_botones,text="LIMPIAR",command=ventana.quit ,height=2,width=10,bg="gray",fg="white",font=("Fixedsys", 10)).grid(row=0, column=2, padx=10, pady=15)
boton_cancelar=Button(frame_botones,text="CERRAR",command=ventana.quit ,height=2,width=10,bg="red",fg="white",font=("Fixedsys", 10)).grid(row=0, column=3, padx=10, pady=15)

ventana.mainloop()