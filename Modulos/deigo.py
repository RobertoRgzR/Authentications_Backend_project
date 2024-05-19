import numpy as np

# Función para crear matrices de letras con un tamaño específico
def crear_matriz_letra(filas, columnas, forma):
    matriz = np.zeros((filas, columnas), dtype=int)
    for i in range(filas):
        for j in range(columnas):
            if forma[i][j] == '1':
                matriz[i][j] = 1
    return matriz

# Matrices que representan visualmente las letras mayúsculas del abecedario
letras_mayusculas = {
    'A': [
        '001100',
        '010010',
        '111111',
        '100001',
        '100001',
        '100001'
    ],
    'B': [
        '111100',
        '100010',
        '111100',
        '100010',
        '111100',
        '000000'
    ],
    'C': [
        '011110',
        '100000',
        '100000',
        '100000',
        '011110',
        '000000'
    ],
    'D': [
        '111100',
        '100010',
        '100001',
        '100001',
        '111100',
        '000000'
    ],
    'E': [
        '111111',
        '100000',
        '111110',
        '100000',
        '111111',
        '000000'
    ],
    'F': [
        '111111',
        '100000',
        '111110',
        '100000',
        '100000',
        '000000'
    ],
    'G': [
        '011110',
        '100000',
        '100111',
        '100001',
        '011110',
        '000000'
    ],
    'H': [
        '100001',
        '100001',
        '111111',
        '100001',
        '100001',
        '000000'
    ],
    'I': [
        '111111',
        '001000',
        '001000',
        '001000',
        '111111',
        '000000'
    ],
    'J': [
        '000111',
        '000001',
        '000001',
        '100001',
        '011110',
        '000000'
    ],
    'K': [
        '100001',
        '100010',
        '111100',
        '100010',
        '100001',
        '000000'
    ],
    'L': [
        '100000',
        '100000',
        '100000',
        '100000',
        '111111',
        '000000'
    ],
    'M': [
        '100001',
        '110011',
        '101101',
        '100001',
        '100001',
        '000000'
    ],
    'N': [
        '100001',
        '110001',
        '101001',
        '100101',
        '100011',
        '000000'
    ],
    'O': [
        '011110',
        '100001',
        '100001',
        '100001',
        '011110',
        '000000'
    ],
    'P': [
        '111100',
        '100010',
        '111100',
        '100000',
        '100000',
        '000000'
    ],
    'Q': [
        '011110',
        '100001',
        '100001',
        '100101',
        '011111',
        '000001'
    ],
    'R': [
        '111100',
        '100010',
        '111100',
        '100010',
        '100001',
        '000000'
    ],
    'S': [
        '011110',
        '100000',
        '011100',
        '000010',
        '111100',
        '000000'
    ],
    'T': [
        '111111',
        '001000',
        '001000',
        '001000',
        '001000',
        '000000'
    ],
    'U': [
        '100001',
        '100001',
        '100001',
        '100001',
        '011110',
        '000000'
    ],
    'V': [
        '100001',
        '100001',
        '010010',
        '010010',
        '001100',
        '000000'
    ],
    'W': [
        '100001',
        '101101',
        '101101',
        '101101',
        '010010',
        '000000'
    ],
    'X': [
        '100001',
        '010010',
        '001100',
        '010010',
        '100001',
        '000000'
    ],
    'Y': [
        '100001',
        '010010',
        '001100',
        '001000',
        '001000',
        '000000'
    ],
    'Z': [
        '111111',
        '000010',
        '000100',
        '001000',
        '111111',
        '000000'
    ]
}

# Matrices que representan visualmente las letras minúsculas del abecedario
letras_minusculas = {
    'a': [
        '000000',
        '000000',
        '011110',
        '100010',
        '011110',
        '000000'
    ],
    'b': [
        '100000',
        '100000',
        '111110',
        '100010',
        '111110',
        '000000'
    ],
    'c': [
        '000000',
        '000000',
        '011110',
        '100000',
        '011110',
        '000000'
    ],
    'd': [
        '000010',
        '000010',
        '011110',
        '100010',
        '011110',
        '000000'
    ],
    'e': [
        '000000',
        '000000',
        '011110',
        '111110',
        '011110',
        '000000'
    ],
    'f': [
        '001000',
        '011100',
        '001000',
        '001000',
        '001000',
        '000000'
    ],
    'g': [
        '000000',
        '011110',
        '100010',
        '011110',
        '000010',
        '011100'
    ],
    'h': [
        '100000',
        '100000',
        '111110',
        '100010',
        '100010',
        '000000'
    ],
    'i': [
        '001000',
        '000000',
        '011000',
        '001000',
        '011110',
        '000000'
    ],
    'j': [
        '000100',
        '000000',
        '000100',
        '100100',
        '011000',
        '000000'
    ],
    'k': [
        '100000',
        '100010',
        '111100',
        '100010',
        '100000',
        '000000'
    ],
    'l': [
        '011000',
        '001000',
        '001000',
        '001000',
        '011110',
        '000000'
    ],
    'm': [
        '000000',
        '000000',
        '110110',
        '101010',
        '100010',
        '000000'
    ],
    'n': [
        '000000',
        '000000',
        '111110',
        '100010',
        '100010',
        '000000'
    ],
    'o': [
        '000000',
        '000000',
        '011110',
        '100010',
        '011110',
        '000000'
    ],
    'p': [
        '000000',
        '111110',
        '100010',
        '111110',
        '100000',
        '000000'
    ],
    'q': [
        '000000',
        '011110',
        '100010',
        '011110',
        '000010',
        '000111'
    ],
    'r': [
        '000000',
        '000000',
        '111110',
        '100010',
        '100000',
        '000000'
    ],
    's': [
        '000000',
        '011110',
        '100000',
        '011110',
        '000010',
        '011100'
    ],
    't': [
        '001000',
        '011100',
        '001000',
        '001000',
        '000000',
        '000000'
    ],
    'u': [
        '000000',
        '000000',
        '100010',
        '100010',
        '011110',
        '000000'
    ],
    'v': [
        '000000',
        '000000',
        '100010',
        '100010',
        '011100',
        '000000'
    ],
    'w': [
        '000000',
        '000000',
        '100010',
        '101010',
        '011100',
        '000000'
    ],
    'x': [
        '000000',
        '000000',
        '100010',
        '011100',
        '100010',
        '000000'
    ],
    'y': [
        '000000',
        '000000',
        '100010',
        '011100',
        '000100',
        '011000'
    ],
    'z': [
        '000000',
        '000000',
        '111110',
        '000100',
        '111110',
        '000000'
    ]
}

# Función para sumar dos matrices del mismo tamaño
def sumar_matrices(matriz1, matriz2):
    if matriz1.shape == matriz2.shape:
        return matriz1 + matriz2
    raise ValueError("Las matrices deben ser del mismo tamaño para sumar.")

# Función para calcular la inversa, transpuesta y determinante de una matriz
def operaciones_matriz(matriz):
    try:
        matriz_inversa = np.linalg.inv(matriz)
        matriz_transpuesta = matriz.T
        determinante = np.linalg.det(matriz)
        return matriz_inversa, matriz_transpuesta, determinante
    except np.linalg.LinAlgError:
        return None, None, None

# Crear matrices para cada letra del abecedario
matrices_abecedario = {}
for letra in letras_mayusculas.keys():
    matriz_mayuscula = crear_matriz_letra(6, 6, letras_mayusculas[letra])
    matrices_abecedario[letra.upper()] = matriz_mayuscula

for letra in letras_minusculas.keys():
    matriz_minuscula = crear_matriz_letra(6, 6, letras_minusculas[letra])
    matrices_abecedario[letra.lower()] = matriz_minuscula

# Agregar matriz de identidad
matriz_identidad = np.eye(6, dtype=int)
matrices_abecedario['identidad'] = matriz_identidad

# Solicitar nombre al usuario
nombre = input("Introduce tu nombre: ")

# Obtener y mostrar las matrices para cada letra del nombre
matrices_nombre = []
for char in nombre:
    if char in matrices_abecedario:
        matriz = matrices_abecedario[char]
        matrices_nombre.append(matriz)
        print(f"Matriz para '{char}':\n{matriz}\n")

# Sumar todas las matrices del nombre
matriz_suma = np.zeros((6, 6), dtype=int)
for matriz in matrices_nombre:
    matriz_suma = sumar_matrices(matriz_suma, matriz)

print(f"Matriz resultante de la suma de las letras de tu nombre:\n{matriz_suma}\n")

# Calcular la inversa, transpuesta y determinante de la matriz resultante
matriz_inversa, matriz_transpuesta, determinante = operaciones_matriz(matriz_suma)

if matriz_inversa is not None:
    print(f"Matriz inversa de la suma de las letras de tu nombre:\n{matriz_inversa}\n")
    print(f"Matriz transpuesta de la suma de las letras de tu nombre:\n{matriz_transpuesta}\n")
    print(f"Determinante de la suma de las letras de tu nombre: {determinante}")
else:
    print("La matriz resultante es singular y no se puede calcular la inversa.")
