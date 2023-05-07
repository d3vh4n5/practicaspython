import random
import re

class Dado:
    def __init__(self):
        self.__valor =1
    
    def tirar(self):
        self.__valor = random.randint(1, 6)

    def imprimir(self):
        print(f"Salio: {self.__valor}")
    
    def obtener_valor(self):
        return self.__valor
    def __repr__(self): #Esto nos dice como se representa un string o una variable en un debugger
        return f"Dado ({self.__valor})"
    def __str__(self): #Esto nos dice como se representa un string o una variable en el print de la consola
        return f"{self.__valor}"
    
    @property
    def valor(self):
        return self.__valor
    
    @valor.setter
    def valor(self, pNuevoValor):
        if pNuevoValor > 6 or pNuevoValor <= 0:
            print("No sepuede haver")
        else:
            self.__valor = pNuevoValor

class JuegoDado:
    def __init__(self):
        self.dado_1 = Dado()
        self.dado_2 = Dado()
        self.dado_3 = Dado()
    
    # def __tirardados(self):# esto es un método auxiliar
    #     self.dado_1.tirar()
    #     self.dado_2.tirar()
    #     self.dado_3.tirar()

    def jugar(self):
        #self.__tirardados()
        self.dado_1.tirar()
        self.dado_1.imprimir()
        self.dado_2.tirar()
        self.dado_2.imprimir()
        self.dado_3.tirar()
        self.dado_3.imprimir()

        #if self.dado_1._JuegoDado__valor == self.dado_2._JuegoDado__valor == self.dado_3._JuegoDado__valor: # Esto funciona pero no se debería hacer, porque si bien en pythopnse puede acceder, debería ser un atributo pribado
        #    print("Ganaste")

        self.dado_1.valor = 12

        if self.dado_1.valor == self.dado_2.valor == self.dado_3.valor:
            print("ganó")

        if self.dado_1.obtener_valor() == self.dado_2.obtener_valor() == self.dado_3.obtener_valor():
            print("Ganaste")
        else:
            print("Perdiste")
    
mi_juego = JuegoDado()
mi_juego.jugar()

