variable = 2
variable2 = 3

#print(variable + variable2)
text = "hola soy una linea" \
    "Hola soy otra linea"
#print(text)

x=0
def function():
    x=1
    def function_interna():
        x=2
        print (f"Local scope x={x}")
    function_interna()
    print(f"Enclosed scope x={x}")
#function()
#print("El valor de x es=", x)
#print(f"Global scope x={x}")

