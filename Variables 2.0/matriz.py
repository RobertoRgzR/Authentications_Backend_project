# Crear la matriz de 5x5 con todos los valores en 0
matriz = [[0 for i in range(5)] for j in range(5)]

# Recorrer la diagonal principal y asignar el valor 1
for i in range(5):
    matriz[i][i] = 1

# Mostrar el contenido de la tabla en pantalla
for fila in matriz:
    print(fila)
