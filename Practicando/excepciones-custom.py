import traceback

def funcion(x, y):
    print('antes')
    div = x/y
    print('Después')
    return div

def main():
    x = float(input('x: '))
    y = float(input('y: '))

    try:
        print(funcion(x, y))
    except BaseException as ex:
        print("Ocurrio un error inesperado: ", traceback.print_exc())
        print("Algo salió mal")
    print("Listo")

main()