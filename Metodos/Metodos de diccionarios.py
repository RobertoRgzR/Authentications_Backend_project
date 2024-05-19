Diccionario = {
    "NOMBRE" : "Roberto",
    "Apellido" : "Rodriguez",
    "Altura" : 1.75 
}
#nos devuelve u elemento dict_item
claves = Diccionario.keys()

#obteniendo un elemento un elemnto con get () (si no encuentra nada el programa continua)
valor_de = Diccionario.get("Roberto")


#eliminando todo el diccionario
#Diccionario.clear()

Diccionario.pop("NOMBRE") #si quiero sacar mas elemntos pongo coma

#obteniendo un elemnto dict_item iterable
diccionario_iterable= Diccionario.items()
print(diccionario_iterable)
type(diccionario_iterable)


