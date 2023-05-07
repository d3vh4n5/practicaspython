que_soy = (4,5,6,"hola",True)
#print (type(que_soy))
lista1=list(que_soy)
#print(type(lista1))

lista2=lista1 #Cuando uno hace esto, le asigna un nuevo nombre al mismo lugar de memoria, NO LA COPIA
#print(lista2)
lista2.append("Gato")
#print(lista2)
#print(lista1)
#id acá es el lugar reservado en memoria
#print(id(lista1))
#print(id(lista2))#tienen las 2 el mismo id porque ES LA MISMA

#aspi copiamos la lista:

#lista2=lista1.copy()
#lista2.append("Hipopotamo")
#print(lista2)
#print(lista1) #vemos ahora que si son lista distintas y el append si hiso en 1 sola lista

#lista2.append(lista1) #agrega la lista como un elemento dentro de la otra lista
#print(lista2)

#lista2.extend(lista1) #concatena una lista con la otra
#print(lista2)

#lista2.clear() #borra todos los elementos de la lista
#print(lista1)
lista1.pop(-1)#de atrás para adelante elimina
#print(lista1)

#//////////////// FUNCIONES EN PYTHON//////////////////////
''' Comentario multilinea se hace con 3 comillas, sea simples o dobles
a="Ejemplo"
print(id(a))
a="Otro Ejemplo"
print(id(a))
print(a[2])
#a[2]=x Los strings son iterables, pero no son modificables, el string es inmutable
'''
'''
a=[10,20]
print(id(a))
a=[20,22]
print(id(a))
a[1]=100
print(a)
print(id(a))
'''


'''
a=(29¿0,40,50)
print(id(a))
#a[0]=50   --> no puedo moficar ningun valor de una tupla
a=(30,66,700)
print(id(a))
'''

#otra forma de imprimir, los "f-strings"
'''
nombre="juan"
apellido="Perez"
edad=33
print("el alumno: ", nombre, apellido, "edad: ", edad)
print(f"el alumno {nombre} - {apellido} tiene una edad de {edad}")
print(
    f"nombre :  {nombre} \n"
    f"Apellido: {apellido}\n"
    f"Edad:     {edad}"
)
'''
'''
n1=10
n2=20
print(f"multiplico {n1} y {n2}: {n1*n2}")
print(f"{n1} es mayor que {n2}? {n1>n2}")

#condicionaes en f-strings

personas=[['Ana', 44],['Juan', 11],['Sol', 33]]
for elem in personas:
    print(f'¿{elem[0]} es mayor de edad?{True if elem[1]>=18 else False}')
s="SI"
n="NO"
for elem in personas:
    print(f'¿{elem[0]} es mayor de edad?{s if elem[1]>=18 else n}')
'''
'''
def opcion(a):
    if a%2==0:
        return 'Par'
    else:
        return 'Impar'

nro=int(input('Ingrese un número: '))
print(f'{nro} es un numero {opcion(nro)}')
'''
import datetime


t=datetime.time(19,24,35,500) # Seteamos la hora (hora, minutos, segundos, milesimas)
print(t)
print('Hora', t.hour)
print('Minutos', t.minute)
print('Segundos', t.second)

print('mas temprano', datetime.time.min)
print('mas tarde', datetime.time.max)
print('Resolution', datetime.time.resolution)

hoy=datetime.date.today() #nos trae la fecha del día
print(hoy)

print(f"fecha actual: {hoy.ctime()}")#ctime() te convierte la fecha en un string

tt=hoy.timetuple()#lo convierto en una tupla
print(tt) #puedo ver todos los atributos de la tupla, util para ver todo el contenido de datetime
print('tupla: Año: ', tt.tm_year)
#tt.tm_mon es para el mes
#tt.tm_mday es el dia del mes
#tt.tm_wday es el dia de la semana
#tt.tm_isdst es para el ahorro ed energia (en paises que hay horario para el mismo)


