#Creando una tupla
datos = ("Roberto", "Hermoso", 556)
en_lista = ["Roberto", "Hermoso", 556]

#Desempaquetando los datos
nombre, estado, seguidores = datos

#Mostrando los datos
print (nombre)

#Desempaquetando con FOR
for dato in enumerate(datos): 
    indice = dato[0]
    valor = dato[1]
    print(f"El indice es: {indice}")
    print(f"El valor es: {valor}")
