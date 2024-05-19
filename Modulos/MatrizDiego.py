import numpy as np

# Definir matrices 5x5 que simulan la forma de las letras del alfabeto
matrices_letras = {
    'A': np.array([[0, 1, 0, 1, 0], [1, 0, 0, 0, 1], [1, 1, 1, 1, 1], [1, 0, 0, 0, 1], [1, 0, 0, 0, 1]]),
    'B': np.array([[1, 1, 1, 1, 0], [1, 0, 0, 0, 1], [1, 1, 1, 1, 0], [1, 0, 0, 0, 1], [1, 1, 1, 1, 0]]),
    'C': np.array([[0, 1, 1, 1, 1], [1, 0, 0, 0, 0], [1, 0, 0, 0, 0], [1, 0, 0, 0, 0], [0, 1, 1, 1, 1]]),
    'D': np.array([[1, 1, 1, 1, 0], [1, 0, 0, 0, 1], [1, 0, 0, 0, 1], [1, 0, 0, 0, 1], [1, 1, 1, 1, 0]]),
    'E': np.array([[1, 1, 1, 1, 1], [1, 0, 0, 0, 0], [1, 1, 1, 1, 0], [1, 0, 0, 0, 0], [1, 1, 1, 1, 1]]),
    'F': np.array([[1, 1, 1, 1, 1], [1, 0, 0, 0, 0], [1, 1, 1, 1, 0], [1, 0, 0, 0, 0], [1, 0, 0, 0, 0]]),
    'G': np.array([[0, 1, 1, 1, 1], [1, 0, 0, 0, 0], [1, 0, 0, 1, 1], [1, 0, 0, 0, 1], [0, 1, 1, 1, 1]]),
    'H': np.array([[1, 0, 0, 0, 1], [1, 0, 0, 0, 1], [1, 1, 1, 1, 1], [1, 0, 0, 0, 1], [1, 0, 0, 0, 1]]),
    'I': np.array([[1, 1, 1, 1, 1], [0, 0, 1, 0, 0], [0, 0, 1, 0, 0], [0, 0, 1, 0, 0], [1, 1, 1, 1, 1]]),
    'J': np.array([[1, 1, 1, 1, 1], [0, 0, 0, 0, 1], [0, 0, 0, 0, 1], [1, 0, 0, 0, 1], [0, 1, 1, 1, 0]]),
    'K': np.array([[1, 0, 0, 0, 1], [1, 0, 1, 0, 0], [1, 1, 1, 0, 0], [1, 0, 1, 0, 0], [1, 0, 0, 0, 1]]),
    'L': np.array([[1, 0, 0, 0, 0], [1, 0, 0, 0, 0], [1, 0, 0, 0, 0], [1, 0, 0, 0, 0], [1, 1, 1, 1, 1]]),
    'M': np.array([[1, 0, 0, 0, 1], [1, 1, 1, 1, 1], [1, 0, 1, 0, 1], [1, 0, 0, 0, 1], [1, 0, 0, 0, 1]]),
    'N': np.array([[1, 0, 0, 0, 1], [1, 1, 0, 0, 1], [1, 1, 1, 0, 1], [1, 0, 1, 0, 1], [1, 0, 0, 0, 1]]),
    'O': np.array([[1, 1, 1, 1, 1], [1, 0, 0, 0, 1], [1, 0, 0, 0, 1], [1, 0, 0, 0, 1], [1, 1, 1, 1, 1]]),
    'P': np.array([[1, 1, 1, 1, 1], [1, 0, 0, 0, 1], [1, 1, 1, 1, 1], [1, 0, 0, 0, 0], [1, 0, 0, 0, 0]]),
    'Q': np.array([[1, 1, 1, 1, 1], [1, 0, 0, 0, 1], [1, 0, 1, 0, 1], [1, 0, 1, 0, 1], [0, 1, 1, 1, 1]]),
    'R': np.array([[1, 1, 1, 1, 1], [1, 0, 0, 0, 1], [1, 1, 1, 1, 0], [1, 0, 1, 0, 0], [1, 0, 0, 0, 1]]),
    'S': np.array([[1, 1, 1, 1, 1], [1, 0, 0, 0, 0], [1, 1, 1, 1, 1], [0, 0, 0, 0, 1], [1, 1, 1, 1, 1]]),
    'T': np.array([[1, 1, 1, 1, 1], [0, 0, 1, 0, 0], [0, 0, 1, 0, 0], [0, 0, 1, 0, 0], [0, 0, 1, 0, 0]]),
    'U': np.array([[1, 0, 0, 0, 1], [1, 0, 0, 0, 1], [1, 0, 0, 0, 1], [1, 0, 0, 0, 1], [1, 1, 1, 1, 1]]),
    'V': np.array([[1, 0, 0, 0, 1], [1, 0, 0, 0, 1], [0, 0, 0, 0, 1], [0, 0, 1, 0, 0], [0, 1, 0, 0, 0]]),
    'W': np.array([[1, 0, 0, 0, 1], [1, 0, 0, 0, 1], [1, 1, 1, 1, 1], [1, 0, 0, 0, 1], [1, 0, 0, 0, 1]]),
    'X': np.array([[1, 0, 1, 0, 1], [0, 0, 1, 0, 0], [0, 1, 1, 1, 0], [0, 0, 1, 0, 0], [1, 0, 1, 0, 1]]),
    'Y': np.array([[1, 0, 0, 0, 1], [1, 0, 1, 0, 0], [0, 0, 1, 0, 0], [0, 0, 1, 0, 0], [0, 0, 1, 0, 0]]),
    'Z': np.array([[1, 1, 1, 1, 1], [0, 0, 0, 0, 1], [0, 1, 1, 1, 0], [1, 0, 0, 0, 0], [1, 1, 1, 1, 1]]),
}

# Crear matrices para letras minúsculas
matrices_letras.update({
    'a': matrices_letras['A'],
    'b': matrices_letras['B'],
    'c': matrices_letras['C'],
    'd': matrices_letras['D'],
    'e': matrices_letras['E'],
    'f': matrices_letras['F'],
    'g': matrices_letras['G'],
    'h': matrices_letras['H'],
    'i': matrices_letras['I'],
    'j': matrices_letras['J'],
    'k': matrices_letras['K'],
    'l': matrices_letras['L'],
    'm': matrices_letras['M'],
    'n': matrices_letras['N'],
    'o': matrices_letras['O'],
    'p': matrices_letras['P'],
    'q': matrices_letras['Q'],
    'r': matrices_letras['R'],
    's': matrices_letras['S'],
    't': matrices_letras['T'],
    'u': matrices_letras['U'],
    'v': matrices_letras['V'],
    'w': matrices_letras['W'],
    'x': matrices_letras['X'],
    'y': matrices_letras['Y'],
    'z': matrices_letras['Z'],
})

# Función para sumar matrices y mantener resultados entre 0 y 1
def suma_matrices(matriz1, matriz2):
    if matriz1.shape == matriz2.shape:
        return (matriz1 + matriz2)  
    else:
        raise ValueError("Las matrices deben tener la misma dimensión para sumarse.")

# Función para calcular el determinante
def matriz_determinante(matriz):
    return np.linalg.det(matriz)

# Pedir un nombre al usuario
nombre = input("Introduce un nombre: ")
apellido = input("Introduce el apellido: ")

# Inicializar matriz total con ceros para acumular la suma
matriz_total = np.zeros((5, 5))

# Imprimir y sumar cada matriz asociada a las letras del nombre
for letra in nombre:
    matriz = matrices_letras[letra]
    print(f"Matriz para la letra '{letra}':")
    print(matriz)
    
    matriz_total = suma_matrices(matriz_total, matriz)  # Sumar a la matriz total

for letra in apellido:
    matriz1 = matrices_letras[letra]
    print(f"La matriz para letra {letra}")
    print(matriz1)
    
# Imprimir la matriz total después de sumar todas las matrices
print("Matriz resultante de la suma de todas las letras del nombre:")
print(matriz_total)


# Calcular y mostrar el determinante de la matriz total
determinante = matriz_determinante(matriz_total)

print("El determinante de la matriz total es:", determinante)

