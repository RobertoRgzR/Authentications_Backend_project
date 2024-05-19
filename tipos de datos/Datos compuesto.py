#datos que adentro tienen otros datos simples u otros datos compuestos
#Al crear una lista se puede modificar los datos dentro
Lista = ["roberto rodriguez", 235, True, False]

#Creando una Tupla y esta no se puede modificar a la hora de hacer print
Tupla = ("roberto rodriguez", 235, True, False)

#esto es valido
Lista [3] = "Ctm"    

#esto no
#Tupla [3] =

conjunto = {"conjunto", True, False, 345, 345.5}

#Creando un diccionario
diccionario = {
    "nombre" : "roberto rodriguez",
    "escuela" : "UTD",
    "felicidad" : False,
    "altura" : 1.75
}

print (diccionario ["nombre"])