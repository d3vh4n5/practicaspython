

def promediar(nro):
    subtotal = 0
    for i in range(nro):
        subtotal += float(input("Ingrese cifra: "))
    print(subtotal/nro)
#promediar(int(input("Cuántos números quiere promediar")))

#si tengo el inicio y el fin uso el for, si no se cuando va a terminar uso un while

def contar(ini, fin):
    for i in range(ini, fin+1):
        print (i)

#contar(int(input("Desde qué número ")), int(input("hastaqué número ")))

#El range tiene un tercer parametro que son los pasos (x, y, z) Donde z serian los pasos
#estos pueden ser negativas e ir de atrás para adelante según se prefiera

def sumar(*args): #args es una tupla, es como una lista pero no se puede modificar
    subtotal = 0
    for i in args:
        subtotal += i
    print (subtotal)

#sumar()
#sumar(3)
#sumar(3,56,321,1,23,2)

def promediar(*args):
    if not len(args): # len(args) == 0
        print("no se puede")
    else:
        subtotal = 0
        for i in args:
            subtotal += i
        print(subtotal / len(args))

promediar (10, 20)
promediar(3,7,9)
promediar()

#explicación de diccionarios quedó en colab