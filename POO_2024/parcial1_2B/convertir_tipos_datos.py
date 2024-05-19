""""
comnetario de varias lineas
nota: cuando se imrime en pantalla una cadena de caracteres
se trabaja por default con "cadenas", es decir python no puede concatenar otra
cosa que no sea un string (string).

"""

texto = "Soy una cadena de caracteres"
numero = 23 

#concaternar str con str
print("Soy otra cadena y " + texto)

#concatenar str con int

print("El numero: " + str(numero))

#concatenar int con str
n1 = 23
n2 = 33

suma = n1 + n2

print(f"la suma es {suma}")

#concatenar float y int con str

n1 = 23.99
n2 = 33.0

suma = int(n1 + n2)

print(f"la suma es {suma}")





