#contador de vocales
vocales = "aeiouAEIOU"
vocales_encontradas = []

def encontrar_vocales(palabra):
    for letra in palabra: 
        if letra in vocales:
            vocales_encontradas.append(letra)

        return vocales_encontradas

palabra_usuario = input("Ingrese la palabra de su gusto: ")
vocales_encontradas = encontrar_vocales(palabra_usuario)
print(vocales_encontradas)




