from tkinter import *

#Creamos la raiz y la nombramos

raiz=Tk()
raiz.title('Python CRUD-Comision 22624')

#creamos el primer menu y sus submenues en cascada

barramenu=Menu(raiz)
raiz.config(menu=barramenu)

bbddmenu=Menu(barramenu, tearoff=0)
bbddmenu.add_command(label='Conectar con BBDD')
bbddmenu.add_command(label='Salir del programa')

borrarmenu=Menu(barramenu, tearoff=0)
borrarmenu.add_command(label='Limpiar formulario')

ayudamenu=Menu(barramenu, tearoff=0)
ayudamenu.add_command(label='Licencia')
ayudamenu.add_command(label='Acerca de..')

barramenu.add_cascade(label='BBDD', menu=bbddmenu)
barramenu.add_cascade(label='Limpiar', menu=borrarmenu)
barramenu.add_cascade(label='Acerca de..', menu=ayudamenu)

#----------------FRAME CAMPOS----------------------

framecampos=Frame(raiz) #notese objeto de tipo frame
framecampos.pack() #este meotodo se usa para adaptar el frame al tamaño del contenido
'''
"STICKY"
        n
    nw      ne
w               e
    sw      se
        s
'''
#Apunte: posicionamienta de elementos en tkinter:
#https://recursospython.com/guias-y-manuales/posicionar-elementos-en-tkinter/

legajolabel=Label(framecampos, text='Legajo')
legajolabel.grid(row=0, column=0, sticky='e', padx=10, pady=10)#donde lo ubicamos, y el padding en x y en y

alumnolabel=Label(framecampos, text='Alumno')
alumnolabel.grid(row=1, column=0, sticky='e', padx=10, pady=10)

emaillabel=Label(framecampos, text='Email')
emaillabel.grid(row=2, column=0, sticky='e', padx=10, pady=10)

calificacionlabel=Label(framecampos, text='Calificacion')
calificacionlabel.grid(row=3, column=0, sticky='e', padx=10, pady=10)

escuelalabel=Label(framecampos, text='Escuela')
escuelalabel.grid(row=4, column=0, sticky='e', padx=10, pady=10)

localidadlabel=Label(framecampos, text='Localidad')
localidadlabel.grid(row=5, column=0, sticky='e', padx=10, pady=10)

provincialabel=Label(framecampos, text='Provincia')
provincialabel.grid(row=6, column=0, sticky='e', padx=10, pady=10)

#========================== INPUTS ==============================

#para los inputs tenemos que definir variables, pero estas son propias de tkinter:
'''
entero = IntVar()
flotante = DoubleVar()
cadena = StringVar()
booleano = BooleanVar()
'''
#necesito variables:
legajo=StringVar()
alumno=StringVar()
email=StringVar()
calificacion=DoubleVar()
escuela=StringVar()
localidad=StringVar()
provincia=StringVar()

#luego creo y ubico los inputs

legajo_input=Entry(framecampos, textvariable='legajo')
legajo_input.grid(row=0, column=1, padx=10, pady=10)#donde lo ubicamos y el padding en x y en Y

alumno_input=Entry(framecampos, textvariable='alumno')
alumno_input.grid(row=1, column=1, padx=10, pady=10)

email_input=Entry(framecampos, textvariable='email')
email_input.grid(row=2, column=1, padx=10, pady=10)

calificacion_input=Entry(framecampos, textvariable='calificacion')
calificacion_input.grid(row=3, column=1, padx=10, pady=10)

escuela_input=Entry(framecampos, textvariable='escuela')
escuela_input.grid(row=4, column=1, padx=10, pady=10)

localidad_input=Entry(framecampos, textvariable='localidad')
localidad_input.grid(row=5, column=1, padx=10, pady=10)

provincia_input=Entry(framecampos, textvariable='provincia')
provincia_input.grid(row=6, column=1, padx=10, pady=10)


#---------------------FRAME BOTONES-----------------------
framebotones=Frame(raiz)
framebotones.pack()

boton_crear=Button(framebotones, text='Crear')
boton_crear.grid(row=1, column=0, sticky="e", padx=10, pady=10)

boton_leer=Button(framebotones, text='Leer')
boton_leer.grid(row=1, column=1, sticky="e", padx=10, pady=10)

boton_actualizar=Button(framebotones, text='Actualizar')
boton_actualizar.grid(row=1, column=2, sticky="e", padx=10, pady=10)

boton_borrar=Button(framebotones, text='Borrar')
boton_borrar.grid(row=1, column=3, sticky="e", padx=10, pady=10)

#------------FRAMECOPY------------------

framecopy=Frame(raiz)
framecopy.pack()

copylabel=Label(framecopy, text='©2022 Copyright: Codo a Codo C#22624, tkinter desarrollado por Juan Basgall. \n Todos los derechos reservados.')
copylabel.grid(row=0, column=0, padx=30, pady=10)

#copylabel=Text('Este es un texto de prueba2') este no funciono





raiz.mainloop()