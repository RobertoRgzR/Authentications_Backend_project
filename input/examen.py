
archivo = "input//examen.py"
archivo_nuevo = "input//examen1.py"


with open(archivo, "r") as archivo:
    input_lista = [line.strip() for line in archivo]

lista_sin_duplicados = list(set(input_lista))

with open(archivo_nuevo, "w") as archivo:
    for elem in lista_sin_duplicados:
        archivo.write(f"{elem}\n")

print(f"Unique list has been written to '{archivo_nuevo}'")
