# https://colab.research.google.com/drive/1S6CFjR7sA1KzEJ3IktIL21bomSK9t9yn#scrollTo=WRgBW8DaGuZV


# for i in range(2, 10, 3):
#     print (i)

# cadena="Hola que tal"

# print(len(cadena))
# for i in cadena:
#     print(i)

# print(cadena[3])

#tupla = (0, True, "hola", 2345, [89, False], "pepe", "Rino")
#print(tupla[2])
#tupla[2]= "pepe" Esto de error y no funciona

lista = [0, True, "hola", 2345, [89, False], "pepe", "Rino"]
longitud = len(lista)
for i in range(longitud):
    print("elemento", i+1, ":", lista[i])