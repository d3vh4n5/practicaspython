from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod # Indicamos que va a ser un método abstracto
    def mover(self):
        pass

    @abstractmethod # Indicamos que va a ser un método abstracto
    def emitir_sonido(self):
        print("Aminal emite sonido: ", end="")
    
    def hacer_caca(self):
        print("Haciendo popo..")

class Gato(Animal): #Creo la clase Gato que hereda de Animal
    def mover(self):# Le doy al método abstracto un comportamiento particular
        print("El gato hace se mueve.")

    def emitir_sonido(self): # Sobreescribo el metodo abstracto
            #Agregándole comportamiento al método anterior
        super().emitir_sonido() #Aprovecho la superclase animal y llamo a su
        print("Miau!")# Le agrego algo propio

class Perro(Animal): #Creo la clase Gato que hereda de Animal
    def mover(self):# Le doy al método abstracto un comportamiento particular
        print("El gato hace se mueve.")

    def emitir_sonido(self): # Sobreescribo el metodo abstracto
            #Agregándole comportamiento al método anterior
        super().emitir_sonido() #Aprovecho la superclase animal y llamo a su
        print("Guau!, Guau!")# Le agrego algo propio

# animal = Animal() # Bo se peudeinstanciar una clase abstracta, dará error
gato = Gato()
perro = Perro()

gato.emitir_sonido()
perro.emitir_sonido()

