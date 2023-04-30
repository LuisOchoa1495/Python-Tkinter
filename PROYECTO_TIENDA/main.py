from tkinter import *
from tkinter import ttk
from tkinter import messagebox 
#Python image Library
from PIL import ImageTk, Image
import sqlite3
from datetime import datetime

class Tienda():
    db_name='tienda_diaz.db'
    def __init__(self, ventana_producto):
        menubar=Menu(ventana_producto)   
        ventana_producto.title("TIENDA DIAZ")
        ventana_producto.geometry("770x700")
        ventana_producto.resizable(0,0)
        ventana_producto.config(bd=10,menu=menubar)
        
        "---------------------Menu---------------------------"
        Productos=Menu(menubar,tearoff=0)
        Ventas=Menu(menubar,tearoff=0)
        Reportes=Menu(menubar,tearoff=0)
        Informacion=Menu(menubar,tearoff=0)
        menubar.add_cascade(label="Productos",menu=Productos)
        menubar.add_cascade(label="Ventas",menu=Ventas)
        #menubar.add_cascade(label="Reportes",menu=Reportes)
        menubar.add_cascade(label="Ayuda",menu=Informacion)
        #Iconos
        self.img_registrar=PhotoImage(file="./PROYECTO_TIENDA/img/registrar.png")
        self.img_buscar=PhotoImage(file="./PROYECTO_TIENDA/img/buscar.png")
        self.img_ventas=PhotoImage(file="./PROYECTO_TIENDA/img/ventas.png")
        self.img_nueva_venta=PhotoImage(file="./PROYECTO_TIENDA/img/nueva_venta.png")
        self.img_cliente=PhotoImage(file="./PROYECTO_TIENDA/img/cliente.png")
        self.img_codigo=PhotoImage(file="./PROYECTO_TIENDA/img/codigo.png")
        self.img_informacion=PhotoImage(file="./PROYECTO_TIENDA/img/informacion.png")
        #Acciones de menu
        self.boton_registrar=Productos.add_command(label="Registrar",command= self.widgets_crud,image=self.img_registrar,compound=LEFT)
        self.boton_buscar=Productos.add_command(label="Buscar",command=self.widgets_buscador,image=self.img_buscar,compound=LEFT)
        self.boton_nueva_venta=Ventas.add_command(label="Nueva Venta",command=self.widgets_nueva_venta,image=self.img_nueva_venta,compound=LEFT)        
        self.boton_ventas=Ventas.add_command(label="Ventas",command=self.widgets_ventas,image=self.img_ventas,compound=LEFT)        
        self.boton_cliente=Ventas.add_command(label="Clientes",command=self.widgets_cliente,image=self.img_cliente,compound=LEFT)        
        self.boton_informacion=Informacion.add_command(label="Codigo Producto",command=self.widgets_codigos,image=self.img_codigo,compound=LEFT)
        self.boton_informacion=Informacion.add_command(label="Informacion del sistema",command=self.widgets_informacion,image=self.img_informacion,compound=LEFT)
        
        "---------------------Widgets---------------------------"
        #widgets crud
        self.frame_logo_productos = LabelFrame(ventana_producto)
        self.frame_registro = LabelFrame(ventana_producto, text="Registrar producto",font=("Comic Sans", 10,"bold"),pady=5)
        self.frame_botones_registro=LabelFrame(ventana_producto)
        self.frame_tabla_crud=LabelFrame(ventana_producto)
        #widgets buscador
        self.frame_buscar_producto = LabelFrame(ventana_producto, text="Buscar producto",font=("Comic Sans", 10,"bold"),pady=10)
        self.frame_boton_buscar=LabelFrame(ventana_producto)
        self.frame_tabla_buscador=LabelFrame(ventana_producto)
        #widgets nueva ventas
        self.frame_dni_venta=LabelFrame(ventana_producto)
        self.frame_nueva_venta = LabelFrame(ventana_producto,text="Nueva venta",font=("Comic Sans", 10,"bold"),pady=10)
        self.frame_finalizar_venta=LabelFrame(ventana_producto)
        self.frame_tabla_nueva_venta=LabelFrame(ventana_producto)
        #widgets ventas
        self.frame_buscar_ventas = LabelFrame(ventana_producto,text="Buscar venta",font=("Comic Sans", 10,"bold"),pady=10)
        self.frame_boton_buscar_ventas=LabelFrame(ventana_producto)
        self.frame_tabla_ventas=LabelFrame(ventana_producto)
        #widgets cliente
        self.frame_nuevo_cliente = LabelFrame(ventana_producto,text="Nuevo Cliente",font=("Comic Sans", 10,"bold"),pady=10)
        self.frame_botones_registro_cliente = LabelFrame(ventana_producto)
        self.frame_buscar_cliente = LabelFrame(ventana_producto,text="Buscar Cliente",font=("Comic Sans", 10,"bold"),pady=10)
        self.frame_tabla_clientes=LabelFrame(ventana_producto)
        #Codigos productos
        self.frame_codigo = LabelFrame(ventana_producto)
        #widgets informacion
        self.Label_informacion = LabelFrame(ventana_producto)

        #Pantalla inicial
        self.widgets_crud()

    "--------------- WIDGETS--------------------"  
    def widgets_crud(self):
        "--------------- Logos tienda --------------------"
        self.frame_logo_productos.config(bd=0)
        self.frame_logo_productos.grid(row=0,column=0,padx=5,pady=5)

        #Logo 
        imagen=Image.open("./PROYECTO_TIENDA/img/logo-tienda.png")
        nueva_imagen=imagen.resize((320,150))
        render=ImageTk.PhotoImage(nueva_imagen)
        label_imagen= Label(self.frame_logo_productos, image= render)
        label_imagen.image=render
        label_imagen.grid(row=0, column=0)
        
        "--------------- Frame marco registro --------------------"
        self.frame_registro.config(bd=2)
        self.frame_registro.grid(row=1,column=0,padx=5,pady=5)

        "--------------- Formulario --------------------"
        label_codigo=Label(self.frame_registro,text="Codigo del producto: ",font=("Comic Sans", 10,"bold")).grid(row=0,column=0,sticky='s',padx=5,pady=8)
        self.codigo=Entry(self.frame_registro,width=25)
        self.codigo.focus()
        self.codigo.grid(row=0, column=1, padx=5, pady=8)
        
        label_nombre=Label(self.frame_registro,text="Nombre del producto: ",font=("Comic Sans", 10,"bold")).grid(row=1,column=0,sticky='s',padx=5,pady=8)
        self.nombre=Entry(self.frame_registro,width=25)
        self.nombre.grid(row=1, column=1, padx=5, pady=8)
        
        label_categoria=Label(self.frame_registro,text="Categoria: ",font=("Comic Sans", 10,"bold")).grid(row=2,column=0,sticky='s',padx=5,pady=9)
        self.combo_categoria=ttk.Combobox(self.frame_registro,values=["Componentes","Perifericos"], width=22,state="readonly")
        self.combo_categoria.current(0)
        self.combo_categoria.grid(row=2,column=1,padx=5,pady=0)

        label_cantidad=Label(self.frame_registro,text="Cantidad: ",font=("Comic Sans", 10,"bold")).grid(row=0,column=2,sticky='s',padx=5,pady=8)
        self.cantidad=Entry(self.frame_registro,width=25)
        self.cantidad.grid(row=0, column=3, padx=5, pady=8)

        label_precio=Label(self.frame_registro,text="Precio ($): ",font=("Comic Sans", 10,"bold")).grid(row=1,column=2,sticky='s',padx=5,pady=8)
        self.precio=Entry(self.frame_registro,width=25)
        self.precio.grid(row=1, column=3, padx=5, pady=8)

        label_descripcion=Label(self.frame_registro,text="Descripcion: ",font=("Comic Sans", 10,"bold")).grid(row=2,column=2,sticky='s',padx=10,pady=8)
        self.descripcion=Entry(self.frame_registro,width=25)
        self.descripcion.grid(row=2, column=3, padx=10, pady=8)
        
        "--------------- Frame botones --------------------"
        self.frame_botones_registro.config(bd=0)
        self.frame_botones_registro.grid(row=2,column=0,padx=5,pady=5)

        "--------------- Botones --------------------"
        boton_registrar=Button(self.frame_botones_registro,text="REGISTRAR",command=self.Agregar_producto,height=2,width=12,bg="green",fg="white",font=("Comic Sans", 10,"bold")).grid(row=0, column=1, padx=10, pady=10)
        boton_editar=Button(self.frame_botones_registro,text="EDITAR",command=self.Editar_producto ,height=2,width=12,bg="gray",fg="white",font=("Comic Sans", 10,"bold")).grid(row=0, column=2, padx=10, pady=10)
        boton_eliminar=Button(self.frame_botones_registro,text="ELIMINAR",command=self.Eliminar_producto,height=2,width=12,bg="red",fg="white",font=("Comic Sans", 10,"bold")).grid(row=0, column=3, padx=10, pady=10)
        
        "--------------- Tabla --------------------"
        self.frame_tabla_crud.config(bd=2)
        self.frame_tabla_crud.grid(row=3,column=0,padx=5,pady=5)

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
        self.widgets_informacion_remove()
        self.widgets_cliente_remove()
        self.widgets_codigos_remove()
        self.widgets_ventas_remove()
        self.widgets_nueva_venta_remove()

    def widgets_buscador(self):
        
        "--------------- Frame marco buscar --------------------"
        self.frame_buscar_producto.config(bd=2)
        self.frame_buscar_producto.grid(row=1,column=0,padx=5,pady=5)
        
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
        self.frame_boton_buscar.grid(row=2,column=0,padx=5,pady=5)
        "--------------- Boton --------------------"
        self.boton_buscar=Button(self.frame_boton_buscar,text="BUSCAR",command=self.Buscar_productos,height=2,width=20,bg="black",fg="white",font=("Comic Sans", 10,"bold"))
        self.boton_buscar.grid(row=0,column=0,padx=5,pady=5)

        "--------------- Tabla --------------------"
        self.frame_tabla_buscador.config(bd=2)
        self.frame_tabla_buscador.grid(row=3,column=0,padx=5,pady=5)

        self.tree_buscar=ttk.Treeview(self.frame_tabla_buscador,height=11, columns=("columna1","columna2","columna3","columna4","columna5"))
        self.tree_buscar.heading("#0",text='Codigo', anchor=CENTER)
        self.tree_buscar.column("#0", width=90, minwidth=75, stretch=NO)
        
        self.tree_buscar.heading("columna1",text='Nombre', anchor=CENTER)
        self.tree_buscar.column("columna1", width=150, minwidth=75, stretch=NO)
        
        self.tree_buscar.heading("columna2",text='Categoria', anchor=CENTER)
        self.tree_buscar.column("columna2", width=150, minwidth=75, stretch=NO)
                
        self.tree_buscar.heading("columna3",text='Cantidad', anchor=CENTER)
        self.tree_buscar.column("columna3", width=70, minwidth=60, stretch=NO)
        
        self.tree_buscar.heading("columna4",text='Precio', anchor=CENTER)
        self.tree_buscar.column("columna4", width=70, minwidth=60, stretch=NO)
        
        self.tree_buscar.heading("columna5",text='Descripcion', anchor=CENTER)
        
        self.tree_buscar.grid(row=0,column=0,sticky=E)
        self.Obtener_productos()
        self.tree_buscar.delete(*self.tree_buscar.get_children())

        #REMOVER OTROS WIDGETS
        self.widgets_crud_remove()
        self.widgets_informacion_remove()
        self.widgets_cliente_remove()
        self.widgets_codigos_remove()
        self.widgets_ventas_remove()
        self.widgets_nueva_venta_remove()

    def widgets_cliente(self):
        
        "--------------- Frame marco buscar --------------------"
        self.frame_nuevo_cliente.config(bd=2)
        self.frame_nuevo_cliente.grid(row=1,column=0,padx=5,pady=5)
        
        "--------------- Registrar cliente --------------------"
        self.label_dni=Label(self.frame_nuevo_cliente,text="DNI: ",font=("Comic Sans", 10,"bold")).grid(row=0,column=0,sticky='s',padx=5,pady=5)
        self.dni=Entry(self.frame_nuevo_cliente,width=25)
        self.dni.focus()
        self.dni.grid(row=0,column=1,padx=5,pady=5)

        self.label_nombres=Label(self.frame_nuevo_cliente,text="Nombres: ",font=("Comic Sans", 10,"bold")).grid(row=1,column=0,sticky='s',padx=5,pady=5)
        self.nombres=Entry(self.frame_nuevo_cliente,width=25)
        self.nombres.grid(row=1, column=1, padx=10, pady=5)

        self.label_apellidos=Label(self.frame_nuevo_cliente,text="Apellidos: ",font=("Comic Sans", 10,"bold")).grid(row=2,column=0,sticky='s',padx=5,pady=5)
        self.apellidos=Entry(self.frame_nuevo_cliente,width=25)
        self.apellidos.grid(row=2, column=1, padx=10, pady=5)

        self.label_telefono=Label(self.frame_nuevo_cliente,text="Telefono: ",font=("Comic Sans", 10,"bold")).grid(row=0,column=2,sticky='s',padx=5,pady=5)
        self.telefono=Entry(self.frame_nuevo_cliente,width=25)
        self.telefono.grid(row=0, column=3, padx=10, pady=5)

        self.label_email=Label(self.frame_nuevo_cliente,text="E-mail: ",font=("Comic Sans", 10,"bold")).grid(row=1,column=2,sticky='s',padx=5,pady=5)
        self.email=Entry(self.frame_nuevo_cliente,width=25)
        self.email.grid(row=1, column=3, padx=10, pady=5)

        self.label_direccion=Label(self.frame_nuevo_cliente,text="Direccion: ",font=("Comic Sans", 10,"bold")).grid(row=2,column=2,sticky='s',padx=5,pady=5)
        self.direccion=Entry(self.frame_nuevo_cliente,width=30)
        self.direccion.grid(row=2, column=3, padx=10, pady=5)

        "--------------- Frame botones --------------------"
        self.boton_registrar=Button(self.frame_nuevo_cliente,text="REGISTRAR",command=self.Agregar_cliente,height=1,width=15,bg="green",fg="white",font=("Comic Sans", 10,"bold"))
        self.boton_registrar.grid(row=0,column=4,padx=10,pady=5)

        self.boton_editar=Button(self.frame_nuevo_cliente,text="EDITAR",command=self.Editar_cliente,height=1,width=15,bg="gray",fg="white",font=("Comic Sans", 10,"bold"))
        self.boton_editar.grid(row=1,column=4,padx=10,pady=5)

        self.boton_eliminar=Button(self.frame_nuevo_cliente,text="ELIMINAR",command=self.Eliminar_cliente,height=1,width=15,bg="red",fg="white",font=("Comic Sans", 10,"bold"))
        self.boton_eliminar.grid(row=2,column=4,padx=10,pady=5)
        
        "--------------- Tabla --------------------"
        self.frame_tabla_clientes.config(bd=2)
        self.frame_tabla_clientes.grid(row=2,column=0,padx=5,pady=5)

        self.tree_cliente=ttk.Treeview(self.frame_tabla_clientes,height=11, columns=("columna1","columna2","columna3","columna4","columna5"))
        self.tree_cliente.heading("#0",text='DNI', anchor=CENTER)
        self.tree_cliente.column("#0", width=90, minwidth=75, stretch=NO)
        
        self.tree_cliente.heading("columna1",text='Nombre', anchor=CENTER)
        self.tree_cliente.column("columna1", width=150, minwidth=75, stretch=NO)
        
        self.tree_cliente.heading("columna2",text='Apellidos', anchor=CENTER)
        self.tree_cliente.column("columna2", width=150, minwidth=75, stretch=NO)
                
        self.tree_cliente.heading("columna3",text='Telefono', anchor=CENTER)
        self.tree_cliente.column("columna3", width=70, minwidth=60, stretch=NO)
        
        self.tree_cliente.heading("columna4",text='E-mail', anchor=CENTER)
        self.tree_cliente.column("columna4", width=70, minwidth=60, stretch=NO)
        
        self.tree_cliente.heading("columna5",text='Direccion', anchor=CENTER)

        self.tree_cliente.grid(row=0,column=0,sticky=E)
        self.Obtener_clientes()
        #self.tree_cliente.delete(*self.tree_cliente.get_children())

        "--------------- Frame buscar --------------------"
        self.frame_buscar_cliente.config(bd=2)
        self.frame_buscar_cliente.grid(row=4,column=0,padx=5,pady=5)
        "--------------- Buscar cliente --------------------"
        self.label_buscar_cliente=Label(self.frame_buscar_cliente,text="DNI: ",font=("Comic Sans", 10,"bold")).grid(row=0,column=0,sticky='s',padx=20,pady=10)
        self.buscar_dni=Entry(self.frame_buscar_cliente,width=30)
        self.buscar_dni.grid(row=0, column=1, padx=30, pady=5)
        self.boton_buscar=Button(self.frame_buscar_cliente,text="BUSCAR",command=self.Buscar_cliente,height=1,width=15,bg="black",fg="white",font=("Comic Sans", 10,"bold"))
        self.boton_buscar.grid(row=0,column=2,padx=30,pady=5)

        self.widgets_buscador_remove()
        self.widgets_crud_remove()
        self.widgets_informacion_remove()
        self.widgets_codigos_remove()
        self.widgets_ventas_remove()
        self.widgets_nueva_venta_remove()

    def widgets_codigos(self):
        self.frame_codigo.config(bd=0)
        self.frame_codigo.grid(row=0,column=0)
        imagen=Image.open("./PROYECTO_TIENDA/img/codigos.png")
        nueva_imagen=imagen.resize((750,650))
        render=ImageTk.PhotoImage(nueva_imagen)
        label_imagen= Label(self.frame_codigo, image= render)
        label_imagen.image=render
        label_imagen.grid(row=0,column=0)

        self.widgets_buscador_remove()
        self.widgets_crud_remove()
        self.widgets_cliente_remove()
        self.widgets_informacion_remove()
        self.widgets_ventas_remove()
        self.widgets_nueva_venta_remove()

    def widgets_informacion(self):

        self.Label_informacion.config(bd=0)
        self.Label_informacion.grid(row=0,column=0)
        "--------------- Titulo --------------------"
        self.Label_titulo = Label(self.Label_informacion,text="APLICACION DE ESCRITORIO",fg="white",bg="black",font=("Comic Sans", 23,"bold"),padx=150,pady=20)
        self.Label_titulo.grid(row=0,column=0)

        "--------------- Logos imagenes--------------------"
        #Logo 
        imagen=Image.open("./PROYECTO_TIENDA/img/app_logo_2.png")
        nueva_imagen=imagen.resize((170,170))
        render=ImageTk.PhotoImage(nueva_imagen)
        label_imagen= Label(self.Label_informacion, image= render)
        label_imagen.image=render
        label_imagen.grid(row=1,column=0,padx=10,pady=15)

        "--------------- opciones--------------------"
        self.Label_titulo = Label(self.Label_informacion,text="> CONTROL DE PRODUCTOS ",fg="black",font=("Comic Sans", 16,"bold"))
        self.Label_titulo.grid(row=2,column=0,sticky=W,padx=30,pady=10)

        self.Label_titulo = Label(self.Label_informacion,text="> BUSCADOR DE PRODUCTOS ",fg="black",font=("Comic Sans", 16,"bold"))
        self.Label_titulo.grid(row=3,column=0,sticky=W,padx=30,pady=10)

        self.Label_titulo = Label(self.Label_informacion,text="> REGISTRO VENTAS ",fg="black",font=("Comic Sans", 16,"bold"))
        self.Label_titulo.grid(row=4,column=0,sticky=W,padx=30,pady=10)

        self.Label_titulo = Label(self.Label_informacion,text="> GENERACION DE REPORTE ",fg="black",font=("Comic Sans", 16,"bold"))
        self.Label_titulo.grid(row=5,column=0,sticky=W,padx=30,pady=10)

        self.Label_titulo = Label(self.Label_informacion,text="Creado por Emiliano Diaz - 2023",fg="black",font=("Comic Sans",12,"bold"))
        self.Label_titulo.grid(row=6,column=0,pady=85)
        
        #Remove
        self.widgets_buscador_remove()
        self.widgets_crud_remove()
        self.widgets_cliente_remove()
        self.widgets_codigos_remove()
        self.widgets_ventas_remove()
        self.widgets_nueva_venta_remove()

    def widgets_nueva_venta(self):
        "--------------- Frame marco dni_ventas --------------------"
        self.frame_dni_venta.config(bd=1)
        self.frame_dni_venta.grid(row=1,column=0,padx=5,pady=5)

        label_dni_venta=Label(self.frame_dni_venta,text="DNI: ",font=("Comic Sans", 10,"bold")).grid(row=0,column=0,sticky='s',padx=5,pady=5)
        self.dni_venta=Entry(self.frame_dni_venta,width=25)
        self.dni_venta.focus()
        self.dni_venta.grid(row=0, column=1, padx=10, pady=5)

        label_medio_pago=Label(self.frame_dni_venta,text="Medio de pago: ",font=("Comic Sans", 10,"bold")).grid(row=0,column=2,sticky='s',padx=5,pady=5)
        self.combo_medio_pago=ttk.Combobox(self.frame_dni_venta,values=["Efectivo","Tarjeta","Transferencia"], width=22,state="readonly")
        self.combo_medio_pago.current(0)
        self.combo_medio_pago.grid(row=0,column=3,padx=5,pady=5)

        "--------------- Frame marco nueva venta --------------------"
        self.frame_nueva_venta.config(bd=2)
        self.frame_nueva_venta.grid(row=2,column=0,padx=5,pady=5)

        label_codigo_producto_venta=Label(self.frame_nueva_venta,text="Codigo: ",font=("Comic Sans", 10,"bold")).grid(row=0,column=0,sticky='s',padx=5,pady=5)
        self.codigo_producto_venta=Entry(self.frame_nueva_venta,width=25)
        self.codigo_producto_venta.focus()
        self.codigo_producto_venta.grid(row=0, column=1, padx=10, pady=5)

        label_cantidad_producto_venta=Label(self.frame_nueva_venta,text="Cantidad: ",font=("Comic Sans", 10,"bold")).grid(row=1,column=0,sticky='s',padx=5,pady=5)
        self.cantidad_producto_venta=Entry(self.frame_nueva_venta,width=25)
        self.cantidad_producto_venta.grid(row=1, column=1, padx=10, pady=5)

        self.boton_agregar_producto_venta=Button(self.frame_nueva_venta,text="AGREGAR",command=self.Agregar_producto_venta,height=1,width=15,bg="green",fg="white",font=("Comic Sans", 10,"bold"))
        self.boton_agregar_producto_venta.grid(row=0,column=2,padx=5,pady=5)

        self.boton_eliminar_producto_venta=Button(self.frame_nueva_venta,text="ELIMINAR",command=self.Eliminar_producto_venta,height=1,width=15,bg="red",fg="white",font=("Comic Sans", 10,"bold"))
        self.boton_eliminar_producto_venta.grid(row=1,column=2,padx=5,pady=5)

        "--------------- Tabla --------------------"
        self.frame_tabla_nueva_venta.config(bd=2)
        self.frame_tabla_nueva_venta.grid(row=3,column=0,padx=5,pady=5)

        self.tree_nueva_venta=ttk.Treeview(self.frame_tabla_nueva_venta,height=11, columns=("columna1","columna2","columna3","columna4","columna5"))
        self.tree_nueva_venta.heading("#0",text='Codigo', anchor=CENTER)
        self.tree_nueva_venta.column("#0", width=90, minwidth=75, stretch=NO)
        
        self.tree_nueva_venta.heading("columna1",text='Producto', anchor=CENTER)
        self.tree_nueva_venta.column("columna1", width=150, minwidth=75, stretch=NO)
        
        self.tree_nueva_venta.heading("columna2",text='Descripcion', anchor=CENTER)
        self.tree_nueva_venta.column("columna2", width=150, minwidth=75, stretch=NO)
                
        self.tree_nueva_venta.heading("columna3",text='Precio', anchor=CENTER)
        self.tree_nueva_venta.column("columna3", width=70, minwidth=60, stretch=NO)
        
        self.tree_nueva_venta.heading("columna4",text='Cantidad', anchor=CENTER)
        self.tree_nueva_venta.column("columna4", width=70, minwidth=60, stretch=NO)

        self.tree_nueva_venta.heading("columna5",text='Subtotal', anchor=CENTER)

        self.tree_nueva_venta.grid(row=0,column=0,sticky=E)

        "--------------- Finalizar venta --------------------"
        self.frame_finalizar_venta.config(bd=1)
        self.frame_finalizar_venta.grid(row=4,column=0,padx=5,pady=5,sticky=E)

        self.boton_finalizar_venta=Button(self.frame_finalizar_venta,text="Finalizar venta",command=self.Finalizar_venta,height=2,width=15,bg="black",fg="white",font=("Comic Sans", 12,"bold"))
        self.boton_finalizar_venta.grid(row=0,column=0,padx=5,pady=5)       

        label_venta_total=Label(self.frame_finalizar_venta,text="Venta total ($): ",font=("Comic Sans", 12,"bold")).grid(row=0,column=1,padx=5,pady=5)
        self.venta_total=Label(self.frame_finalizar_venta,text="0.00",font=("Comic Sans", 12,"bold"),height=1,width=10,bg="blue",fg="white")
        self.venta_total.grid(row=0, column=2, padx=10, pady=5)

        self.widgets_crud_remove()
        self.widgets_codigos_remove()
        self.widgets_buscador_remove()
        self.widgets_informacion_remove()
        self.widgets_cliente_remove()
        self.widgets_ventas_remove()  
          
    def widgets_ventas(self):
        "--------------- Frame marco ventas --------------------"
        self.frame_buscar_ventas.config(bd=2)
        self.frame_buscar_ventas.grid(row=1,column=0,padx=5,pady=5)
        
        "--------------- Formulario Buscar ventas--------------------"
        self.label_buscar_venta=Label(self.frame_buscar_ventas,text="Buscar Por: ",font=("Comic Sans", 10,"bold")).grid(row=0,column=0,sticky='s',padx=5,pady=5)
        self.combo_buscar_venta=ttk.Combobox(self.frame_buscar_ventas,values=["DNI","Fecha"], width=22,state="readonly")
        self.combo_buscar_venta.current(0)
        self.combo_buscar_venta.grid(row=0,column=1,padx=5,pady=5)

        label_dni_fecha=Label(self.frame_buscar_ventas,text="DNI / Fecha: ",font=("Comic Sans", 10,"bold")).grid(row=0,column=2,sticky='s',padx=5,pady=5)
        self.dni_fecha=Entry(self.frame_buscar_ventas,width=25)
        self.dni_fecha.focus()
        self.dni_fecha.grid(row=0, column=3, padx=10, pady=5)

        "--------------- Frame marco ventas--------------------"
        self.frame_boton_buscar_ventas.config(bd=0)
        self.frame_boton_buscar_ventas.grid(row=2,column=0,padx=5,pady=5)
        "--------------- Boton --------------------"
        self.boton_buscar_ventas=Button(self.frame_boton_buscar_ventas,text="BUSCAR",command=self.Buscar_venta,height=2,width=20,bg="black",fg="white",font=("Comic Sans", 10,"bold"))
        self.boton_buscar_ventas.grid(row=0,column=0,padx=5,pady=5)

        "--------------- Tabla --------------------"
        self.frame_tabla_ventas.config(bd=2)
        self.frame_tabla_ventas.grid(row=3,column=0,padx=5,pady=5)

        self.tree_buscar_ventas=ttk.Treeview(self.frame_tabla_ventas,height=11, columns=("columna1","columna2","columna3","columna4","columna5"))
        self.tree_buscar_ventas.heading("#0",text='Fecha', anchor=CENTER)
        self.tree_buscar_ventas.column("#0", width=150, minwidth=75, stretch=NO)
        
        self.tree_buscar_ventas.heading("columna1",text='DNI', anchor=CENTER)
        self.tree_buscar_ventas.column("columna1", width=90, minwidth=60, stretch=NO)
        
        self.tree_buscar_ventas.heading("columna2",text='Nombres', anchor=CENTER)
        self.tree_buscar_ventas.column("columna2", width=90, minwidth=60, stretch=NO)
                
        self.tree_buscar_ventas.heading("columna3",text='Apellidos', anchor=CENTER)
        self.tree_buscar_ventas.column("columna3", width=90, minwidth=60, stretch=NO)
        
        self.tree_buscar_ventas.heading("columna4",text='Medio de pago', anchor=CENTER)
        self.tree_buscar_ventas.column("columna4", width=110, minwidth=75, stretch=NO)
        
        self.tree_buscar_ventas.heading("columna5",text='Venta total', anchor=CENTER)

        self.tree_buscar_ventas.grid(row=0,column=0,sticky=E)

        self.widgets_crud_remove()
        self.widgets_codigos_remove()
        self.widgets_buscador_remove()
        self.widgets_informacion_remove()
        self.widgets_cliente_remove()
        self.widgets_nueva_venta_remove()

    "--------------- WIDGETS REMOVE --------------------" 
    def widgets_crud_remove(self):
        self.frame_registro.grid_remove()
        self.frame_botones_registro.grid_remove()
        self.frame_tabla_crud.grid_remove()

    def widgets_buscador_remove(self):
        self.frame_buscar_producto.grid_remove()
        self.frame_boton_buscar.grid_remove()
        self.frame_tabla_buscador.grid_remove()

    def widgets_informacion_remove(self):
        self.Label_informacion.grid_remove()

    def widgets_cliente_remove(self):
        self.frame_nuevo_cliente.grid_remove()
        self.frame_buscar_cliente.grid_remove()
        self.frame_tabla_clientes.grid_remove()

    def widgets_codigos_remove(self):
        self.frame_codigo.grid_remove()

    def widgets_ventas_remove(self):
        self.frame_buscar_ventas.grid_remove()
        self.frame_boton_buscar_ventas.grid_remove()
        self.frame_tabla_ventas.grid_remove()

    def widgets_nueva_venta_remove(self):
        self.frame_dni_venta.grid_remove()
        self.frame_nueva_venta.grid_remove()
        self.frame_tabla_nueva_venta.grid_remove()
        self.frame_finalizar_venta.grid_remove()
    "--------------- CRUD --------------------"               
    def Obtener_productos(self):
        records=self.tree.get_children()
        for element in records:
            self.tree.delete(element)
        query='SELECT * FROM Productos ORDER BY id_producto asc'
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
        nuevo_combo_categoria=ttk.Combobox(self.Ventana_editar,values=["Componentes","Perifericos"], width=22,state="readonly")
        nuevo_combo_categoria.set(categoria)
        nuevo_combo_categoria.grid(row=2,column=1,padx=5,pady=0)

        label_cantidad=Label(self.Ventana_editar,text="Cantidad: ",font=("Comic Sans", 10,"bold")).grid(row=0,column=2,sticky='s',padx=5,pady=8)
        nueva_cantidad=Entry(self.Ventana_editar,textvariable=StringVar(self.Ventana_editar,value=cantidad),width=25)
        nueva_cantidad.grid(row=0, column=3, padx=5, pady=8)

        label_precio=Label(self.Ventana_editar,text="Precio ($): ",font=("Comic Sans", 10,"bold")).grid(row=1,column=2,sticky='s',padx=5,pady=8)
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
        if(self.Validar_busqueda()):
            #Obtener todos los elementos con get_children(), que retorna una tupla de ID.
            records=self.tree_buscar.get_children()
            for element in records:
                self.tree_buscar.delete(element)
            if (self.combo_buscar.get()=='Codigo'):
                query=("SELECT * FROM Productos WHERE Codigo LIKE ? ") 
                parameters=(self.codigo_nombre.get()+"%")
                db_rows=self.Ejecutar_consulta(query,(parameters,))
                for row in db_rows:
                    self.tree_buscar.insert("",0, text=row[1],values=(row[2],row[3],row[4],row[5],row[6]))
                if(list(self.tree.get_children())==[]):
                    messagebox.showerror("ERROR","Producto no encontrado")
            else:
                query=("SELECT * FROM Productos WHERE Nombre LIKE ? ")
                parameters=("%"+self.codigo_nombre.get()+"%")
                db_rows=self.Ejecutar_consulta(query,(parameters,))
                for row in db_rows:
                    self.tree_buscar.insert("",0, text=row[1],values=(row[2],row[3],row[4],row[5],row[6]))
                if(list(self.tree.get_children())==[]):
                    messagebox.showerror("ERROR","Producto no encontrado")

    "--------------- OTRAS FUNCIONES PRODUCTOS--------------------"
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
    
    def Validar_busqueda(self):
        if len(self.codigo_nombre.get()) !=0:
            return True
        else:
             self.tree.delete(*self.tree.get_children())
             messagebox.showerror("ERROR", "Complete todos los campos para la busqueda") 

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

    "--------------- CLIENTES--------------------"
    def Obtener_clientes(self):
        records=self.tree_cliente.get_children()
        for element in records:
            self.tree_cliente.delete(element)
        query='SELECT * FROM Clientes'
        db_rows=self.Ejecutar_consulta(query)
        for row in db_rows:
            self.tree_cliente.insert("",0, text=row[0],values=(row[1],row[2],row[3],row[4],row[5]))
            
    def Agregar_cliente(self):
        if self.Validar_formulario_completo_cliente() and self.Validar_registrar_cliente():
            query='INSERT INTO Clientes VALUES(?, ?, ?, ?, ?, ?)'
            parameters = (self.dni.get(),self.nombres.get(),self.apellidos.get(),self.telefono.get(),self.email.get(),self.direccion.get())
            self.Ejecutar_consulta(query, parameters)
            messagebox.showinfo("REGISTRO EXITOSO", f'Cliente registrado: {self.dni.get()}')
            print('REGISTRADO')
            self.Limpiar_formulario_cliente()
        self.Obtener_clientes()

    def Eliminar_cliente(self):
        try:
            self.tree_cliente.item(self.tree_cliente.selection())['text']
        except IndexError as e:
            messagebox.showerror("ERROR","Porfavor selecciona un elemento") 
            return
        dato=self.tree_cliente.item(self.tree_cliente.selection())['text']
        nombre=self.tree_cliente.item(self.tree_cliente.selection())['values'][1]
        query="DELETE FROM Clientes WHERE DNI = ?"
        respuesta=messagebox.askquestion("ADVERTENCIA",f"¿Seguro que desea eliminar el cliente: {dato} - {nombre}?")
        if respuesta == 'yes':
            self.Ejecutar_consulta(query,(dato,))
            self.Obtener_clientes()
            messagebox.showinfo('EXITO',f'Cliente eliminado: {dato} - {nombre}')
        else:
            messagebox.showerror('ERROR',f'Error al eliminar el producto: {dato} - {nombre}')

    def Editar_cliente(self):
        try:
            self.tree_cliente.item(self.tree_cliente.selection())['text']
        except IndexError as e:
            messagebox.showerror("ERROR","Porfavor selecciona un elemento") 
            return
        dni=self.tree_cliente.item(self.tree_cliente.selection())['text']
        nombres=self.tree_cliente.item(self.tree_cliente.selection())['values'][0]
        apellidos=self.tree_cliente.item(self.tree_cliente.selection())['values'][1]
        telefono=self.tree_cliente.item(self.tree_cliente.selection())['values'][2]
        email=self.tree_cliente.item(self.tree_cliente.selection())['values'][3]
        direccion=self.tree_cliente.item(self.tree_cliente.selection())['values'][4]
        
        self.Ventana_editar_cliente = Toplevel()
        self.Ventana_editar_cliente.title('EDITAR CLIENTE')
        self.Ventana_editar_cliente.resizable(0,0)
        
        #Valores ventana editar
        label_dni=Label(self.Ventana_editar_cliente,text="DNI: ",font=("Comic Sans", 10,"bold")).grid(row=0,column=0,sticky='s',padx=5,pady=8)
        nuevo_dni=Entry(self.Ventana_editar_cliente,textvariable=StringVar(self.Ventana_editar_cliente,value=dni),width=25)
        nuevo_dni.grid(row=0, column=1, padx=5, pady=8)
        
        label_nombres=Label(self.Ventana_editar_cliente,text="Nombres: ",font=("Comic Sans", 10,"bold")).grid(row=1,column=0,sticky='s',padx=5,pady=8)
        nuevo_nombres=Entry(self.Ventana_editar_cliente,textvariable=StringVar(self.Ventana_editar_cliente,value=nombres),width=25)
        nuevo_nombres.grid(row=1, column=1, padx=5, pady=8)
    
        label_apellidos=Label(self.Ventana_editar_cliente,text="Apellidos: ",font=("Comic Sans", 10,"bold")).grid(row=2,column=0,sticky='s',padx=5,pady=9)
        nuevo_apellidos=Entry(self.Ventana_editar_cliente,textvariable=StringVar(self.Ventana_editar_cliente,value=apellidos),width=25)
        nuevo_apellidos.grid(row=2,column=1,padx=5,pady=0)

        label_telefono=Label(self.Ventana_editar_cliente,text="Telefono: ",font=("Comic Sans", 10,"bold")).grid(row=0,column=2,sticky='s',padx=5,pady=8)
        nueva_telefono=Entry(self.Ventana_editar_cliente,textvariable=StringVar(self.Ventana_editar_cliente,value=telefono),width=25)
        nueva_telefono.grid(row=0, column=3, padx=5, pady=8)

        label_email=Label(self.Ventana_editar_cliente,text="E-mail: ",font=("Comic Sans", 10,"bold")).grid(row=1,column=2,sticky='s',padx=5,pady=8)
        nuevo_email=Entry(self.Ventana_editar_cliente,textvariable=StringVar(self.Ventana_editar_cliente,value=email),width=25)
        nuevo_email.grid(row=1, column=3, padx=5, pady=8)
        
        label_direccion=Label(self.Ventana_editar_cliente,text="Direccion: ",font=("Comic Sans", 10,"bold")).grid(row=2,column=2,sticky='s',padx=10,pady=8)
        nueva_direccion=Entry(self.Ventana_editar_cliente,textvariable=StringVar(self.Ventana_editar_cliente,value=direccion),width=25)
        nueva_direccion.grid(row=2, column=3, padx=10, pady=8)

        boton_actualizar_cliente=Button(self.Ventana_editar_cliente,text="ACTUALIZAR",command= lambda: self.Actualizar_cliente(nuevo_dni.get(),nuevo_nombres.get(),nuevo_apellidos.get(),nueva_telefono.get(),nuevo_email.get(),nueva_direccion.get(),dni,nombres),height=2,width=20,bg="black",fg="white",font=("Comic Sans", 10,"bold"))
        boton_actualizar_cliente.grid(row=3, column=1,columnspan=2, padx=10, pady=15)
        
        self.Ventana_editar_cliente.mainloop()      
        
    def Actualizar_cliente(self,nuevo_dni,nuevo_nombres,nuevo_apelllidos,nueva_telefono,nuevo_email,nueva_direccion,dni,nombres):
        query='UPDATE Clientes SET DNI = ?, Nombres = ?, Apellidos = ?, Telefono =?, Email=?, Direccion =? WHERE DNI = ? AND Nombres =?'
        parameters=(nuevo_dni,nuevo_nombres,nuevo_apelllidos,nueva_telefono,nuevo_email,nueva_direccion,dni,nombres)
        self.Ejecutar_consulta(query,parameters)
        messagebox.showinfo('EXITO',f'Cliente actualizado:{nuevo_dni}')
        self.Ventana_editar_cliente.destroy()
        self.Obtener_clientes()

    def Buscar_cliente(self):
        if(self.Validar_busqueda_cliente()):
            #Obtener todos los elementos con get_children(), que retorna una tupla de ID.
            records=self.tree_cliente.get_children()
            for element in records:
                #self.tree_cliente.delete(element)
                query=("SELECT * FROM Clientes WHERE DNI LIKE ? ") 
                parameters=(self.buscar_dni.get()+"%")
                db_rows=self.Ejecutar_consulta(query,(parameters,))
                for row in db_rows:
                    self.tree_cliente.delete(*self.tree_cliente.get_children())
                    self.tree_cliente.insert("",0, text=row[0],values=(row[1],row[2],row[3],row[4],row[5]))
                if(list(self.tree_cliente.get_children())==[]):
                    messagebox.showerror("ERROR","Cliente no encontrado")
        
    "--------------- OTRAS FUNCIONES CLIENTES--------------------"
    def Validar_formulario_completo_cliente(self):
        if len(self.dni.get()) !=0 and len(self.nombres.get()) !=0 and len(self.apellidos.get()) !=0 and len(self.telefono.get()) !=0 and len(self.email.get()) !=0 and len(self.direccion.get()) !=0:
            return True
        else:
             messagebox.showerror("ERROR", "Complete todos los campos del formulario")

    def Validar_registrar_cliente(self):
        parameters= self.dni.get()
        query="SELECT * FROM Clientes WHERE DNI = ?"
        dato = self.Ejecutar_consulta(query,(parameters,))
        if (dato.fetchall() == []):
            return True
        else:
            messagebox.showerror("ERROR EN REGISTRO", "DNI registrado anteriormente")

    def Limpiar_formulario_cliente(self):
        self.dni.delete(0, END)
        self.nombres.delete(0, END)
        self.apellidos.delete(0, END)
        self.telefono.delete(0, END)
        self.email.delete(0, END)
        self.direccion.delete(0, END) 

    def Validar_busqueda_cliente(self):
        if len(self.buscar_dni.get()) !=0:
            return True
        else:
             self.tree_cliente.delete(*self.tree_cliente.get_children())
             messagebox.showerror("ERROR", "Complete todos los campos para la busqueda") 

    "--------------- VENTAS--------------------"
    def Agregar_producto_venta(self):
        codigo_busqueda=self.codigo_producto_venta.get()
        cantidad=self.cantidad_producto_venta.get()
        if(self.Validar_busqueda_producto_venta()):
            query=("SELECT Codigo,Nombre,Descripcion,Precio FROM Productos WHERE Codigo LIKE ?") 
            parameters=(codigo_busqueda)
            db_rows=self.Ejecutar_consulta(query,(parameters,))
            rows=db_rows.fetchall()
            subtotal=(float(rows[0][3])*float(cantidad))
            rows.extend([cantidad,subtotal])
            print(rows[2])
            self.tree_nueva_venta.insert("",0, text=rows[0][0],values=(rows[0][1],rows[0][2],rows[0][3],rows[1],rows[2]))
            self.Limpiar_nueva_venta()
            self.Suma_total_venta()

    def Finalizar_venta(self):
        fecha=datetime.now()
        formato_fecha=fecha.strftime('%d/%m/%Y  %H:%M:%S')
        print(self.monto_total)
        
        query='INSERT INTO Ventas VALUES(NULL, ?, ?, ?,?)'
        parameters = (self.dni_venta.get(),formato_fecha,self.combo_medio_pago.get(),self.monto_total)
        print('REGISTRADO')
        respuesta=messagebox.askquestion("ADVERTENCIA",f"¿Seguro que desea terminar la venta?")
        if respuesta == 'yes':
            self.Ejecutar_consulta(query, parameters)
            messagebox.showinfo("VENTA FINALIZADA", f'Monto total de ven: {self.monto_total}')
            self.Limpiar_venta_finalizada()
        else:
            messagebox.showerror('ERROR',f'Error al eliminar el producto')
    
    def Buscar_venta(self):
        if(self.Validar_busqueda_ventas()):
            #Obtener todos los elementos con get_children(), que retorna una tupla de ID.
            records=self.tree_buscar_ventas.get_children()
            for element in records:
                self.tree_buscar_ventas.delete(element)
            if (self.combo_buscar_venta.get()=='DNI'):
                query=("SELECT Fecha,DNI,Clientes.Nombres,Clientes.Apellidos , Medio_pago, Total FROM Ventas INNER JOIN Clientes on Ventas.dni_cliente=Clientes.DNI WHERE DNI LIKE ? ") 
                parameters=(self.dni_fecha.get()+"%")
                db_rows=self.Ejecutar_consulta(query,(parameters,))
                for row in db_rows:
                    self.tree_buscar_ventas.insert("",0, text=row[0],values=(row[1],row[2],row[3],row[4],row[5]))
                if(list(self.tree_buscar_ventas.get_children())==[]):
                    messagebox.showerror("ERROR","Ventas no encontradas")
            else:
                query=("SELECT Fecha,DNI,Clientes.Nombres,Clientes.Apellidos , Medio_pago, Total FROM Ventas INNER JOIN Clientes on Ventas.dni_cliente=Clientes.DNI WHERE Fecha LIKE ? ")
                parameters=("%"+self.dni_fecha.get()+"%")
                db_rows=self.Ejecutar_consulta(query,(parameters,))
                for row in db_rows:
                    self.tree_buscar_ventas.insert("",0, text=row[0],values=(row[1],row[2],row[3],row[4],row[5]))
                if(list(self.tree_buscar_ventas.get_children())==[]):
                    messagebox.showerror("ERROR","Ventas no encontradas")

    "--------------- OTRAS FUNCIONES CLIENTES--------------------"
    def Validar_busqueda_producto_venta(self):
        if len(self.codigo_producto_venta.get()) !=0 and len(self.cantidad_producto_venta.get()) !=0 :
            return True
        else:
                #self.tree_cliente.delete(*self.tree_cliente.get_children())
                messagebox.showerror("ERROR", "Complete todos los campos") 

    def Suma_total_venta(self):
        self.monto_total = 0.00
        for item in self.tree_nueva_venta.get_children():    
            celda = float(self.tree_nueva_venta.set(item, "columna5"))
            self.monto_total += celda
        self.venta_total.config(text=self.monto_total)
    
    def Eliminar_producto_venta(self):
        try:
            item=self.tree_nueva_venta.selection()
        except IndexError as e:
            messagebox.showerror("ERROR","Porfavor selecciona un elemento") 
            return
        respuesta=messagebox.askquestion("ADVERTENCIA",f"¿Seguro que desea eliminar el producto?")
        if respuesta == 'yes':
            self.tree_nueva_venta.delete(item)
            messagebox.showinfo('EXITO',f'Producto eliminado')
            self.Suma_total_venta()
        else:
            messagebox.showerror('ERROR',f'Error al eliminar el producto')

    def Limpiar_nueva_venta(self):
        self.codigo_producto_venta.delete(0,END)
        self.cantidad_producto_venta.delete(0,END)

    def Limpiar_venta_finalizada(self):
        self.dni_venta.delete(0,END)
        records=self.tree_nueva_venta.get_children()
        for element in records:
            self.tree_nueva_venta.delete(element)

    def Validar_busqueda_ventas(self):
        if len(self.dni_fecha.get()) !=0:
            return True
        else:
             self.tree_buscar_ventas.delete(*self.tree_buscar_ventas.get_children())
             messagebox.showerror("ERROR", "Complete todos los campos para la busqueda") 

if __name__ == '__main__':
    ventana_producto=Tk()
    label_crud=Label(ventana_producto)
    application=Tienda(ventana_producto)
    ventana_producto.mainloop()
