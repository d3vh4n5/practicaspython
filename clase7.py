""" Modulo encargado de calculos matemáticos """
import math


def mcd(n, m):
    """Función que calcula el máximo común divisor de dos números utilizando el algoritmo de eucliedes.
    Parámetros:
        - n: Es un número entero.
        - m: Es un número entero.
    Devuelve:
        El máximo común divisor de n y m.
    """
    dividendo = 0
    while (m > 0):
        dividendo = m
        m = n % m
        n = dividendo
    return n


mcd(7, 21)


def mcd_2(n, m):
    return math.gcd(n, m)

# ejercicio2


def mcm(n, m):
    """Función que calcula el mínimo común múltiplo de dos números.
    Parámetros:
        - n: Es un número entero.
        - m: Es un número entero.
    Devuelve:
        El mínimo común múltiplo de n y m.
    """
    if n > m:
        mayor = n
    else:
        mayor = m
    while (mayor % n != 0) or (mayor % m != 0):
        mayor += 1

    return mayor

# ejercicio 3


def contar_palabras(texto):
    """Función que cuenta el número de veces que aparece cada palabra en un texto.
    Parámetros:
        - texto: Es una cadena de caracteres.
    Devuelve:
        Un diccionario con pares palabra:frecuencia con las palabras contenidas en el texto y su frecuencia.
    """
    texto = texto.split()
    palabras = {}
    for i in texto:
        if i in palabras:
            palabras[i] += 1
        else:
            palabras[i] = 1
    return palabras


texto = 'Como quieres que te quiera si el que quiero que me quiera no me quiere como quiero que me quiera'
print(f"Cantidad de palabras: {contar_palabras(texto)}")

def contar_palabras(texto):
    """Función que cuenta el número de veces que aparece cada palabra en un texto.
    Parámetros:
        - texto: Es una cadena de caracteres.
    Devuelve:
        Un diccionario con pares palabra:frecuencia con las palabras contenidas en el texto y su frecuencia.
    """
    texto = texto.split()
    palabras = {}
    for i in texto:
        if i in palabras:
            palabras[i] += 1
        else:
            palabras[i] = 1
    return palabras


def mas_repetida(palabras_dict):
    max_palabra = ''
    max_freq = 0
    for palabra, freq in palabras_dict.items():
        if freq > max_freq:
            max_palabra = palabra
            max_freq = freq
    return max_palabra, max_freq


texto='Como quieres que te quiera si el que quiero que me quiera no me quiere como quiero que me quiera'
print(f"Cantidad de palabras: {contar_palabras(texto)}")
print(f"(Palabra mas repetida, frecuencia) -> {mas_repetida(contar_palabras(texto))}")

# Otras resoluciones
# lista_frecuencias = list(diccionario.values())                          # values()	Returns a list of all the values in the dictionary
# frecuencia_maxima = max(lista_frecuencias)
# indice_palab_mas_freq= lista_frecuencias.index(frecuencia_maxima)       # index()	Returns the index of the first element with the specified value
# lista_tuplas=list(diccionario.items())                                  # items()	Returns a list containing a tuple for each key value pair
# resultado=lista_tuplas[indice_palab_mas_freq]

# def tupla_palabra_frecuencia_mas_repetida(cadena):
#     diccionario_palabras_frecuencias = ejercicio3.diccionario_palabras_y_frecuencia(cadena)
#     diccionario_ordenado_frecuencias_reversa = sorted(diccionario_palabras_frecuencias.items(), reverse=True, key= lambda x:x[1])
    
#     return (diccionario_ordenado_frecuencias_reversa[0][0], diccionario_ordenado_frecuencias_reversa[0][1])

# print(tupla_palabra_frecuencia_mas_repetida(ejercicio3.cadena))


'''Ejercicio 5'''

def get_int():
    ingreso_correcto = False
    while not ingreso_correcto:
        user_input = input('Ingrese un número entero: ')
        try:
            valor = int(user_input)
        except ValueError:
            print('No es un entero válido. Intente nuevamente!')
        else:
            ingreso_correcto = True

    return valor


print(f"Número ingresado: {get_int()}")

#recursivo:

def get_int2():
    user_input = input('Por favor ingrese un número: ')
    try:
        value = int(user_input)
    except ValueError:
        print('No es un entero válido. Intente nuevamente!')
        return get_int()
    else:
        return value


print(f"Número ingresado: {get_int()}")