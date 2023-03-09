"""
BUSCADOR-PRODUCTOS
-Buscar  Prouctos
-Buscar en bd SQlite
"""
from tkinter import *
from tkinter import ttk
from tkinter import messagebox 
#Python image Library
from PIL import ImageTk, Image
import sqlite3


class Producto():
    db_name='database_proyecto.db'
    def __init__(self, ventana_producto):
        menubar=Menu(ventana_producto)   
        ventana_producto.title("APLICACION")
        ventana_producto.geometry("769x660")
        ventana_producto.resizable(0,0)
        ventana_producto.config(bd=10,menu=menubar)
        
        "---------------------Menu---------------------------"
        Productos=Menu(menubar,tearoff=0)
        Ventas=Menu(menubar,tearoff=0)
        Reportes=Menu(menubar,tearoff=0)
        Informacion=Menu(menubar,tearoff=0)
        menubar.add_cascade(label="Productos",menu=Productos)
        menubar.add_cascade(label="Ventas",menu=Ventas)
        menubar.add_cascade(label="Reportes",menu=Reportes)
        menubar.add_cascade(label="Ayuda",menu=Informacion)
        #Iconos
        self.img_registrar=PhotoImage(file="D:/EIGHTA/PYTHON-TKINTER/SISTEMA DESKTOP/Imagenes/registrar.png")
        self.img_buscar=PhotoImage(file="D:/EIGHTA/PYTHON-TKINTER/SISTEMA DESKTOP/Imagenes/buscar.png")
        self.img_informacion=PhotoImage(file="D:/EIGHTA/PYTHON-TKINTER/SISTEMA DESKTOP/Imagenes/informacion.png")
        #Acciones de menu
        self.boton_registrar=Productos.add_command(label="Registrar",command= self.widgets_crud,image=self.img_registrar,compound=LEFT)
        self.boton_buscar=Productos.add_command(label="Buscar",command=self.widgets_buscador,image=self.img_buscar,compound=LEFT)
        self.boton_informacion=Informacion.add_command(label="Informacion del sistema",command=self.widgets_informacion,image=self.img_informacion,compound=LEFT)
        
        "---------------------Widgets---------------------------"
        #widgets crud
        self.Label_titulo_crud=LabelFrame(ventana_producto)
        self.frame_logo_productos = LabelFrame(ventana_producto)
        self.frame_registro = LabelFrame(ventana_producto, text="Informacion del producto",font=("Comic Sans", 10,"bold"),pady=5)
        self.frame_botones_registro=LabelFrame(ventana_producto)
        self.frame_tabla_crud=LabelFrame(ventana_producto)
        #widgets buscador
        self.Label_titulo_buscador=LabelFrame(ventana_producto)
        self.frame_buscar_producto = LabelFrame(ventana_producto, text="Buscar producto",font=("Comic Sans", 10,"bold"),pady=10)
        self.frame_boton_buscar=LabelFrame(ventana_producto)
        #widgets informacion
        self.Label_informacion = LabelFrame(ventana_producto)

        #Pantalla inicial
        self.widgets_crud()

    def widgets_crud(self):
        self.Label_titulo_crud.config(bd=0)
        self.Label_titulo_crud.grid(row=0,column=0,padx=5,pady=5)
        "--------------- Titulo --------------------"
        self.titulo_crud= Label(self.Label_titulo_crud, text="REGISTRO DE PRODUCTOS ELECTRONICOS",fg="black",font=("Comic Sans", 17,"bold"))
        self.titulo_crud.grid(row=0,column=0)
        
        "--------------- Logos productos --------------------"
        self.frame_logo_productos.config(bd=0)
        self.frame_logo_productos.grid(row=1,column=0,padx=5,pady=5)

        #Logo arduino
        imagen_arduino=Image.open("D:/EIGHTA/PYTHON-TKINTER/SISTEMA DESKTOP/Imagenes/arduino-logo.png")
        nueva_imagen=imagen_arduino.resize((60,60))
        render=ImageTk.PhotoImage(nueva_imagen)
        label_imagen= Label(self.frame_logo_productos, image= render)
        label_imagen.image=render
        label_imagen.grid(row=0, column=0,padx=15,pady=5)

        #Logo nodemcu
        imagen_nodemcu=Image.open("D:/EIGHTA/PYTHON-TKINTER/SISTEMA DESKTOP/Imagenes/nodemcu-logo.png")
        nueva_imagen=imagen_nodemcu.resize((60,60))
        render=ImageTk.PhotoImage(nueva_imagen)
        label_imagen= Label(self.frame_logo_productos, image= render)
        label_imagen.image=render
        label_imagen.grid(row=0, column=1,padx=15,pady=5)
        
        #Logo raspberry
        imagen_raspberry=Image.open("D:/EIGHTA/PYTHON-TKINTER/SISTEMA DESKTOP/Imagenes/raspberry-logo.png")
        nueva_imagen=imagen_raspberry.resize((60,60))
        render=ImageTk.PhotoImage(nueva_imagen)
        label_imagen= Label(self.frame_logo_productos, image= render)
        label_imagen.image=render
        label_imagen.grid(row=0, column=2,padx=15,pady=5)
        
        "--------------- Frame marco --------------------"
        self.frame_registro.config(bd=2)
        self.frame_registro.grid(row=2,column=0,padx=5,pady=5)

        "--------------- Formulario --------------------"
        label_codigo=Label(self.frame_registro,text="Codigo del producto: ",font=("Comic Sans", 10,"bold")).grid(row=0,column=0,sticky='s',padx=5,pady=8)
        self.codigo=Entry(self.frame_registro,width=25)
        self.codigo.focus()
        self.codigo.grid(row=0, column=1, padx=5, pady=8)
        
        label_nombre=Label(self.frame_registro,text="Nombre del producto: ",font=("Comic Sans", 10,"bold")).grid(row=1,column=0,sticky='s',padx=5,pady=8)
        self.nombre=Entry(self.frame_registro,width=25)
        self.nombre.grid(row=1, column=1, padx=5, pady=8)
        
        label_categoria=Label(self.frame_registro,text="Categoria: ",font=("Comic Sans", 10,"bold")).grid(row=2,column=0,sticky='s',padx=5,pady=9)
        self.combo_categoria=ttk.Combobox(self.frame_registro,values=["Microcontrolador","Microordenador","Sensores","Accesorios"], width=22,state="readonly")
        self.combo_categoria.current(0)
        self.combo_categoria.grid(row=2,column=1,padx=5,pady=0)

        label_cantidad=Label(self.frame_registro,text="Cantidad: ",font=("Comic Sans", 10,"bold")).grid(row=0,column=2,sticky='s',padx=5,pady=8)
        self.cantidad=Entry(self.frame_registro,width=25)
        self.cantidad.grid(row=0, column=3, padx=5, pady=8)

        label_precio=Label(self.frame_registro,text="Precio (S/.): ",font=("Comic Sans", 10,"bold")).grid(row=1,column=2,sticky='s',padx=5,pady=8)
        self.precio=Entry(self.frame_registro,width=25)
        self.precio.grid(row=1, column=3, padx=5, pady=8)

        label_descripcion=Label(self.frame_registro,text="Descripcion: ",font=("Comic Sans", 10,"bold")).grid(row=2,column=2,sticky='s',padx=10,pady=8)
        self.descripcion=Entry(self.frame_registro,width=25)
        self.descripcion.grid(row=2, column=3, padx=10, pady=8)
        
        "--------------- Frame botones --------------------"
        self.frame_botones_registro.config(bd=0)
        self.frame_botones_registro.grid(row=3,column=0,padx=5,pady=5)

        "--------------- Botones --------------------"
        boton_registrar=Button(self.frame_botones_registro,text="REGISTRAR",command=self.Agregar_producto,height=2,width=12,bg="green",fg="white",font=("Comic Sans", 10,"bold")).grid(row=0, column=1, padx=10, pady=15)
        boton_editar=Button(self.frame_botones_registro,text="EDITAR",command=self.Editar_producto ,height=2,width=12,bg="gray",fg="white",font=("Comic Sans", 10,"bold")).grid(row=0, column=2, padx=10, pady=15)
        boton_eliminar=Button(self.frame_botones_registro,text="ELIMINAR",command=self.Eliminar_producto,height=2,width=12,bg="red",fg="white",font=("Comic Sans", 10,"bold")).grid(row=0, column=3, padx=10, pady=15)
        
        "--------------- Tabla --------------------"
        self.frame_tabla_crud.config(bd=2)
        self.frame_tabla_crud.grid(row=4,column=0,padx=5,pady=5)

        self.tree=ttk.Treeview(self.frame_tabla_crud,height=11, columns=("columna1","columna2","columna3","columna4","columna5"))
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
        
        self.tree.grid(row=0,column=0,sticky=E)
        
        self.Obtener_productos()
        
        #REMOVER OTROS WIDGETS
        self.widgets_buscador_remove()
        self.Label_informacion.grid_remove()

    def widgets_buscador(self):
        self.Label_titulo_buscador.config(bd=0)
        self.Label_titulo_buscador.grid(row=0,column=0,padx=5,pady=5)

        "--------------- Titulo --------------------"
        self.titulo_buscador= Label(self.Label_titulo_buscador, text="BUSCADOR DE PRODUCTOS ELECTRONICOS",fg="black",font=("Comic Sans", 17,"bold"))
        self.titulo_buscador.grid(row=0,column=0)
        
        "--------------- Frame buscar --------------------"
        self.frame_buscar_producto.config(bd=2)
        self.frame_buscar_producto.grid(row=2,column=0,padx=5,pady=5)
        
        "--------------- Formulario Buscar--------------------"
        self.label_buscar=Label(self.frame_buscar_producto,text="Buscar Por: ",font=("Comic Sans", 10,"bold")).grid(row=0,column=0,sticky='s',padx=5,pady=5)
        self.combo_buscar=ttk.Combobox(self.frame_buscar_producto,values=["Codigo","Nombre"], width=22,state="readonly")
        self.combo_buscar.current(0)
        self.combo_buscar.grid(row=0,column=1,padx=5,pady=5)

        label_codigo_codigo=Label(self.frame_buscar_producto,text="Codigo / Nombre del producto: ",font=("Comic Sans", 10,"bold")).grid(row=0,column=2,sticky='s',padx=5,pady=5)
        self.codigo_nombre=Entry(self.frame_buscar_producto,width=25)
        self.codigo_nombre.focus()
        self.codigo_nombre.grid(row=0, column=3, padx=10, pady=5)

        "--------------- Frame marco --------------------"
        self.frame_boton_buscar.config(bd=0)
        self.frame_boton_buscar.grid(row=3,column=0,padx=5,pady=5)
        "--------------- Boton --------------------"
        self.boton_buscar=Button(self.frame_boton_buscar,text="BUSCAR",command=self.Buscar_productos,height=2,width=20,bg="black",fg="white",font=("Comic Sans", 10,"bold"))
        self.boton_buscar.grid(row=0,column=0,padx=5,pady=5)

        self.tree.delete(*self.tree.get_children())

        #REMOVER OTROS WIDGETS
        self.widgets_crud_remove()
        self.Label_informacion.grid_remove()
        
    def widgets_crud_remove(self):
        self.Label_titulo_crud.grid_remove()
        self.frame_registro.grid_remove()
        self.frame_botones_registro.grid_remove()

    def widgets_buscador_remove(self):
        self.Label_titulo_buscador.grid_remove()
        self.frame_buscar_producto.grid_remove()
        self.frame_boton_buscar.grid_remove()

    def widgets_informacion(self):
        self.Label_informacion.config(bd=0)
        self.Label_informacion.grid(row=0,column=0)
        "--------------- Titulo --------------------"
        self.Label_titulo = Label(self.Label_informacion,text="APLICACION DE ESCRITORIO",fg="white",bg="black",font=("Comic Sans", 25,"bold"),padx=137,pady=20)
        self.Label_titulo.grid(row=0,column=0)

        "--------------- Logos imagenes--------------------"
        #Logo 
        imagen_arduino=Image.open("D:/EIGHTA/PYTHON-TKINTER/SISTEMA DESKTOP/Imagenes/app_logo_2.png")
        nueva_imagen=imagen_arduino.resize((170,170))
        render=ImageTk.PhotoImage(nueva_imagen)
        label_imagen= Label(self.Label_informacion, image= render)
        label_imagen.image=render
        label_imagen.grid(row=1,column=0,padx=10,pady=15)

        "--------------- opciones--------------------"
        self.Label_titulo = Label(self.Label_informacion,text="> CONTROL DE PRODUCTOS ",fg="black",font=("Comic Sans", 18,"bold"))
        self.Label_titulo.grid(row=2,column=0,sticky=W,padx=30,pady=10)

        self.Label_titulo = Label(self.Label_informacion,text="> BUSCADOR DE PRODUCTOS ",fg="black",font=("Comic Sans", 18,"bold"))
        self.Label_titulo.grid(row=3,column=0,sticky=W,padx=30,pady=10)

        self.Label_titulo = Label(self.Label_informacion,text="> REGISTRO VENTAS ",fg="black",font=("Comic Sans", 18,"bold"))
        self.Label_titulo.grid(row=4,column=0,sticky=W,padx=30,pady=10)

        self.Label_titulo = Label(self.Label_informacion,text="> GENERACION DE REPORTE ",fg="black",font=("Comic Sans", 18,"bold"))
        self.Label_titulo.grid(row=5,column=0,sticky=W,padx=30,pady=10)

        self.Label_titulo = Label(self.Label_informacion,text="Creado por Luis Ochoa - 2023",fg="black",font=("Comic Sans",10,"bold"))
        self.Label_titulo.grid(row=6,column=0,pady=60)

        #Remove
        self.widgets_buscador_remove()
        self.widgets_crud_remove()

    "--------------- CRUD --------------------"               
    def Obtener_productos(self):
        records=self.tree.get_children()
        for element in records:
            self.tree.delete(element)
        query='SELECT * FROM Productos ORDER BY Nombre desc'
        db_rows=self.Ejecutar_consulta(query)
        for row in db_rows:
            self.tree.insert("",0, text=row[1],values=(row[2],row[3],row[4],row[5],row[6]))
            
    def Agregar_producto(self):
        if self.Validar_formulario_completo() and self.Validar_registrar():
            query='INSERT INTO Productos VALUES(NULL, ?, ?, ?, ?, ?, ?)'
            parameters = (self.codigo.get(),self.nombre.get(),self.combo_categoria.get(),self.cantidad.get(),self.precio.get(),self.descripcion.get())
            self.Ejecutar_consulta(query, parameters)
            messagebox.showinfo("REGISTRO EXITOSO", f'Producto registrado: {self.nombre.get()}')
            print('REGISTRADO')
            self.Limpiar_formulario()
        self.Obtener_productos()
    
    def Eliminar_producto(self):
        try:
            self.tree.item(self.tree.selection())['text'][0]
        except IndexError as e:
            messagebox.showerror("ERROR","Porfavor selecciona un elemento") 
            return
        dato=self.tree.item(self.tree.selection())['text']
        nombre=self.tree.item(self.tree.selection())['values'][0]
        query="DELETE FROM Productos WHERE Codigo = ?"
        respuesta=messagebox.askquestion("ADVERTENCIA",f"¿Seguro que desea eliminar el producto: {nombre}?")
        if respuesta == 'yes':
            self.Ejecutar_consulta(query,(dato,))
            self.Obtener_productos()
            messagebox.showinfo('EXITO',f'Producto eliminado: {nombre}')
        else:
            messagebox.showerror('ERROR',f'Error al eliminar el producto: {nombre}')
     
    def Editar_producto(self):
        try:
            self.tree.item(self.tree.selection())['text'][0]
        except IndexError as e:
            messagebox.showerror("ERROR","Porfavor selecciona un elemento") 
            return
        codigo=self.tree.item(self.tree.selection())['text']
        nombre=self.tree.item(self.tree.selection())['values'][0]
        categoria=self.tree.item(self.tree.selection())['values'][1]
        cantidad=self.tree.item(self.tree.selection())['values'][2]
        precio=self.tree.item(self.tree.selection())['values'][3]
        descripcion=self.tree.item(self.tree.selection())['values'][4]
        
        self.Ventana_editar = Toplevel()
        self.Ventana_editar.title('EDITAR PRODUCTO')
        self.Ventana_editar.resizable(0,0)
        
        
        #Valores ventana editar
        label_codigo=Label(self.Ventana_editar,text="Codigo del producto: ",font=("Comic Sans", 10,"bold")).grid(row=0,column=0,sticky='s',padx=5,pady=8)
        nuevo_codigo=Entry(self.Ventana_editar,textvariable=StringVar(self.Ventana_editar,value=codigo),width=25)
        nuevo_codigo.grid(row=0, column=1, padx=5, pady=8)
        
        label_nombre=Label(self.Ventana_editar,text="Nombre del producto: ",font=("Comic Sans", 10,"bold")).grid(row=1,column=0,sticky='s',padx=5,pady=8)
        nuevo_nombre=Entry(self.Ventana_editar,textvariable=StringVar(self.Ventana_editar,value=nombre),width=25)
        nuevo_nombre.grid(row=1, column=1, padx=5, pady=8)
    
        label_categoria=Label(self.Ventana_editar,text="Categoria: ",font=("Comic Sans", 10,"bold")).grid(row=2,column=0,sticky='s',padx=5,pady=9)
        nuevo_combo_categoria=ttk.Combobox(self.Ventana_editar,values=["Microcontrolador","Microordenador","Sensores","Accesorios"], width=22,state="readonly")
        nuevo_combo_categoria.set(categoria)
        nuevo_combo_categoria.grid(row=2,column=1,padx=5,pady=0)

        label_cantidad=Label(self.Ventana_editar,text="Cantidad: ",font=("Comic Sans", 10,"bold")).grid(row=0,column=2,sticky='s',padx=5,pady=8)
        nueva_cantidad=Entry(self.Ventana_editar,textvariable=StringVar(self.Ventana_editar,value=cantidad),width=25)
        nueva_cantidad.grid(row=0, column=3, padx=5, pady=8)

        label_precio=Label(self.Ventana_editar,text="Precio (S/.): ",font=("Comic Sans", 10,"bold")).grid(row=1,column=2,sticky='s',padx=5,pady=8)
        nuevo_precio=Entry(self.Ventana_editar,textvariable=StringVar(self.Ventana_editar,value=precio),width=25)
        nuevo_precio.grid(row=1, column=3, padx=5, pady=8)
        
        label_descripcion=Label(self.Ventana_editar,text="Descripcion: ",font=("Comic Sans", 10,"bold")).grid(row=2,column=2,sticky='s',padx=10,pady=8)
        nueva_descripcion=Entry(self.Ventana_editar,textvariable=StringVar(self.Ventana_editar,value=descripcion),width=25)
        nueva_descripcion.grid(row=2, column=3, padx=10, pady=8)

        boton_actualizar=Button(self.Ventana_editar,text="ACTUALIZAR",command= lambda: self.Actualizar(nuevo_codigo.get(),nuevo_nombre.get(),nuevo_combo_categoria.get(),nueva_cantidad.get(),nuevo_precio.get(),nueva_descripcion.get(),codigo,nombre),height=2,width=20,bg="black",fg="white",font=("Comic Sans", 10,"bold"))
        boton_actualizar.grid(row=3, column=1,columnspan=2, padx=10, pady=15)
        
        self.Ventana_editar.mainloop()      
        
    def Actualizar(self,nuevo_codigo,nuevo_nombre,nuevo_combo_categoria,nueva_cantidad,nuevo_precio,nueva_descripcion,codigo,nombre):
        query='UPDATE Productos SET Codigo = ?, Nombre = ?, Categoria = ?, Cantidad =?, Precio=?, Descripcion =? WHERE Codigo = ? AND Nombre =?'
        parameters=(nuevo_codigo,nuevo_nombre,nuevo_combo_categoria,nueva_cantidad,nuevo_precio,nueva_descripcion,codigo,nombre)
        self.Ejecutar_consulta(query,parameters)
        messagebox.showinfo('EXITO',f'Producto actualizado:{nuevo_nombre}')
        self.Ventana_editar.destroy()
        self.Obtener_productos()

    def Buscar_productos(self):
        #Obtener todos los elementos con get_children(), que retorna una tupla de ID.
        records=self.tree.get_children()
        for element in records:
            self.tree.delete(element)
        
        if (self.combo_buscar.get()=='Codigo'):
            query=("SELECT * FROM Productos WHERE Codigo LIKE ? ") 
            parameters=(self.codigo_nombre.get()+"%")
            db_rows=self.Ejecutar_consulta(query,(parameters,))
            for row in db_rows:
                self.tree.insert("",0, text=row[1],values=(row[2],row[3],row[4],row[5],row[6]))
            if(list(self.tree.get_children())==[]):
               messagebox.showerror("ERROR","Producto no encontrado")
        else:
            query=("SELECT * FROM Productos WHERE Nombre LIKE ? ")
            parameters=("%"+self.codigo_nombre.get()+"%")
            db_rows=self.Ejecutar_consulta(query,(parameters,))
            for row in db_rows:
                self.tree.insert("",0, text=row[1],values=(row[2],row[3],row[4],row[5],row[6]))
            if(list(self.tree.get_children())==[]):
               messagebox.showerror("ERROR","Producto no encontrado")

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

    def Validar_registrar(self):
        parameters= self.codigo.get()
        query="SELECT * FROM Productos WHERE Codigo = ?"
        dato = self.Ejecutar_consulta(query,(parameters,))
        if (dato.fetchall() == []):
            return True
        else:
            messagebox.showerror("ERROR EN REGISTRO", "Codigo registrado anteriormente")

if __name__ == '__main__':
    ventana_producto=Tk()
    label_crud=Label(ventana_producto)
    application=Producto(ventana_producto)
    ventana_producto.mainloop()
