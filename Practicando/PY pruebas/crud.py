from tkinter import *
from tkinter import messagebox
import mysql.connector #instale antes el "pip install mysql-connector-python" desde la consola
from asyncio.windows_events import NULL



#db = new PDO("mysql:dbname=miproyecto;host=127.0.0.1","root","");

def conectar():
    print('entrando al conector')
    global con
    global cur
    try:
        con=mysql.connector.connect(host='127.0.0.1', user='root', password='', db='miproyecto')
        cur=con.cursor()
        messagebox.showinfo('COMECTADO', '¡La conexión con la base de datos ha sido existosa!')
        print("STATUS", "¡Conectado con la bbdd!")
    except Exception as e:
        print('ERROR', 'No se pudo conectar a la base de datos')


def salir():
    resp=messagebox.askquestion('Confirme', "¿Desea salir del programa?")
    if resp=="yes":
        raiz.destroy()

def buscar_escuelas(actualiza):
    con=sq3.connect('mi_db.db')
    cur=con.cursor()
    if actualiza:
        cur.execute('SELECT _id, localidad, provincia FROM escuelas WHERE nombre=?', (escuela.get(),))
    else:
        cur.execute('SELECT nombre FROM escuelas')
    
    resultado=cur.fetchall()#aca metemos unalista de tuplas del resultado del if anterior
    retorno=[]
    for e in resultado:
        if actualiza:
            #messagebox.showinfo('AYUDA', 'entramos al lugar correcto')
            id=e[0]
            loc=e[1]
            prov=e[2]
            retorno.append(id)
            retorno.append(loc)
            retorno.append(prov)
        else:
            esc=e[0]
            retorno.append(esc)
        
    con.close()
    return retorno
    
#buscar_escuelas(False)


def limpiar():
    id.set('')
    categoria.set('')
    

def mostrar_licencia():
# CREATIVE COMMONS GNU GPL https://www.gnu.org/licenses/gpl-3.0.txt
  msg = '''
  Demo de un sistema CRUD en Python para gestión 
  de alumnos
  Copyright (C) 2022 - Karin Fleischer
  Email: kkkk@bue.edu.ar\n=======================================
  This program is free software: you can redistribute it 
  and/or modify it under the terms of the GNU General Public 
  License as published by the Free Software Foundation, 
  either version 3 of the License, or (at your option) any 
  later version.
  This program is distributed in the hope that it will be 
  useful, but WITHOUT ANY WARRANTY; without even the 
  implied warranty of MERCHANTABILITY or FITNESS FOR A 
  PARTICULAR PURPOSE.  See the GNU General Public License 
  for more details.
  You should have received a copy of the GNU General Public 
  License along with this program.  
  If not, see <https://www.gnu.org/licenses/>.'''
  messagebox.showinfo("LICENCIA", msg)

def mostrar_acercade():
    messagebox.showinfo("ACERCA DE...", "Creado por Juan Angel Basgall \npara Codo a Codo - Big Data \nNoviembre 2022")

#Con Ctrl+k+c puedo comentar todas las lineas seleccionadas


def boton(rw, col, txt, hcolor=NULL, cmd=NULL, tcolor = NULL,):
    def hover(event):
        miBoton.config(bg=hcolor)
        if tcolor==0:
            miBoton.config(fg=framebotones_color_texto)
        else:
            miBoton.config(fg=tcolor)

    def leave(event):
        miBoton.config(bg=framebotones_color_boton, fg=framebotones_color_texto)

    miBoton=Button(framebotones, text=txt, command=cmd)
    miBoton.config(bg=framebotones_color_boton,fg=framebotones_color_texto,width=10,cursor='hand2')
    miBoton.grid(row=rw, column=col, sticky="e", padx=20, pady=10)
    miBoton.bind("<Enter>", hover)
    miBoton.bind("<Leave>", leave)


def listar():




    class Table():
        def __init__(self, raiz2):
            nombre_cols=['ID', 'Categoria']
            for i in range(cant_cols):
                self.e=Entry(frameppal)
                self.e.config(bg='black', fg='lightgreen')
                self.e.grid(row=0, column=i)
                self.e.insert(END, nombre_cols[i])#Que ponga uno a continuacion dle otro
                #self.e.config(state='readonly')
                for fila in range(cant_filas):
                    for col in range(cant_cols):
                        self.e=Entry(frameppal)
                        self.e.config(bg='blue', fg='black')
                        self.e.grid(row=fila+1, column=col)
                        self.e.insert(END, resultado[fila][col])
                        self.e.config(state='readonly')
    raiz2=Tk()
    raiz2.title('listado categorias')
    raiz2.resizable(0,0)#esto hace que  no se pueda agrandar la ventana, recibe 2 valores, ambos booleanos, que corresponden al (width, height)
    #raiz2.iconbitmap("IMG\\hansicon.ico")#Pongo el icono de la ventana
    raiz2.config(bg='gray96')
    frameppal=LabelFrame(raiz2, text='Listado completo de categorias', padx=20, pady=20)
    frameppal.pack(fill='both',
                    padx=15,
                    pady=15,
                    )
    frameppal.config(bg='lightskyblue1')
    framecerrar=Frame(raiz2)
    framecerrar.pack(fill='both',
                    padx=15,
                    pady=15,
                    )

    boton_cerrar=Button(framecerrar, text='Cerrar', command=raiz2.destroy)
    boton_cerrar.config(bg='coral', fg='gray22', cursor='pirate')
    boton_cerrar.pack(fill='both')
    #boton_cerrar.grid(row=0, column=0)
    try:
        conectar()
        conmssj=Label(raiz2, text='Conexion exitosa con la BBDD')
        conmssj.pack()
    except Exception as e:
        conmssj=Label(raiz2, text='Error de conexión con la BBDD')
        conmssj.pack()
        messagebox.showerror('ERROR', 'No se pudo conectar a la base de datos')
   
    query1 = '''SELECT * FROM categorias'''
    cur.execute(query1)
    resultado=cur.fetchall()
    cant_filas=len(resultado)
    cant_cols=(len(resultado[0]))
    tabla=Table(frameppal)
    con.close()
    raiz2.mainloop

# CRUD-------------
'''
Pasando los crear y actualizar tuve un problema con las sentencias, resulta que
por algun motivo ahora no le justan los '?' para representar valores, sino que le gustan
los '%s'

esto lo resolvió el bot: GPT-3

y aca hay una explicación de la diferencia:

In an SQL statement, the ? character and the %s string are used as placeholders for values that will be passed to the statement later. The difference between them is in the way they are used and the type of data they can hold.

The ? character is used as a placeholder in the pyodbc library for Python. It is used to represent a parameter that will be passed to the execute() method of the cursor object. The execute() method accepts a tuple or a list of values that will be used to replace the ? placeholders in the SQL statement. The ? placeholder can hold values of any type, such as strings, integers, or floating-point numbers.

On the other hand, the %s string is used as a placeholder in the mysql-connector-python library for Python. It is used to represent a string parameter that will be passed to the execute() method of the cursor object. The execute() method accepts a tuple or a list of values that will be used to replace the %s placeholders in the SQL statement. The %s placeholder can only hold string values.

In general, the ? placeholder is more flexible and can hold values of different types, while the %s placeholder is limited to holding string values.

I hope this helps! Let me know if you have any other questions.
'''



# CREAR
def crear():
    try:
        query_buscar = '''SELECT id, nombre_categoria FROM categorias WHERE id='''
        cur.execute(query_buscar+id.get())
        resultado=cur.fetchall()
        if resultado ==[]:
            datos=(id.get(), categoria.get())
            cur.execute("INSERT INTO categorias (id, nombre_categoria) VALUES (%s,%s)",datos)
            con.commit()
            messagebox.showinfo("STATUS", "registro agregado")
            limpiar()
        else:
            messagebox.showerror("ERROR","El número de legajo ya existe")
            print(e)
            categoria.set("")
            limpiar()
    except Exception as e:
        messagebox.showerror('ERROR', 'No se pudo crear el alumno, revise la conexión a la Base de Datos.')
        print(e)
    

# LEER
def buscar_legajo():
    query_buscar = '''SELECT nombre_categoria FROM categorias WHERE id='''
    try:
        cur.execute(query_buscar+id.get()) #ejecuta el query + lo que le ponemos en el imput como legajo, entonces con esto completa el query
        resultado=cur.fetchall()
        if resultado ==[]:
            messagebox.showerror("ERROR","El numero de legajo no existe")
            id.set("")
        else:
            print(resultado)
            for campo in resultado:
                print("ese es el campo:", campo)

                categoria.set(campo[0])
               
    except Exception as e:
        messagebox.showerror('ERROR', 'No se pudo leer el legajo, revise la conexión a la Base de Datos.')
# ACTUALIZAR
def actualizar():
    try:
        print('En el try')
        datos=(categoria.get(),id.get())
        print('datos:', datos)
        # Construct the UPDATE statement
        sql = '''UPDATE categorias SET nombre_categoria=%s WHERE id=%s'''
        val = (categoria.get(), id.get())

        # Execute the UPDATE statement
        cur.execute(sql, val)
        con.commit()
        messagebox.showinfo('STATUS', 'Registro actualizado')
        limpiar()
    except Exception as e:
        messagebox.showerror('ERROR', 'No se pudo actualizar el alumno, revise la conexión a la Base de Datos.',)
        print(e)
# BORRAR 
def borrar():
    resp=messagebox.askquestion("BORRAR", '¿Está seguro que desea borrar el registro?')
    if resp:
        try:
            cur.execute('DELETE FROM categorias WHERE id='+id.get())
            con.commit()
            messagebox.showinfo("STATUS", 'Registro eliminado')
            limpiar()
        except Exception as e:
            messagebox.showerror('ERROR', 'No se pudo borrar el alumno, revise la conexión a la Base de Datos.')


'''
=====================================================
INTERFAZ GRAFICA
=====================================================
'''
esp_x=10
esp_y=10
#colores para el framecampos
framecampos_color_fondo='gray96'
framecampos_color_letras='black'

framebotones_color_fondo='lightskyblue1'
framebotones_color_boton='gray22'
framebotones_color_texto='gray96'



#Creamos la raiz y la nombramos

raiz=Tk()
raiz.title('Python CRUD - Mercado Lan')
raiz.resizable(0,0)#esto hace que  no se pueda agrandar la ventana, recibe 2 valores, ambos booleanos, que corresponden al (width, height)
#raiz.iconbitmap("IMG\\hansicon.ico")#La defino así para poder compartir luego el archivo compilado
#raiz.iconbitmap("C:\\Users\\Hans\\Desktop\\Python\\IMG\\hansicon.ico")#Pongo el icono de la ventana
#raiz.geometry("500x430")#Definimos el tamaño de la ventana

#creamos el primer menu y sus submenues en cascada

barramenu=Menu(raiz)
raiz.config(menu=barramenu)

bbddmenu=Menu(barramenu, tearoff=0)
bbddmenu.add_command(label='Conectar con BBDD', command=conectar)#el conectar es la función que definimos
bbddmenu.add_command(label='Listar categorias', command=listar)
bbddmenu.add_command(label='Listar productos', command=listar)
bbddmenu.add_command(label='Salir del programa', command=salir)#salir la definimos nosotros

borrarmenu=Menu(barramenu, tearoff=0)
borrarmenu.add_command(label='Limpiar formulario', command=limpiar)

ayudamenu=Menu(barramenu, tearoff=0)
ayudamenu.add_command(label='Licencia', command=mostrar_licencia)
ayudamenu.add_command(label='Acerca de..', command=mostrar_acercade)

barramenu.add_cascade(label='BBDD', menu=bbddmenu)
barramenu.add_cascade(label='Limpiar', menu=borrarmenu)
barramenu.add_cascade(label='Acerca de..', menu=ayudamenu)

#----------------FRAME CAMPOS----------------------
def config_label(mi_label, fila):
    espaciado_label={'column':0, 'sticky':'e', 'padx':esp_x, 'pady':esp_y}
    color_labels={'bg':framecampos_color_fondo, 'fg':framecampos_color_letras}
    mi_label.grid(row=fila, **espaciado_label)
    mi_label.config(**color_labels)

contenedorcampos=Frame(raiz, width=650, height=335)
contenedorcampos.pack(fill='both')
contenedorcampos.config(bg=framecampos_color_fondo)
framecampos=Frame(contenedorcampos) #notese objeto de tipo frame
framecampos.config(bg=framecampos_color_fondo, border=6, relief="groove")
framecampos.place(x=300, y=10) #este meotodo se usa para adaptar el frame al tamaño del contenido
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



'''
miImagen=PhotoImage(file=".\\IMG\\hanslogo.png")
Label(contenedorcampos, image=miImagen, width=246, height=246).place(x=30, y=30)
'''


idlabel=Label(framecampos, text='ID')
config_label(idlabel,0)
#legajolabel.grid(row=0, column=0, sticky='e', padx=10, pady=10)#donde lo ubicamos, y el padding en x y en y

categorialabel=Label(framecampos, text='categoria')
config_label(categorialabel,1)
#alumnolabel.grid(row=1, column=0, sticky='e', padx=10, pady=10)


#========================== INPUTS ==============================

#para los inputs tenemos que definir variables, pero estas son propias de tkinter:
'''
entero = IntVar()
flotante = DoubleVar()
cadena = StringVar()
booleano = BooleanVar()
'''
#necesito variables:
id=StringVar()
categoria=StringVar()

#luego creo y ubico los inputs



widthinputs={'width':35}

id_input=Entry(framecampos, textvariable=id)
id_input.grid(row=0, column=1, padx=10, pady=10)#donde lo ubicamos y el padding en x y en Y
id_input.config(**widthinputs)
id_input.focus()

categoria_input=Entry(framecampos, textvariable=categoria)
categoria_input.grid(row=1, column=1, padx=10, pady=10)
categoria_input.config(**widthinputs)


#---------------------FRAME BOTONES-----------------------
contenedorbotones=Frame(raiz)
contenedorbotones.pack(fill='both')
contenedorbotones.config(bg=framebotones_color_fondo)
framebotones=Frame(contenedorbotones)
framebotones.config(bg=framebotones_color_fondo)
framebotones.pack()


boton(1, 0, "Crear", 'green', crear)
boton(1, 1, "Leer", "yellow", buscar_legajo, 'Black')
boton(1, 2, 'Actualizar', 'blue', actualizar)
boton(1, 3, 'Borrar', 'Red', borrar)


#------------FRAMECOPY------------------

framecopy=Frame(raiz)
framecopy.config(bg='coral', pady=20)
framecopy.pack(fill='both', expand='true')

copylabel=Label(framecopy, text='©2022 Copyright: Codo a Codo C#22624, tkinter desarrollado por Juan Basgall. \n Todos los derechos reservados.')
copylabel.config(bg='salmon4', fg='white', border=4)
copylabel.pack()



raiz.mainloop()
