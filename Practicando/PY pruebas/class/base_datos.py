import autoload
import mysql.connector #instale antes el "pip install mysql-connector-python" desde la consola

def conectar():
    print('entrando al conector')
    global con
    global cur
    try:
        con=mysql.connector.connect(host='127.0.0.1', user='root', password='', db='miproyecto')
        cur=con.cursor()
        print("STATUS", "¡Conectado con la bbdd!")
    except Exception as e:
        print('ERROR', 'No se pudo conectar a la base de datos')

#conectar()

'''
=======================================================
DEFINIENDO LA CLASE
=======================================================
'''

class Base_datos:

    def __init__(self):
        
    