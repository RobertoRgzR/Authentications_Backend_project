
lista = list(["hola",1.75,"soy guapo",45,67,8,])


#Cuenta la cantidad de elementos en una lista
len(lista)


#agregando un elemnto a la lista
lista.append("Victor adir")

#agregando un elemnto a la lista en un indice especifico
lista.insert(2,45)

#agregando varios elementos a la lista (tenemos que poner una lista y la mete a la lista)
lista.extend([True,2344])

#eliminando un elemento de la lista por su indice
lista.pop(3) #-1 para eliminar el ultimo, -2 para eliminar el antepenultimo y asi sucesivamente

#removiendo un elemnto de la lista por su valor
lista.remove("hola")

#eliminando todos los elementos de la lista
#lista.clear()

#ordenando la lista (si usamos el parametro reverse los voltea, solo funciona con cosas que no sea un string)
lista.sort()
print(lista)
#Voltea simplemente la lista al reves
lista.reverse()


#Verificando si une elemento se encuentra en la lista 
elemento_encontrado = lista.index(45)