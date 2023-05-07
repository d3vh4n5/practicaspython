


class Person:
    edad=''

    def __init__(self, nombre, apellido = None):
        self.nombre = nombre
        self.apellido = apellido
        print('Esto es el init')
    
    def otrometodo(self):
        print('Este es el otro metodo')

try:
    nuevapersona = Person('Victor')
    nuevapersona.edad = 27
    nuevapersona.otrometodo()

    print(nuevapersona.edad, nuevapersona.nombre, nuevapersona.apellido)
except Exception as e:
    print("Error: ",e)