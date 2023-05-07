
# import pprint

# def conectar():
#     print("Esta es la función conectar y no retorna nada")

# #aca la ejecuto
# conectar()

# class Persona:
#     nombre = ''
#     edad = 0
#     sexo = ''

# maria = Persona()
# maria.nombre = 'Maria Goyete'
# maria.edad = 23
# maria.sexo = 'F'

# class errorLoco(Exception):
#     print('toy dentro del error loco')

# try:
#     raise errorLoco
#     print(vars(maria))
#     print('----------------')
#     pprint.pprint(maria)
# except Exception as ex:
#     print('Hubo un error: ', ex)

def sumar(args):
    print('Vamos a sumar: ', args, ' De largo: ', len(args))
    total = 0
    for i in args:
        total += i
    print('Resultado: ', total)

tupla = (1, 3, 2)
lista = [1, 2, 3]

sumar(tupla)
sumar(lista)