
#Excepciones múltiples
def SaldoNegativoException(Exception):
    pass

try:
    n = float(input("Ingrese un número divisor: "))
    5/n
    #raise SaldoNegativoException("Dio negativo la sube") #exceptiones custom
# La idea es empezar desde las ramas mas pequeñas del arbol de errores
# Sinó saltara un error generalizado y se perderá especificidad del error
# Lo que complicará la operación de debugeo
# except Exception as e:
#     print("error")
# except TypeError:
#     pass            Estoe s guardar la basura debajo de la alfonbra, no se hace a menos que se quiera pasar el error a otra cosa.
except TypeError:
    print("No se puede dividir el número entre una cadena")
except ValueError:
    print("Debes introducir una cadena que sea un número")
except ZeroDivisionError as ze:
    print("No puede dividir por cero, pruebe otro número")
except Exception as e:
    print("Ha ocurrido un error no previsto", type(e).__name__)
else:
    print("Este sistema es la gloia")



print("Sigo con las operaciones locas")