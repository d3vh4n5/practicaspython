# Paquete distribuible

# Funciona todo exactamente igual como si estuviera la carpeta a la misma
# altura que este archivo

# Módulos

import modulo
import modulo as m
from modulo import funcion1, funcion2
from modulo import funcion3 as fn3
from modulo import *

import paquetes.modulo1
import paquetes.modulo1 as mipaquete
from paquetes.modulo1 import *

import paquetes.subpaquetes.modulo3
from paquetes.subpaquetes.modulo3 import module3
from paquetes.subpaquetes.modulo3 import module3 as m3
from paquetes.subpaquetes import modulo3 as mm3

# Modulo

modulo.funcion1
modulo.funcion2

funcion1()
funcion2()
funcion3()
funcion4()

# Paquetes

paquetes.modulo1.modulo1()
paquetes.modulo1.modulo2()
modulo1()
modulo2()
mipaquete.modulo1()
mipaquete.modulo2()

# Subpaquetes

paquetes.subpaquetes.modulo3.module3()
module3()
m3()
mm3.module3()
