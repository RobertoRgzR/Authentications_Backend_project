Cadena1 = "roberto, Rodriguez,que,mas,pues"
Cadena2 =  "Bienvenido"
#la estructura de un meto es: EL DATO. EL METODO Y ()

#Dir- Devuelve la lista de comandos del objeto pasado


resultado1 = dir (Cadena1)

#UPPER- convierte todo a mayuscula, los metodos son seguidos de
resultado = Cadena1.upper()


#Lower- convierte a minusculuas
Bienvenida = "HOLA COMO ESTAN".lower()

#Capitalize-convierte la primera letra en mayuscula
primera_letra_en_mayuscula = Cadena1.capitalize()


#FIND- Buscar un valor que le pidamos, una cadena en una cadena
busqueda_find = Cadena1.find("o")

#INDEX
busqueda_index = Cadena1.index("z")
print (busqueda_index)

#ISNUMERIC-si es numerico devuelve true
es_numerico = Cadena1.isnumeric()

#ISALPHA-si es alfanumerico devolvemos true
es_alpha_numerico = Cadena1.isalpha()

#COUNT
contar_coincidencias = Cadena1.count("o")
print(contar_coincidencias)

#LEN es una funcion no un metodo
#contar_caracteres = Cadena1.len()

#ENDSWITH- verifica si una cadena comienza con
termina_con = Cadena2.endswith("t")
print(termina_con)

#STARSWITH- verifica si una cade termina con
empieza_con = Cadena1.startswith("s")
print(empieza_con)
#Replace-remplaza un valor por otro (remplaza el valor 1 por el valor 2)
cadena_nueva = Cadena1.replace("roberto Rodriguez", "Que onda puto")

#Split- separa por el parametro dado (crea una lista segun el valor que le demos)
cadena_separada = Cadena1.split(",")
print (cadena_separada)

