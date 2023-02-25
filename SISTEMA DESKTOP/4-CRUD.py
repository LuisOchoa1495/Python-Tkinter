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
    
    def __init__(self, ventana_producto):
        self.window=ventana_producto   
        self.window.title("APLICACION")
        self.window.geometry("800x720")
        self.window.resizable(0,0)
        self.window.config(bd=10)
        
        "--------------- Titulo --------------------"
        titulo= Label(ventana_producto, text="REGISTRO DE PRODUCTOS ELECTRONICOS",fg="black",font=("Comic Sans", 17,"bold"),pady=10).pack()

        "--------------- Logos productos --------------------"
        frame_logo_productos = LabelFrame(ventana_producto)
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
        marco = LabelFrame(ventana_producto, text="Informacion del producto",font=("Comic Sans", 10,"bold"),pady=5)
        marco.config(bd=2)
        marco.pack()

        "--------------- Formulario --------------------"
        label_codigo=Label(marco,text="Codigo del producto: ",font=("Comic Sans", 10,"bold")).grid(row=0,column=0,sticky='s',padx=5,pady=8)
        self.codigo=Entry(marco,width=25)
        self.codigo.focus()
        self.codigo.grid(row=0, column=1, padx=5, pady=8)
        
        label_nombre=Label(marco,text="Nombre del producto: ",font=("Comic Sans", 10,"bold")).grid(row=1,column=0,sticky='s',padx=5,pady=8)
        self.nombre=Entry(marco,width=25)
        self.nombre.grid(row=1, column=1, padx=5, pady=8)
        
        label_categoria=Label(marco,text="Categoria: ",font=("Comic Sans", 10,"bold")).grid(row=2,column=0,sticky='s',padx=5,pady=9)
        self.combo_categoria=ttk.Combobox(marco,values=["Microcontrolador","Microordenador","Sensores","Accesorios"], width=22,state="readonly")
        self.combo_categoria.current(0)
        self.combo_categoria.grid(row=2,column=1,padx=5,pady=0)


        label_cantidad=Label(marco,text="Cantidad: ",font=("Comic Sans", 10,"bold")).grid(row=0,column=2,sticky='s',padx=5,pady=8)
        self.cantidad=Entry(marco,width=25)
        self.cantidad.grid(row=0, column=3, padx=5, pady=8)

        label_precio=Label(marco,text="Precio (S/.): ",font=("Comic Sans", 10,"bold")).grid(row=1,column=2,sticky='s',padx=5,pady=8)
        self.precio=Entry(marco,width=25)
        self.precio.grid(row=1, column=3, padx=5, pady=8)

        label_descripcion=Label(marco,text="Descripcion: ",font=("Comic Sans", 10,"bold")).grid(row=2,column=2,sticky='s',padx=10,pady=8)
        self.descripcion=Text(marco,width=25,height=2)
        self.descripcion.grid(row=2, column=3,rowspan=10, padx=10, pady=8)

        "--------------- Frame botones --------------------"
        frame_botones=Frame(ventana_producto)
        frame_botones.pack()

        "--------------- Botones --------------------"
        boton_registrar=Button(frame_botones,text="REGISTRAR",command=self.Agregar_producto,height=2,width=10,bg="green",fg="white",font=("Comic Sans", 10,"bold")).grid(row=0, column=1, padx=10, pady=15)
        boton_editar=Button(frame_botones,text="EDITAR",command=ventana_producto.quit ,height=2,width=10,bg="gray",fg="white",font=("Comic Sans", 10,"bold")).grid(row=0, column=2, padx=10, pady=15)
        boton_eliminar=Button(frame_botones,text="ELIMINAR",command=ventana_producto.quit,height=2,width=10,bg="red",fg="white",font=("Comic Sans", 10,"bold")).grid(row=0, column=3, padx=10, pady=15)

        "--------------- Tabla --------------------"    
        self.tree=ttk.Treeview(height=13, columns=("columna1","columna2","columna3","columna4","columna5"))
        self.tree.heading("#0",text='Codigo', anchor=CENTER)
        self.tree.column("#0", width=90, minwidth=75, stretch=NO)
        
        self.tree.heading("columna1",text='Nombre', anchor=CENTER)
        self.tree.column("columna1", width=150, minwidth=75, stretch=NO)
        
        self.tree.heading("columna2",text='Categoria', anchor=CENTER)
        self.tree.column("columna2", width=150, minwidth=75, stretch=NO)
                
        self.tree.heading("columna3",text='Cantidad', anchor=CENTER)
        self.tree.column("columna3", width=70, minwidth=60, stretch=NO)
        
        self.tree.heading("columna4",text='Precio', anchor=CENTER)
        self.tree.column("columna4", width=70, minwidth=60, stretch=NO)
        
        self.tree.heading("columna5",text='Descripcion', anchor=CENTER)
        
        self.tree.pack()
        
        "--------------- Boton actualizar --------------------"   
        Button(ventana_producto,text="ACTUALIZAR LISTA",command=self.Obtener_producto ,height=2,width=20,bg="black",fg="white",font=("Comic Sans", 10,"bold")).pack(side=BOTTOM)
    
    "--------------- CRUD --------------------"               
    def Obtener_producto(self):
        records=self.tree.get_children()
        for element in records:
            self.tree.delete(element)
        query='SELECT * FROM Productos ORDER BY Nombre desc'
        db_rows=self.Ejecutar_consulta(query)
        for row in db_rows:
            self.tree.insert("",0, text=row[1],values=(row[2],row[3],row[4],row[5],row[6]))
            
    def Agregar_producto(self):
        if self.Validar_formulario_completo():
            query='INSERT INTO Productos VALUES(NULL, ?, ?, ?, ?, ?, ?)'
            parameters = (self.codigo.get(),self.nombre.get(),self.combo_categoria.get(),self.cantidad.get(),self.precio.get(),self.descripcion.get())
            self.Ejecutar_consulta(query, parameters)
            messagebox.showinfo("REGISTRO EXITOSO", f'Producto registrado: {self.nombre.get()}')
            print('REGISTRADO')
            self.Limpiar_formulario()
            self.Obtener_producto()
            
    "--------------- OTRAS FUNCIONES --------------------"
    def Ejecutar_consulta(self, query, parameters=()):
        with sqlite3.connect(self.db_name) as conexion:
            cursor=conexion.cursor()
            result=cursor.execute(query,parameters)
            conexion.commit()
        return result   
               
    def Validar_formulario_completo(self):
        if len(self.codigo.get()) !=0 and len(self.nombre.get()) !=0 and len(self.combo_categoria.get()) !=0 and len(self.cantidad.get()) !=0 and len(self.precio.get()) !=0 and len(self.descripcion.get()) !=0:
            return True
        else:
             messagebox.showerror("ERROR", "Complete todos los campos del formulario") 
    
    def Limpiar_formulario(self):
        self.codigo.delete(0, END)
        self.nombre.delete(0, END)
        self.cantidad.delete(0, END)
        self.precio.delete(0, END)
        self.descripcion.delete(0, END)       
             
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
      
if __name__ == '__main__':
    ventana_producto=Tk()
    application=Producto(ventana_producto)
    ventana_producto.mainloop()