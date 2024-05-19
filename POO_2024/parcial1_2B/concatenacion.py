#Formas de concatenacion en python

nombre = "Roberto"
apellido = "Rodriguez"
Especialidad = "Area SW multiplataforma"
carrera = "Ing. en desarrollo y gestion de software"

#1er forma de concatenar
print("Mi nombre es: "+ nombre + " Estoy en la especialidad"+ Especialidad +" en la carrera de "+ carrera)

print("\n")

#2da forma

print("Mi nombre es: ", nombre , " Estoy en la especialidad", Especialidad ," en la carrera de ", carrera)

print("\n")

#3ra forma "FORMA COMUN EN PYTHON"
print(f"Mi nombre es:  {nombre}  Estoy en la {Especialidad}  en la carrera de {carrera}")

print("\n")

#4ta forma
print("Mi nombre es:  {} Estoy en la {}  en la carrera de {}") 
format(nombre, Especialidad,carrera)

print("\n")

#5ta forma 
print("Mi nombre es: "+ nombre + " Estoy en la especialidad"+ Especialidad +" en la carrera de "+ carrera)

print("\n")

