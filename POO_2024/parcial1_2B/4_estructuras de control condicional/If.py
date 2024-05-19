"""
Existe una estructura de condicion llamada "if"
La cual evalua una condicion para encontrar el valor del "TRUE" o se cumple
la condicion se ejecuta la lina o lineas de codigo

Tema 4 variantes del if

IF simple
IF compuesto
if anidado
if, elif, else
"""

#Ejemplo if simple
color = "Rojo"
rojo = "azul"

if color == rojo:
    print("Soy rojo")

#Ejemplo if compuesto

if color == rojo:
    print("Soy rojo")
else:
    print("No soy rojo")

#Ejemplo if anidado puede funcionar cuando el primer if se logro, ahora te toca cumplir otra condicion 

if color == rojo:
    print("Soy rojo")
    if color != rojo: 
        print("Soy otro color")

#Ejemplo if con elif: si el if no se cumple, se va para ver si se cumple otra condicion

if color == rojo:
    print("Soy rojo")
elif color=="negro":
    print("Soy negro")
elif color=="Verde":
    print("Soy verde")
else:
    print("No tengo color")