class Mascota:
    especie=''
    nombre=''
    edad=0
    sexo=''
    castrado=False

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

m1=Mascota()
m1.especie='Perro'
m1.nombre='Pichi'
m1.edad=1
m1.sexo='H'


m1.mostrarDatos()

m2=Mascota()
m2.especie='Gato'
m2.nombre='Michi'
m2.edad=6
m2.sexo='M'
m2.castrado=True

m2.mostrarDatos()