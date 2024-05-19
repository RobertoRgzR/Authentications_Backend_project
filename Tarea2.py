def rellenar_array(tamaño, numero):
    array = [[0]* tamaño for _ in range(tamaño)]
    valor = numero
    for i in range(tamaño):
        for j in range(tamaño):
            array[i][j] = valor
            valor += numero
    return array

def mostrar_array(array):
    for fila in array: 
        for elemento in fila: 
            print(elemento, end=" ")
        print()

try:
    tamaño = int(input("Ingrese un numero para el tamaño de la matriz: "))
    numero = int(input("Ingrese el numero con el que desea rellenar: "))

    if tamaño <= 0: 
        print("Ingrese un numero mayor a 0")
    else: 
        array_resultante = rellenar_array(tamaño, numero)
        print("Matriz resultante: ")
        mostrar_array(array_resultante)
except ValueError:
    print("Ingrese un numero valido")