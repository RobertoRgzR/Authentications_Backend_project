
with open('hola.txt', 'w') as archivo:
    archivo.write("hola")

with open('hola.txt', 'r') as archivo:
    lineas = archivo.read()
    print(lineas)
