# Importar librería
import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import colorchooser
### Importar librería para los menús
from tkinter import Menu
# Importa librería para las cajas de mensajes
from tkinter import messagebox
from tkinter import messagebox as mBox

def cerrar_aplicacion():
    if messagebox.askokcancel("Cerrar la aplicación", "¿Seguro que deseas cerrar la Aplicación?\n\n*Optar por favor*"):
        ventana.destroy()

#ventana pared
def pared():
    pared = Toplevel(ventana)
    pared.title("Pared")
    pared.geometry("1300x650+10+10")
    pared.resizable(0, 0)  # Para evitar modificar el tamaño de una ventana
    pared.iconbitmap("casa.ico")
    pared.config(bg="blue")

    ### imagenes Formulario
    imagen2 = PhotoImage(file="pared.png")
    fondo2 = Label(pared, width=120,height=120, image=imagen2).place(x=1130,y=100)
    
    def pared1():
        alturaP1=float(alturaP.get())
        largoP1=float(largoP.get())
        resultado=(alturaP1*1)*(largoP1*1)
        presupuesto=(resultado*800)
        agua=30*resultado
        arena=0.125*resultado
        ladrillos=46*resultado
        corceplas=2*resultado
        cemento=1*resultado
        etiqueta4 = Label(pared, text=(resultado), font=("Courier",15),bg="black",fg="white").place(x=780, y=180)
        etiqueta6 = Label(pared, text=(presupuesto), font=("Courier",15),bg="black",fg="white").place(x=780, y=230)
        etiqueta18 = Label(pared, text=("litros de agua:",agua), font=("Courier",12),bg="black",fg="white").place(x=780, y=370)
        etiqueta13 = Label(pared, text=("arena colorada:",arena), font=("Courier",12),bg="black",fg="white").place(x=780, y=410)
        etiqueta14 = Label(pared, text=("ladrillos:",ladrillos), font=("Courier",12),bg="black",fg="white").place(x=780, y=450)
        etiqueta15 = Label(pared, text=("corceplas:",corceplas), font=("Courier",12),bg="black",fg="white").place(x=780, y=490)
        etiqueta16 = Label(pared, text=("cemento:",cemento), font=("Courier",12),bg="black",fg="white").place(x=780, y=530)
#etiquetas y botones
    etiqueta = Label(pared, text="Pared", font=("Courier",32), bg="white").place(x=580, y=30)
    etiqueta1 = Label(pared, text="Ingrese la altura de pared: ").place(x=410, y=120)
    alturaP=tk.DoubleVar()
    combo=Entry(pared,textvariable=alturaP).place(x=780, y=120)
    etiqueta2 = Label(pared, text="Ingrese largo de pared: ").place(x=410, y=150)
    largoP=tk.DoubleVar()
    combo2=Entry(pared,textvariable=largoP).place(x=780, y=150)
    etiqueta3 = Label(pared, text="Resultado: ").place(x=410, y=180)
    etiqueta5 = Label(pared, text="Precio del Presupuesto: ").place(x=410, y=230)
    Button(pared, text="Calcular", fg="#17202A", bg="#FF8000", relief="ridge", borderwidth=5, command=pared1 , width=12, font=("Arial",12)).place(x=1130,y=250)
    etiqueta17 = Label(pared, text="Materiales para M2", font=("Courier",16), bg="white").place(x=220, y=330)
    etiqueta7 = Label(pared, text="30 litros de agua", font=("Courier",12), bg="white").place(x=220, y=370)
    etiqueta8 = Label(pared, text="1/8 M3 de arena colorada", font=("Courier",12), bg="white").place(x=220, y=410)
    etiqueta9 = Label(pared, text="46 ladrillos", font=("Courier",12), bg="white").place(x=220, y=450)
    etiqueta10 = Label(pared, text="2 baldes de corceplas", font=("Courier",12), bg="white").place(x=220, y=490)
    etiqueta11 = Label(pared, text="1 balde de cemento", font=("Courier",12), bg="white").place(x=220, y=530)
    etiqueta12 = Label(pared, text="Cantidad de Materiales", font=("Courier",16),bg="black",fg="white").place(x=780, y=330)
     
    pared.transient(ventana)
    ventana.mainloop()
#65 ladrillos, 2 baldes de corceplas, 1 balde de cemento y un octavo de m2 de arena colorada para 1 metro cuadrado de pared
    
#ventana bolseado
def bolseado():
    bolseado = Toplevel(ventana)
    bolseado.title("Bolseado")
    bolseado.geometry("1300x650+10+10")
    bolseado.resizable(0, 0)  # Para evitar modificar el tamaño de una ventana
    bolseado.iconbitmap("casa.ico")
    bolseado.config(bg="blue")

    ##
    imagen3 = PhotoImage(file="bolseado.png")
    fondo3 = Label(bolseado, width=120,height=120, image=imagen3).place(x=1130,y=100)
    
    def bolseado1():
        alturaP1=float(alturaP.get())
        largoP1=float(largoP.get())
        resultado=(alturaP1*1)*(largoP1*1)
        presupuesto=(resultado*700)
        agua=8*resultado
        arena=0.03125*resultado
        cemento=1*resultado
        etiqueta4 = Label(bolseado, text=(resultado), font=("Courier",14),bg="black",fg="white").place(x=800, y=180)
        etiqueta6 = Label(bolseado, text=(presupuesto), font=("Courier",14),bg="black",fg="white").place(x=800, y=230)
        etiqueta12 = Label(bolseado, text=("litros de agua:",agua), font=("Courier",12), bg="black",fg="white").place(x=800, y=370)
        etiqueta13 = Label(bolseado, text=("arena negra:",arena), font=("Courier",12), bg="black",fg="white").place(x=800, y=410)
        etiqueta14 = Label(bolseado, text=("cemento:",cemento), font=("Courier",12),bg="black",fg="white").place(x=800, y=450)
    
#etiquetas y botones
    etiqueta = Label(bolseado, text="Bolseado", font=("Courier",30), bg="white").place(x=580, y=30)
    etiqueta1 = Label(bolseado, text="Ingrese la altura de pared a bolsear: ").place(x=410, y=120)
    alturaP=tk.DoubleVar()
    combo=Entry(bolseado,textvariable=alturaP).place(x=800, y=120)
    etiqueta2 = Label(bolseado, text="Ingrese largo de pared a bolsear: ").place(x=410, y=150)
    largoP=tk.DoubleVar()
    combo2=Entry(bolseado,textvariable=largoP).place(x=800, y=150)
    etiqueta3 = Label(bolseado, text="Resultado: ").place(x=410, y=180)
    etiqueta5 = Label(bolseado, text="Precio del Presupuesto: ").place(x=410, y=230)
    Button(bolseado, text="Calcular", fg="#17202A", bg="#FF8000", relief="ridge", borderwidth=5, command=bolseado1, width=12, font=("Arial",12)).place(x=1130,y=250)

    etiqueta7 = Label(bolseado, text="Materiales para M2", font=("Courier",16), bg="white").place(x=220, y=330)
    etiqueta8 = Label(bolseado, text="8 litros de agua", font=("Courier",12), bg="white").place(x=220, y=370)
    etiqueta9 = Label(bolseado, text="1/32 M3 de arena negra", font=("Courier",12), bg="white").place(x=220, y=410)
    etiqueta10 = Label(bolseado, text="1 balde de cemento", font=("Courier",12), bg="white").place(x=220, y=450)
    etiqueta11 = Label(bolseado, text="Cantidad de Materiales", font=("Courier",16), bg="black",fg="white").place(x=800, y=330)

#1 baldes cemento, 8 litros de agua, 1/32 de arena negra.

    bolseado.transient(ventana)
    ventana.mainloop()
  
#ventana reboque
def reboque():
    reboque = Toplevel(ventana)
    reboque.title("Revoque")
    reboque.geometry("1300x650+10+10")
    reboque.resizable(0, 0)  # Para evitar modificar el tamaño de una ventana
    reboque.iconbitmap("casa.ico")
    reboque.config(bg="blue")

    ##
    imagen4 = PhotoImage(file="revoque.png")
    fondo4 = Label(reboque, width=120,height=120, image=imagen4).place(x=1130,y=100)
    def reboque1():
        alturaP1=float(alturaP.get())
        largoP1=float(largoP.get())
        resultado=(alturaP1*1)*(largoP1*1)
        presupuesto=(resultado*850)
        agua=30*resultado
        arena=0.125*resultado
        corceplas=2*resultado
        cemento=1*resultado 
        etiqueta4 = Label(reboque, text=(resultado), font=("Courier",14),  bg="black",fg="white").place(x=800, y=180)
        etiqueta6 = Label(reboque, text=(presupuesto), font=("Courier",14),  bg="black",fg="white").place(x=800, y=230)
        etiqueta11 = Label(reboque, text=("litros de agua:",agua), font=("Courier",12),  bg="black",fg="white").place(x=800, y=370)
        etiqueta13 = Label(reboque, text=("arena colorada:",arena), font=("Courier",12),  bg="black",fg="white").place(x=800, y=410)
        etiqueta14 = Label(reboque, text=("corceplas:",corceplas), font=("Courier",12), bg="black",fg="white").place(x=800, y=450)
        etiqueta15 = Label(reboque, text=("cemento:",cemento), font=("Courier",12),  bg="black",fg="white").place(x=800, y=490)
        
#etiquetas y botones
    etiqueta = Label(reboque, text="Revoque", font=("Courier",30), bg="white").place(x=580, y=30)
    etiqueta1 = Label(reboque, text="Ingrese la altura de pared a revocar: ").place(x=400, y=120)
    alturaP=tk.DoubleVar()
    combo=Entry(reboque,textvariable=alturaP).place(x=800, y=120)
    etiqueta2 = Label(reboque, text="Ingrese largo de pared a revocar: ").place(x=400, y=150)
    largoP=tk.DoubleVar()
    combo2=Entry(reboque,textvariable=largoP).place(x=800, y=150)
    etiqueta3 = Label(reboque, text="Resultado: ").place(x=400, y=180)
    etiqueta5 = Label(reboque, text="Precio del Presupuesto: ").place(x=400, y=230)
    Button(reboque, text="Calcular", fg="#17202A", bg="#FF8000", relief="ridge", borderwidth=5, command=reboque1 , width=12, font=("Arial",12)).place(x=1130,y=250)

    etiqueta = Label(reboque, text="Materiales para M2", font=("Courier",16), bg="white").place(x=220, y=330)
    etiqueta7 = Label(reboque, text="30 litros de agua", font=("Courier",12), bg="white").place(x=220, y=370)
    etiqueta8 = Label(reboque, text="1/8 M3 de arena colorada", font=("Courier",12), bg="white").place(x=220, y=410)
    etiqueta9 = Label(reboque, text="2 balde de corceplas", font=("Courier",12), bg="white").place(x=220, y=450)
    etiqueta10 = Label(reboque, text="1 balde de cemento", font=("Courier",12), bg="white").place(x=220, y=490)
    
    etiqueta12 = Label(reboque, text="Cantidad de Materiales", font=("Courier",16),  bg="black",fg="white").place(x=800, y=330)

    reboque.transient(ventana)
    ventana.mainloop()


#ventana enlucido
def enlucido():
    enlucido = Toplevel(ventana)
    enlucido.title("Enlucido y Reboque")
    enlucido.geometry("1300x650+10+10")
    enlucido.resizable(0, 0)  # Para evitar modificar el tamaño de una ventana
    enlucido.iconbitmap("casa.ico")
    enlucido.config(bg="blue")

    ##
    imagen7 = PhotoImage(file="enlucido.png")
    fondo7 = Label(enlucido, width=120,height=120, image=imagen7).place(x=1130,y=100)
    
    def enlucido1():
        alturaP1=float(alturaP.get())
        largoP1=float(largoP.get())
        resultado=(alturaP1*1)*(largoP1*1)
        presupuesto=(resultado*650)
        agua=8*resultado
        arena=0.03125*resultado
        cal=1*resultado
        cemento=0.03125*resultado
        etiqueta4 = Label(enlucido, text=(resultado), font=("Courier",14), bg="black",fg="white").place(x=800, y=180)
        etiqueta6 = Label(enlucido, text=(presupuesto), font=("Courier",14),bg="black",fg="white").place(x=800, y=230)
        etiqueta11 = Label(enlucido, text=("litros de agua:",agua), font=("Courier",12), bg="black",fg="white").place(x=800, y=370)
        etiqueta13 = Label(enlucido, text=("arena colorada:",arena), font=("Courier",12), bg="black",fg="white").place(x=800, y=410)
        etiqueta14 = Label(enlucido, text=("cal:",cal), font=("Courier",12), bg="black",fg="white").place(x=800, y=450)
        etiqueta15 = Label(enlucido, text=("cemento:",cemento), font=("Courier",12),bg="black",fg="white").place(x=800, y=490) 

#etiquetas y botones
    etiqueta = Label(enlucido, text="Enlucido", font=("Courier",30), bg="white").place(x=600, y=30)
    etiqueta1 = Label(enlucido, text="Ingrese la altura de pared a enlucir: ").place(x=400, y=120)
    alturaP=tk.DoubleVar()
    combo=Entry(enlucido,textvariable=alturaP).place(x=800, y=120)
    etiqueta2 = Label(enlucido, text="Ingrese largo de pared a enlucir: ").place(x=400, y=150)
    largoP=tk.DoubleVar()
    combo2=Entry(enlucido,textvariable=largoP).place(x=800, y=150)
    etiqueta3 = Label(enlucido, text="Resultado: ").place(x=400, y=180)
    etiqueta5 = Label(enlucido, text="Precio del Presupuesto: ").place(x=400, y=230)
    Button(enlucido, text="Calcular", fg="#17202A", bg="#FF8000", relief="ridge", borderwidth=5, command=enlucido1 , width=12, font=("Arial",12)).place(x=1130,y=250)

    etiqueta = Label(enlucido, text="Materiales para M2", font=("Courier",16), bg="white").place(x=220, y=330)
    etiqueta7 = Label(enlucido, text="8 litros de agua", font=("Courier",12), bg="white").place(x=220, y=370)
    etiqueta8 = Label(enlucido, text="1/32 M3 de arena negra", font=("Courier",12), bg="white").place(x=220, y=410)
    etiqueta9 = Label(enlucido, text="1 balde de cal", font=("Courier",12), bg="white").place(x=220, y=450)
    etiqueta10 = Label(enlucido, text="1/32 balde de cemento", font=("Courier",12), bg="white").place(x=220, y=490)
    
    etiqueta12 = Label(enlucido, text="Cantidad de Materiales", font=("Courier",16),bg="black",fg="white").place(x=800, y=330)

    enlucido.transient(ventana)
    ventana.mainloop()

#ventana piso
def piso():
    piso = Toplevel(ventana)
    piso.title("Piso")
    piso.geometry("1300x650+10+10")
    piso.resizable(0, 0)  # Para evitar modificar el tamaño de una ventana
    piso.iconbitmap("casa.ico")
    piso.config(bg="blue")

    ##
    imagen5 = PhotoImage(file="piso.png")
    fondo5 = Label(piso, width=120,height=120, image=imagen5).place(x=1130,y=100)
    
    def piso1():
        anchoP1=float(anchoP.get())
        largoP1=float(largoP.get())
        resultado=(anchoP1*1)*(largoP1*1)
        presupuesto=(resultado*900)
        agua=15*resultado
        cemento=2*resultado
        ripio=0.125*resultado
        etiqueta4 = Label(piso, text=(resultado), font=("Courier",14), bg="black",fg="white").place(x=800, y=180)
        etiqueta6 = Label(piso, text=(presupuesto), font=("Courier",14),bg="black",fg="white").place(x=800, y=230)
        etiqueta11 = Label(piso, text=("litros de agua:",agua), font=("Courier",12),bg="black",fg="white").place(x=800, y=370)
        etiqueta13 = Label(piso, text=("ripio:",ripio), font=("Courier",12),bg="black",fg="white").place(x=800, y=410)
        etiqueta14 = Label(piso, text=("cemento:",cemento), font=("Courier",12),bg="black",fg="white").place(x=800, y=450)

#etiquetas y botones
    etiqueta = Label(piso, text="Piso", font=("Courier",30), bg="white").place(x=600, y=30)
    etiqueta1 = Label(piso, text="Ingrese el ancho del piso: ").place(x=400, y=120)
    anchoP=tk.DoubleVar()
    combo=Entry(piso,textvariable=anchoP).place(x=800, y=120)
    etiqueta2 = Label(piso, text="Ingrese largo del piso: ").place(x=400, y=150)
    largoP=tk.DoubleVar()
    combo2=Entry(piso,textvariable=largoP).place(x=800, y=150)
    etiqueta3 = Label(piso, text="Resultado: ").place(x=400, y=180)
    etiqueta5 = Label(piso, text="Precio del Presupuesto: ").place(x=400, y=230)
    Button(piso, text="Calcular", fg="#17202A", bg="#FF8000", relief="ridge", borderwidth=5, command=piso1 , width=12, font=("Arial",12)).place(x=1130,y=250)

    etiqueta = Label(piso, text="Materiales para M2", font=("Courier",16), bg="white").place(x=220, y=330)
    etiqueta7 = Label(piso, text="15 litros de agua", font=("Courier",12), bg="white").place(x=220, y=370)
    etiqueta8 = Label(piso, text="1/32 M3 de ripio", font=("Courier",12), bg="white").place(x=220, y=410)
    etiqueta9 = Label(piso, text="2 baldes de cemento", font=("Courier",12), bg="white").place(x=220, y=450)
    
    etiqueta12 = Label(piso, text="Cantidad de Materiales", font=("Courier",16),bg="black",fg="white").place(x=800, y=330) 

    piso.transient(ventana)
    ventana.mainloop()
    
#ventana ceramica
def ceramica():
    ceramica = Toplevel(ventana)
    ceramica.title("Ceramicas")
    ceramica.geometry("1300x650+10+10")
    ceramica.resizable(0, 0)  # Para evitar modificar el tamaño de una ventana
    ceramica.iconbitmap("casa.ico")
    ceramica.config(bg="blue")

    ##
    imagen6 = PhotoImage(file="ceramica.png")
    fondo6 = Label(ceramica, width=120,height=120, image=imagen6).place(x=1130,y=100)
    
    def ceramica1():
        anchoP1=float(anchoP.get())
        largoP1=float(largoP.get())
        resultado=(anchoP1*1)*(largoP1*1)
        presupuesto=(resultado*700)
        agua=4*resultado
        pegamento=2*resultado
        ceramicas=3*resultado
        etiqueta4 = Label(ceramica, text=(resultado), font=("Courier",14),bg="black",fg="white").place(x=800, y=180)
        etiqueta6 = Label(ceramica, text=(presupuesto), font=("Courier",14),bg="black",fg="white").place(x=800, y=230)
        etiqueta11 = Label(ceramica, text=("litros de agua:",agua), font=("Courier",12), bg="black",fg="white").place(x=800, y=370)
        etiqueta13 = Label(ceramica, text=("pegamento:",pegamento), font=("Courier",12), bg="black",fg="white").place(x=800, y=410)
        etiqueta14 = Label(ceramica, text=("ceramica:",ceramicas), font=("Courier",12),bg="black",fg="white").place(x=800, y=450)
    
#etiquetas y botones
    etiqueta = Label(ceramica, text="Ceramica", font=("Courier",30), bg="white").place(x=600, y=30)
    etiqueta1 = Label(ceramica, text="Ingrese el ancho del piso ah colocar ceramica: ").place(x=400, y=120)
    anchoP=tk.DoubleVar()
    combo=Entry(ceramica,textvariable=anchoP).place(x=800, y=120)
    etiqueta2 = Label(ceramica, text="Ingrese largo del piso ah colocar ceramica: ").place(x=400, y=150)
    largoP=tk.DoubleVar()
    combo2=Entry(ceramica,textvariable=largoP).place(x=800, y=150)
    etiqueta3 = Label(ceramica, text="Resultado: ").place(x=400, y=180)
    etiqueta5 = Label(ceramica, text="Precio del Presupuesto: ").place(x=400, y=230)
    Button(ceramica, text="Calcular", fg="#17202A", bg="#FF8000", relief="ridge", borderwidth=5, command=ceramica1, width=12, font=("Arial",12)).place(x=1130,y=250)


    etiqueta = Label(ceramica, text="Materiales para M2", font=("Courier",16), bg="white").place(x=220, y=330)
    etiqueta7 = Label(ceramica, text="4 litros de agua", font=("Courier",12), bg="white").place(x=220, y=370)
    etiqueta8 = Label(ceramica, text="2 baldes de pegamento", font=("Courier",12), bg="white").place(x=220, y=410)
    etiqueta9 = Label(ceramica, text="3 ceramica de 40x40 para m2", font=("Courier",12), bg="white").place(x=220, y=450)

    
    etiqueta12 = Label(ceramica, text="Cantidad de Materiales", font=("Courier",16), bg="black",fg="white").place(x=800, y=330)

    ceramica.transient(ventana)
    ventana.mainloop()

    
#ventana techado
def techado():
    techado = Toplevel(ventana)
    techado.title("Techado")
    techado.geometry("1300x650+10+10")
    techado.resizable(0, 0)  # Para evitar modificar el tamaño de una ventana
    techado.iconbitmap("casa.ico")
    techado.config(bg="blue")

    ##
    imagen8 = PhotoImage(file="techado.png")
    fondo8 = Label(techado, width=120,height=120, image=imagen8).place(x=1130,y=100)
    
    def techado1():
        anchot1=float(anchot.get())
        largot1=float(largot.get())
        resultado=(anchot1*1)*(largot1*1)
        presupuesto=(resultado*5500)
        chapa=1*resultado
        tornillo=12*resultado
        alfajia=4*resultado
        palo=2*resultado
        madera=10*resultado
        etiqueta4 = Label(techado, text=(resultado), font=("Courier",14), bg="black",fg="white").place(x=800, y=180)
        etiqueta6 = Label(techado, text=(presupuesto), font=("Courier",14), bg="black",fg="white").place(x=800, y=230)
        etiqueta14 = Label(techado, text=("chapa:",chapa), font=("Courier",12),bg="black",fg="white").place(x=800, y=370)
        etiqueta15 = Label(techado, text=("tornillos:",tornillo), font=("Courier",12), bg="black",fg="white").place(x=800, y=410)
        etiqueta16 = Label(techado, text=("alfajias:",alfajia), font=("Courier",12),bg="black",fg="white").place(x=800, y=450)
        etiqueta17 = Label(techado, text=("palos:",palo), font=("Courier",12), bg="black",fg="white").place(x=800, y=490)
        etiqueta18 = Label(techado, text=("tablas:",madera), font=("Courier",12), bg="black",fg="white").place(x=800, y=530)
    
#etiquetas y botones
    etiqueta = Label(techado, text="Techado", font=("Courier",30), bg="white").place(x=600, y=30)
    etiqueta1 = Label(techado, text="Ingrese el ancho del techo ah colocar: ").place(x=400, y=120)
    anchot=tk.DoubleVar()
    combo=Entry(techado,textvariable=anchot).place(x=800, y=120)
    etiqueta2 = Label(techado, text="Ingrese largo del techo ah colocar: ").place(x=400, y=150)
    largot=tk.DoubleVar()
    combo2=Entry(techado,textvariable=largot).place(x=800, y=150)
    etiqueta3 = Label(techado, text="Resultado: ").place(x=400, y=180)
    etiqueta5 = Label(techado, text="Precio del Presupuesto: ").place(x=400, y=230)
    Button(techado, text="Calcular", fg="#17202A", bg="#FF8000", relief="ridge", borderwidth=5, command=techado1, width=12, font=("Arial",12)).place(x=1130,y=250)

    etiqueta7 = Label(techado, text="Materiales para M3", font=("Courier",16), bg="white").place(x=220, y=330)
    etiqueta8 = Label(techado, text="1 chapa de m2", font=("Courier",12), bg="white").place(x=220, y=370)
    etiqueta9 = Label(techado, text="12 tornillos con arandelas", font=("Courier",12), bg="white").place(x=220, y=410)
    etiqueta10 = Label(techado, text="4 alfajias de 1m", font=("Courier",12), bg="white").place(x=220, y=450)
    etiqueta11 = Label(techado, text="2 palos de 1m", font=("Courier",12), bg="white").place(x=220, y=490)
    etiqueta12 = Label(techado, text="10 tablas de 1m y de 10cm", font=("Courier",12), bg="white").place(x=220, y=530)
    etiqueta13 = Label(techado, text="Cantidad de Materiales", font=("Courier",16), bg="black",fg="white").place(x=800, y=330)
  
    techado.transient(ventana)
    ventana.mainloop()

    
#ventana hija
def accion1():
    hija = Toplevel(ventana)
    hija.title("Constructora Rojas")
    hija.geometry("1300x650+10+10")
    hija.resizable(0, 0)  # Para evitar modificar el tamaño de una ventana
    hija.iconbitmap("casa.ico")
    hija.config(bg="blue")

    ### imagenes Formulario
    imagen2 = PhotoImage(file="pared.png")
    fondo2 = Label(hija, width=120,height=120, image=imagen2).place(x=50,y=300)
    ##
    imagen3 = PhotoImage(file="bolseado.png")
    fondo3 = Label(hija, width=120,height=120, image=imagen3).place(x=230,y=300)
    ##
    imagen4 = PhotoImage(file="revoque.png")
    fondo4 = Label(hija, width=120,height=120, image=imagen4).place(x=410,y=300)
    ##
    imagen5 = PhotoImage(file="piso.png")
    fondo5 = Label(hija, width=120,height=120, image=imagen5).place(x=590,y=300)
    ##
    imagen6 = PhotoImage(file="ceramica.png")
    fondo6 = Label(hija, width=120,height=120, image=imagen6).place(x=770,y=300)
    ##
    imagen7 = PhotoImage(file="enlucido.png")
    fondo7 = Label(hija, width=120,height=120, image=imagen7).place(x=950,y=300)
    ##
    imagen8 = PhotoImage(file="techado.png")
    fondo8 = Label(hija, width=120,height=120, image=imagen8).place(x=1130,y=300)


    #botones
    Cerrar = Button(hija, text="Pared", fg="#17202A", bg="#FF8000", relief="ridge", borderwidth=5, command=pared, width=12, font=("Arial",12)).place(x=50,y=470)
    Cerrar = Button(hija, text="Bolseado", fg="#17202A", bg="#FF8000", relief="ridge", borderwidth=5, command=bolseado, width=12, font=("Arial",12)).place(x=230,y=470)
    Cerrar = Button(hija, text="Revoque", fg="#17202A", bg="#FF8000", relief="ridge", borderwidth=5, command=reboque, width=12, font=("Arial",12)).place(x=410,y=470)
    Cerrar = Button(hija, text="Piso", fg="#17202A", bg="#FF8000", relief="ridge", borderwidth=5, command=piso, width=12, font=("Arial",12)).place(x=590,y=470)
    Cerrar = Button(hija, text="Ceramica", fg="#17202A", bg="#FF8000", relief="ridge", borderwidth=5, command=ceramica, width=12, font=("Arial",12)).place(x=770,y=470)
    Cerrar = Button(hija, text="Enlucido", fg="#17202A", bg="#FF8000", relief="ridge", borderwidth=5, command=enlucido, width=12, font=("Arial",12)).place(x=950,y=470)
    Cerrar = Button(hija, text="Techado", fg="#17202A", bg="#FF8000", relief="ridge", borderwidth=5, command=techado, width=12, font=("Arial",12)).place(x=1130,y=470)
        
    etiqueta = Label(hija, text="Trabajos", font=("Courier",32), bg="blue",fg="white").place(x=500, y=30)

    hija.transient(ventana)
    ventana.mainloop()

#ventana madre
ventana = tk.Tk()
ventana.protocol("WM_DELETE_WINDOW", cerrar_aplicacion)
ventana.title("Constructora Rojas")
ventana.geometry("1300x650+10+10")
ventana.resizable(0, 0)  # Para evitar modificar el tamaño de una ventana
ventana.iconbitmap("casa.ico")
ventana.config(bg="blue")
imagen = PhotoImage(file="casa2.png")
fondo1 = Label(ventana, image=imagen).place(x=500,y=200)

# creamos una barra de menus y la añadimos a la ventana principal
menubar = Menu(ventana)
ventana.config(menu=menubar)

# Agregar opciones al menú
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="Ir al programa",font=("Calibri",10), command=accion1)
#Separador de Ventana
filemenu.add_separator()
#fin Separador de Ventana
filemenu.add_command(label="Salir del Programa", command=cerrar_aplicacion)

helpmenu = Menu(menubar, tearoff=0)
helpmenu.add_command(label="Ayuda")

menubar.add_cascade(label="Archivo", menu=filemenu)
menubar.add_cascade(label="Ayuda", menu=helpmenu)

# Crear Boton Salir de Sistema
Cerrar = Button(ventana, text="Ir al programa", fg="#17202A", bg="#FF8000", relief="ridge", borderwidth=8, command=accion1 , font=("Arial",12), width=15).place(x=450,y=520)
Cerrar = Button(ventana, text="Salir del Sistema", fg="#17202A", bg="#FF8000", relief="ridge", borderwidth=8, command=cerrar_aplicacion ,font=("Arial",12), width=15).place(x=680,y=520)
etiqueta = Label(ventana, text="Constructora Rojas", font=("Courier",32), bg="blue",fg="white").place(x=400, y=30)
etiqueta1 = Label(ventana, text="Presupuestos de Mamposteria", font=("Courier",18), bg="blue",fg="white").place(x=450, y=100)

# Activar ventana
ventana.mainloop()