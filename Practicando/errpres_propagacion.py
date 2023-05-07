
def programa():
    print("Un monton de código")

f = 2



def funcion(x, y):
    print('antes')
    # try:             #No siempre se hace el control en la función base, sino que se puede
                    # hacer en la final y controlarlo ahí, por si consume muchas funciones
                    #para no tener 200 mil try ad excep en cualquier lado
        # div = x/y
    div = x/y
    # except ZeroDivisionError:
    #     print("Logueo todo")
    #     raise ValueError("Parametros incorrectos")
    
    print('Después')
    return div

def main():
    x = float(input('x: '))
    y = float(input('y: '))

    try:
        print(function(x, y)) #Se puede controlar acá, al final
    except ZeroDivisionError as error:
        print("Pusiste un cero no seas gil")
    except BaseException:    
        print("La funcion no anda")
    print("Listo")


main()