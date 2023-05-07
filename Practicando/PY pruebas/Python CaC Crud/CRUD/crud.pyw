from tkinter import *
from tkinter import messagebox
from asyncio.windows_events import NULL
import sqlite3 as sq3
'''
=====================================================
PARTE FUNCIONAL
=====================================================
'''
def conectar():
    global con
    global cur
    con=sq3.connect('mi_db.db')
    cur=con.cursor()
    messagebox.showinfo("STATUS", "¡Conectado con la bbdd!")

def salir():
    resp=messagebox.askquestion('Confirme', "¿Desea salir del programa?")
    if resp=="yes":
        raiz.destroy()

def buscar_escuela(actualiza):
    con=sq3.connect('mi_db.db')
    cur=con.cursor()
    if actualiza:
        cur.execute('SELECT _id, localidad, provincia FROM escuelas WHERE nombre=?', (escuela.get(),))
    else:
        cur.execute('SELECT nombre FROM escuelas')
    resultado=cur.fetchall()
    
    for e in resultado:
        print(e)
    con.close()

buscar_escuela(False)





'''
=====================================================
INTERFAZ GRAFICA
=====================================================
'''
esp_x=10
esp_y=10
#colores para el framecampos
framecampos_color_fondo='cyan'
framecampos_color_letras='red'

framebotones_color_fondo='plum'
framebotones_color_boton='black'
framebotones_color_texto='lightgreen'



#Creamos la raiz y la nombramos

raiz=Tk()
raiz.title('Python CRUD-Comision 22624')

#creamos el primer menu y sus submenues en cascada

barramenu=Menu(raiz)
raiz.config(menu=barramenu)

bbddmenu=Menu(barramenu, tearoff=0)
bbddmenu.add_command(label='Conectar con BBDD', command=conectar)#el conectar es la función que definimos
bbddmenu.add_command(label='Salir del programa', command=salir)#salir la definimos nosotros

borrarmenu=Menu(barramenu, tearoff=0)
borrarmenu.add_command(label='Limpiar formulario')

ayudamenu=Menu(barramenu, tearoff=0)
ayudamenu.add_command(label='Licencia')
ayudamenu.add_command(label='Acerca de..')

barramenu.add_cascade(label='BBDD', menu=bbddmenu)
barramenu.add_cascade(label='Limpiar', menu=borrarmenu)
barramenu.add_cascade(label='Acerca de..', menu=ayudamenu)

#----------------FRAME CAMPOS----------------------
def config_label(mi_label, fila):
    espaciado_label={'column':0, 'sticky':'e', 'padx':esp_x, 'pady':esp_y}
    color_labels={'bg':framecampos_color_fondo, 'fg':framecampos_color_letras}
    mi_label.grid(row=fila, **espaciado_label)
    mi_label.config(**color_labels)

framecampos=Frame(raiz) #notese objeto de tipo frame
framecampos.config(bg=framecampos_color_fondo)
framecampos.pack(fill='both') #este meotodo se usa para adaptar el frame al tamaño del contenido
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
config_label(legajolabel,0)
#legajolabel.grid(row=0, column=0, sticky='e', padx=10, pady=10)#donde lo ubicamos, y el padding en x y en y

alumnolabel=Label(framecampos, text='Alumno')
config_label(alumnolabel,1)
#alumnolabel.grid(row=1, column=0, sticky='e', padx=10, pady=10)

emaillabel=Label(framecampos, text='Email')
config_label(emaillabel,2)
#emaillabel.grid(row=2, column=0, sticky='e', padx=10, pady=10)

calificacionlabel=Label(framecampos, text='Calificacion')
config_label(calificacionlabel,3)
#calificacionlabel.grid(row=3, column=0, sticky='e', padx=10, pady=10)

escuelalabel=Label(framecampos, text='Escuela')
config_label(escuelalabel,4)
#escuelalabel.grid(row=4, column=0, sticky='e', padx=10, pady=10)

localidadlabel=Label(framecampos, text='Localidad')
config_label(localidadlabel,5)
#localidadlabel.grid(row=5, column=0, sticky='e', padx=10, pady=10)

provincialabel=Label(framecampos, text='Provincia')
config_label(provincialabel,6)
#provincialabel.grid(row=6, column=0, sticky='e', padx=10, pady=10)

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
framebotones.config(bg=framebotones_color_fondo)
framebotones.pack(fill='both')

boton_crear=Button(framebotones, text='Crear')
boton_crear.config(bg=framebotones_color_boton, fg=framebotones_color_texto)
boton_crear.grid(row=1, column=0, sticky="e", padx=10, pady=10)

boton_leer=Button(framebotones, text='Leer')
boton_leer.config(bg=framebotones_color_boton, fg=framebotones_color_texto)
boton_leer.grid(row=1, column=1, sticky="e", padx=10, pady=10)

boton_actualizar=Button(framebotones, text='Actualizar')
boton_actualizar.config(bg=framebotones_color_boton, fg=framebotones_color_texto)
boton_actualizar.grid(row=1, column=2, sticky="e", padx=10, pady=10)

boton_borrar=Button(framebotones, text='Borrar')
boton_borrar.config(bg=framebotones_color_boton, fg=framebotones_color_texto)
boton_borrar.grid(row=1, column=3, sticky="e", padx=10, pady=10)

#------------FRAMECOPY------------------

framecopy=Frame(raiz)
framecopy.config(bg='tomato')
framecopy.pack(fill='both', expand='true')

copylabel=Label(framecopy, text='©2022 Copyright: Codo a Codo C#22624, tkinter desarrollado por Juan Basgall. \n Todos los derechos reservados.')
copylabel.config(bg='grey', fg='white')
copylabel.grid(row=0, column=3, padx=30, pady=10)

#copylabel=Text('Este es un texto de prueba2') este no funciono





raiz.mainloop()