import ejercicio_integrador_excepciones


class Persona():
    def __init__(self, nombre="", edad=0, dni=""):
        self.nombre = nombre
        self.edad = edad
        self.dni = dni
        # De esta forma estaría seteando directamente las variables "privadas"
        # pero al no usar las properties me perdería las validaciones
        # self.__nombre=nombre
        # self.__edad=edad
        # self.__dni=dni

    @property
    def nombre(self):
        return self.__nombre

    @property
    def edad(self):
        return self.__edad

    @property
    def dni(self):
        return self.__dni

    @nombre.setter
    def nombre(self, nuevo_valor):
        self.__nombre = nuevo_valor

    def __validar_dni(self, numero):
        try:
            dni = int(numero)
        except ValueError:
            mensaje = f"Creación de Persona con DNI incorrecto: {dni}"
            print(mensaje)
            raise ejercicio_integrador_excepciones.PersonaDatoInvalidoError(mensaje)

        if len(str(dni)) < 7:
            mensaje = f"Creación de Persona con DNI incorrecto: {dni}"
            print(mensaje)
            raise ejercicio_integrador_excepciones.PersonaDatoInvalidoError(mensaje)

    @dni.setter
    def dni(self, nuevo_valor):
        self.__validar_dni(nuevo_valor)
        self.__dni = int(nuevo_valor)

    @edad.setter
    def edad(self, nuevo_valor):
        if nuevo_valor < 0:
            mensaje = f"Creación de Persona con Edad incorrecta: {nuevo_valor}"
            print(mensaje)
            raise ejercicio_integrador_excepciones.PersonaDatoInvalidoError(mensaje)
        else:
            self.__edad = nuevo_valor

    def mostrar(self):
        return f"Nombre: {self.nombre},Edad: {str(self.edad)},DNI: {self.dni}"

    def es_mayor_de_edad(self):
        return self.edad >= 18


# Prueba de utilización de código
juan = Persona("Alejandro", 39, "299500188")
print(juan.mostrar())
juan.nombre = "Alberto"
print(juan.mostrar())
if juan.es_mayor_de_edad():
    print(f"Juan es mayor de Edad")
else:
    print("Juan es menor")
pedro = Persona("Pedro", 2, 23)

class Cuenta():

    def __init__(self, titular, cantidad=0):
        self.titular = titular
        self.__cantidad = cantidad

    @property
    def titular(self):
        return self.__titular

    @property
    def cantidad(self):
        return self.__cantidad

    @titular.setter
    def titular(self, titular):
        self.__titular = titular

    def mostrar(self):
        print(
            f"Cuenta-> Titular:{self.titular.mostrar()}, Cantidad:{str(self.cantidad)}")

    def ingresar(self, cantidad):
        if cantidad > 0:
            self.__cantidad = self.__cantidad + cantidad

    def retirar(self, cantidad):
        if cantidad > 0:
            self.__cantidad = self.__cantidad - cantidad

from ejercicio_integrador_6 import Persona
from ejercicio_integrador_7 import Cuenta
import ejercicio_integrador_excepciones


class CuentaJoven(Cuenta):

    def __init__(self, titular, cantidad=0, bonificacion=0):
        super().__init__(titular, cantidad)
        self.bonificacion = bonificacion

    @property
    def bonificacion(self):
        return self.__bonificacion

    @bonificacion.setter
    def bonificacion(self, bonificacion):
        self.__bonificacion = bonificacion

    def mostrar(self):
        print(f"Cuenta Joven -> Titular: {self.titular.mostrar()}, Cantidad: {self.cantidad}, Bonificación: {self.bonificacion}%")

    def es_titular_valido(self):
        return self.titular.edad < 25 and self.titular.es_mayor_de_edad()

    def retirar(self, cantidad):
        if not self.es_titular_valido():
            mensaje = f"El titular {self.titular} no puede retirar dinero porque es inválido"
            print(mensaje)
            raise ejercicio_integrador_excepciones.CuentaJovenTitularInvalidoError(mensaje)
        elif cantidad > 0:
            super().retirar(cantidad)


# Pruebas de código
juan = Persona("Juan", 20, 29950189)
cuenta_juan = CuentaJoven(juan, 20.5, 10)
cuenta_juan.ingresar(30.2)
cuenta_juan.retirar(1)
cuenta_juan.mostrar()