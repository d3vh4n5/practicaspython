
# En este agragaremos un método constructor

class Mascota:
    def __init__(self,es,n,ed,s,c):
        self.especie=es
        self.nombre=n
        self.edad=ed
        self.sexo=s
        self.castrado=c

    def mostrarDatos(self):
        print('------------------------------')
        print('especie:  ', self.especie)
        print('nombre:   ', self.nombre)
        print('edad:     ', self.edad)
        print('sexo:     ', self.sexo)
        if self.castrado:
            r='SI'
        else:
            r='NO'
        print('Castrado: ', r)
    def castrar(self):
        self.castrado=True
    def nom(self, n):
        self.nombre=n

print('Intento 4')
m3=Mascota('Lagarto','Godzilla', 2.5, 'M', False)
m3.mostrarDatos()
m3.castrar()
m3.mostrarDatos()
m3.nombre='Raul'
m3.mostrarDatos()
m3.nom('Michilagarto')
m3.mostrarDatos()

