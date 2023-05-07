# 1 Escribir una funcion que calcule el máximo compun divisor entre dos números.
'''
    elegir al mas chico
    usar la funcion que dice si el resto es cero desde el 1 hasta el numero en cuestión
    Cada vez que el resto sea cero, agregar el número a una lista
    incluir el propio número a la lista
    obtener el max(lista)
    tomar el numero más alto y hacer lo del resto y guardado en una lista
    el numero max que habíamos obtenido, preguntar si está en la lista
    si es correcto devolverlo, sino preguntar por el anterior
'''

# #operaciones basicas

# # numero = 10
# # print(numero)
# # print(numero+5)
# # print(numero-3)
# # print(numero*7)
# # print(numero/5)
# # print(numero**2) #potencia
# # print(numero//3) #parte entera de la division
# # print(numero%3) #reso de la division

# def crearListaMin(n):
#     lista = []
#     for i in range(1, n):
#         if n%i == 0:
#             lista.append(i)
#     lista.append(n)
#     return lista

# def maxDiv(a, b):
#     if a<b:
#         lista = crearListaMin(a)
#         m = b
#     else:
#         lista = crearListaMin(b)
#         m = b
#     for i in range(len(lista)):
#         d= max(lista)
#         if m%max(lista) == 0:
#             print('El maximo común divisor es: ', d)
#             break
#         else:
#             lista.pop(-1)

# def intento2(a, b):
#     lista = []
#     if a<b:
#         for i in range(1, a):
#             if b%i == 0 and i<=a/2:
#                 lista.append(i)
#     else:
#         print("toy en else")
#         for i in range(1, b):
#             if a%i == 0 and i<=b/2:
#                 lista.append(i)
#     print("el MCD es: ", max(lista))

'''
    Python trae una funcion que ya hace el mcd, es "math.gcd!"  
'''

def intento3(a, b):
    lista = []
    for i in range(1, min(a, b)):
        if max(a, b)%i == 0 and i<=min(a, b)/2:
            lista.append(i)
    print("El MCD es: ", max(lista))

# maxDiv(44, 242)
# intento2(44, 242)
# intento3(44, 242)
# intento3(98, 56)
# intento3(1, 56)

def mcd(a, b):
    if a == 0:
        return b
    return mcd(b%a, a)

# 2 Minimo común múltipo entre 2 números

def minMult(a, b):
    lista1 = [a]
    lista2 = [b]
    lista3 = []
    while len(lista3) == 0:
        for i in range(len(lista1)):
            print(i)
            if lista1[i] in lista2:
                lista3.append(lista1[i])
            else:
                lista1.append(a*(i+1))
                lista2.append(b*(i+1))
    print("El mínimo común múltiplo es: ",lista3[0])
            

# minMult(-2, -3)

# 3 programa que reciba un string, y devuelva un diccionario con cada palabra que contiene y la cantidad de veces que aparece(frecuencia)

def contadorPalabras(cadena):
    palabras = cadena.split()
    cantidades=[]
    for i in range(len(palabras)):
        cantidades.append(0)
        for j in range(len(palabras)):
            if palabras[i] == palabras[j]:
                cantidades[i] += 1

    ziped = zip(palabras, cantidades)
    print(dict(ziped))

#contadorPalabras('Hola que tal hola como que tal')

# 4 la funcion anterior pero que devuelva el diccionario
# y lo tome otra función que devuelva la palanra más repetida y su frecuancia

def contadorPalabras2(cadena):
    palabras = cadena.split()
    cantidades=[]
    for i in range(len(palabras)):
        cantidades.append(0)
        for j in range(len(palabras)):
            if palabras[i] == palabras[j]:
                cantidades[i] += 1

    ziped = zip(palabras, cantidades)
    return dict(ziped)

def palabraMasRepetida(dic):
    claves = list(dic.keys())
    valores = list(dic.values())
    print("La palabra que mas veces aparece es: '",claves[valores.index(max(valores))], "' Y aparece ", max(valores), ' veces')


#palabraMasRepetida(contadorPalabras2('hola que tal tal tal tal es tu hola que tal tal es tu'))


''' # 5 
Sabiendo que ValueError es la excepción que se lanza cuando no podemos convertir
una cadena de texto en su valor numérico. Escriba una funcion get_int() que lea el
valor entero del usuario y lo edvuelva, iterando mientras el valor no sea correcto.
Intente resolver el ejercicio tanto de manera iterativa como recursiva.
'''
# Forma recursiva
def get_int(entero):
    try:
        print("El numero introducido es: ", int(entero))
        print('Fin')
    except ValueError as ve:
        print('Error, tipo de valor incorrecto, intente denuevo  ', ve)
        get_int(input('Introduzca un valor numérico: '))

#get_int(input('Introduzca un valor numérico: '))

def get_int(entero):
    control = True
    while control:
        try:
            var = int(entero)
            assert (isinstance(var, int)), "Error: el número no es de tipo entero"
            print('Valor correcto. Valor introducido: ', var)
            control = False
        except AssertionError as ass:
            print(ass)
            entero = input('Ingrese otro valor: ')
        except ValueError as ve:
            print('Error, tipo de valor incorrecto, intente denuevo  ', ve)
            entero = input('Ingrese otro valor: ')
        else:
            print('Fin de este maravilloso programa')

#get_int(input('Introduzca un valor numérico: '))

'''
6 clase persona con nombre edad i DNI. 
    Metodo constructor donde los datos pueden estar vacios
    setters y getters para cada uno de los atributos. hay que validar las entradas ed datos
    mostrar() que muestre los datos de la persona
    es_mayor_de_edad() Que devuelva true sie s mayor de 18
'''

class Persona():
    # def __init__(self, nom, ed, d):
    def __init__(self):
        self._nombre = ''
        self._edad = 0
        self._dni = ''
    
    @property
    def nombre(self):
        return self._nombre
    
    @nombre.setter
    def nombre(self, pNombre):
        self._nombre = pNombre
    
    @property
    def edad(self):
        return self._edad
    @edad.setter
    def edad(self, n):
        try:
            n = int(n)
        except ValueError as ve:
            print("Tiene que ingresar un string", ve)
        if n >0:
            self._edad = n
        else:
            print('No puede ingresar un numero negativo ni 0')
    
    @property
    def dni(self):
        return self._dni
    
    @dni.setter
    def dni(self, n):
        try:
            n = int(n)
        except ValueError as ve:
            print("Tiene que ingresar un string", ve)
        if n >0:
            self._edad = n
        else:
            print('No puede ingresar un numero negativo ni 0')
    
    def mostrar(self):
        print('Nombre: ', self._nombre, ' Edad: ', self._edad, ' DNI: ', self._dni)

    def es_mayor_de_edad(self):
        return self._edad>18
    
# pablo = Persona()
# pablo.nombre = 'pablo'
# pablo.edad = 0
# print(pablo)

'''
 7 Crear una clase llamada Cuenta que tendrá los siguientes atributos: 
 titular : que es una persona
 cantidad : que puede tener decimales.

 El titular será obligatorio y la cantidad será opcional. Crear los sig metodos:

 Constructor, donde los datos pueden iniciar vacioos
 Setters y getters para c/u de los atributos. El atributo no se puede
 modificar directamente, sólo ingresando o retirando dinero.
 mostrar(): Muestra los datos de la cuenta.
 ingresar(cantidad): se ingresa una cantidad a la cuenta, so la cantidad 
 introducida es negativa, no se hará nada.
 retirar(cantidad): se retira una cantidad a la cuenta. La cuenta puede estar en
 numeros rojos. (Por lo que validad que alcance la cantidad e la cuenta con la 
 cantidad a retirar)
'''

class Cuenta:
    def __init__(self, persona, saldo):
        self._titular = persona
        self._cantidad = saldo
    
    @property
    def titular(self):
        return self._titular
    
    @titular.setter
    def titular(self, persona):
        self._titular = persona
        pass
    
    @property
    def cantidad(self):
        return self._cantidad

    @cantidad.setter
    def cantidad(self, n):
        pass

    def mostrar(self):
        print('Nombre: ', self._titular['nombre'])
        print('Edad: ', self._titular['edad'])
        print('DNI: ', self._titular['dni'])
        print('Saldo: ', self._cantidad)
    
    def ingresar(self, n):
        if n > 0:
            self._cantidad += n
        else:
            print('Solo se admiten números positivos')
    def retirar(self, n):
        if n > 0:
            if n <= self._cantidad:
                print('Has retirado: ', n)
                self._cantidad -= n
                print('Saldo restante: ', self._cantidad)
            else:
                print('Saldo insuficiente para realizar la transacción')
        else:
            print('No pued eingresar números negativos')


# print("Ejercicio 7")
# obj = Cuenta({"nombre" : "Mariela", "edad" : 32, "dni" : "33213212"}, 100)
# #obj.titular = {"nombre" : "Mariela", "edad" : 32, "dni" : "33213212"}
# obj.ingresar(50)
# obj.retirar(20)
# obj.mostrar()

'''
    8

    Definir una "Cuenta Joven", que deriva de la clase anterior
    cuando se crea esta clase, ademas de titular y la cantidad, 
    se debe guardar una bonificación que estará expresada en tanto por ciento.
    Crear los sig metodos:
    Constructor
    Setters y getters
    En esta ocación los titulares de este tipo de cuenta tienen que ser mayor
    de edad por lo tanto hay un que crear un metodo es_titular_válido() que
    devuelve verdadero si el titular es mayor de edad pero menor de 25 años
    y falso en caso contrario.
    Además, la retirada de dinero solo se podrá hacer si el titular es válido.
    El método mostrar() debe devolver el mensaje de "Cuenta Joven" y la bonificacion
    de la cuenta.
'''

class CuentaJoven(Cuenta):

    def __init__(self, persona, saldo, bon):
        Cuenta.__init__(self, persona, saldo)
        self._bonificacion = bon

    @property
    def cuenta(self):
        return self.mostrar()
    
    @cuenta.setter
    def cuenta(self, persona, saldo):
        self._titular = persona
        self._cantidad = saldo
    
    @property
    def bonificacion(self):
        return self._bonificacion
    
    @bonificacion.setter
    def bonificacion(self, n):
        self._bonificacion = n
    
    def es_titular_valido(self):
        return self._titular['edad'] > 18 and self._titular['edad'] < 25
    
    def retirar(self, n):
        if self.es_titular_valido():
            self._cantidad -= n
            print("Restiraste: ", n)
        else:
            print('No puedes retirar ya que no esres un "joven"')
    
    def mostrar(self):
        print('======================')
        print('Cuenta Joven')
        super().mostrar()
        print('Bonificacion: ',self._bonificacion,'%')
        print('======================')

# joven = CuentaJoven({"nombre" : "Matias", "edad" : 21, "dni" : "33213212"}, 200, 10)
# joven.mostrar()

