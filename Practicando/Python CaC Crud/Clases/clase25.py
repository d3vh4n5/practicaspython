def mifunc(**kwargs):
    for x in kwargs:
        print(x) #imprime claves
        print(kwargs[x]) #imprime valores)
#mifunc(x=3, nombre="juan", b=True)

def suma(**kwarg):
    subtotal=0
    for key, val in kwarg.items():
        subtotal += val
        print(subtotal)
    return subtotal

#print (suma(a=1, b=44, c=70))

def func (a, b,c, *args,**kwargs):
    print("a ",a, "b- ",b, "c- ",c)
    for arg in args:
        print("args- ", arg)
    for k,d in kwargs.items():
        print(k, "--", d)

#print (func(1, "pepe", True, 23,"Jose", 55.4, True, nombre="Juan", edad=55, altura=1.78))

def func (a, b,c, *args,**kwargs):
    print("a ",a, "b- ",b, "c- ",c)
    for arg in args:
        print("args- ", arg)
    for k,d in kwargs.items():
        print(k, "--", d)
tupla=( 23,"Jose", 55.4, True)
#dic={"nombre":"Juan", "edad":55, "altura":1.78}
#print (func(1, "pepe", True,*tupla, **dic))

