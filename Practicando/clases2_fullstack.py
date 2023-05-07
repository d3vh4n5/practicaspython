class Vehiculo():

    def __init__(self, color, ruedas):
        self.color= color
        self.ruedas= ruedas
    
    def __str__(self):
        return "Color: {} - Ruedas: {}".format(self.color, self.ruedas)
    
    def calcular_precio(self):
        return 20
    

# Herencia simple: de una única superclase

class Auto(Vehiculo):

    def __init__(self, color, ruedas, velocidad):
        super().__init__(color, ruedas) # llamo al init de la super clase para poder incializar sus parámetros
        self.velocidad = velocidad
    
    # sobreescritura / redefinición del método especial
    def __str__(self):
        return super().__str__() + " - Velocidad : " + str(self.velocidad)
    
    # def __str__(self):
    #     return " - Velocidad : " + str(self.velocidad)
    
class Moto(Vehiculo):
    def __init__(self, color, ruedas, velocidad, casco):
        super().__init__(color, ruedas)
        self.casco = casco

    def calcular_precio(self):
        return super().calcular_precio() + 5
    
class Bicimoto(Moto):
    def __init__(self, color, ruedas, velocidad, casco, ruido):
        super().__init__(color, ruedas, velocidad, casco)
        self.ruido = ruido
    
    # def precio(self):
    #     super().precio
    #     self.precio
    #     return 5
    

#programa principal

v1= Vehiculo("Blanco", 2)
a1= Auto("Rojo", 4, 140)
a2= Auto("Negro", 4, 180)
a3= Auto("Azul", 4, 200)
moto_1 = Moto("Amarilla", 2, 120, True)
bicimoto_1 = Bicimoto("Amarilla", 2, 120, True, 'Altisimo')

print('Accediendo el método de moto ya que bicimoto no tiene precio: ',bicimoto_1.calcular_precio())

vehiculos = []
vehiculos.append(v1)
vehiculos.append(a1)
vehiculos.append(a2)
vehiculos.append(3)
vehiculos.append(a3)
vehiculos.append(moto_1)
vehiculos.append(bicimoto_1)

# Polimorfismo: Cuando distintos objetos pueden recibir el mismo mensaje

for item in vehiculos:
    #print(isinstance(item, Vehiculo))
    if isinstance(item, Vehiculo):
        print('El precio es ' +  str(item.calcular_precio()))

# print(v1)
# print(a1)
# print(a2)
# print(a3)
# print(moto_1)
# print(bicimoto_1)