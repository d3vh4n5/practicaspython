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


''' Concatenacion '''

# nombre = "Ana"
# apellido = "Lopez"
# # print(nombre +' ' + apellido)

# # #Para hacer una concatenación tienen que ser o ambos texto o ambos numeros.

# nomape=nombre+apellido
# print(nomape)
# print(nomape*6) #Puedo acá multiplicar un string por 6 y me imprime el strng todas esas veces

# edad = 32
# nombre = "Claudia"
# # no se puedeprint(nombre +' ' + edad)
# print(nombre,edad) #así se puede
# print("nombre: ",nombre, "Edad: ", edad)

""" Operadores de asignacion """

# nro=10
# nro=nro+20
# print(nro)
# nro+=20
# print(nro)
# nro*=20
# print(nro)
# nro/=5
# print(nro)

""" Operadores de pertenencia """

# dato = [4,5,6,8,99]
# print(99 in dato)
# print(99 not in dato)
# print(47 in dato)
# print (47 not in dato)

"""Entrada y salida de datos"""

#print('Al print ya lo conocemos, veamos el siguiente')

"""
ENTRADA DE DATOS: input()
Pide un dato al usuario.Dentro de los paréntesis se puede poner un texto que
 le indique al usuario qué es lo que se espera que ingrese.

IMPORTANTE!!!!!!!! todo dato ingresado, ingresa como cadena de texto
(aunque sea un número). Para poder operar con números ingresados por input,
 hay que convertirlos.

"""

# nombre=input('Ingrese su nombre ')
# print("Hola, ",nombre)


# #nombre=input('Ingrese su nombre ') #lo que ingreso con input() tiene que ser solo texto
# #print("Hola, ",nombre)
# nro=input("Ingrese un numero")

# print(type(nro)) #me dice que tipo de dato es
# nroint=int(nro)
# print(type(nroint)) #me dice que tipo de dato es

# nrofl=float(nro) #Lo convertimos en decimal
# print(type(nrofl)) #me dice que tipo de dato es

# total=nroint*1.21 #lo convierto en un entero
# print(total)

# nacimiento=int(input("Ingrese año de nacimiento ")) #tambipen se puede hacer de esta manera
# edad = 2022-nacimiento
# print("Edad: ", edad)


#tambien asi
#print(2022-int(input('Ingrese año de nacimiento ')))

print(type(45))
print(type(str(45)))
