# lista=[0, True, "hola", 2345, [89, False], "pepe", "Rino"]
# for i in range(6):
#    if i==3:
#       pass
#    else:
#       print(lista[i])
# print("Chauuuuu")

arts=[
    ["Articulo 1", 1200, 100],
    ["Articulo 2", 5000, 50],
    ["Articulo 3", 4000, 200],
    ["Articulo 4", 2200, 150]
    ]
#print(arts[1][0])
#for elem in arts:
 # print(elem)
for i in range(len(arts)):
  if arts[i][2]>100:
     pass
  else:
     print("Articulo: ",arts[i][0])
     print("Precio: ", arts[i][1])
     print("Stock:", arts[i][2])


def sumar(n1, n2):
   sumatoria=n1+n2
   return sumatoria
print(sumar(10,30))
print(sumar(10,30)*0.21)
s1=sumar(3, 70)
s2=sumar(7,567)
print(s1+s2)


def sumar(n1, n2):
   return n1+n2
print(sumar(45,6))
print(sumar(sumar(10,20),sumar(35,15)))