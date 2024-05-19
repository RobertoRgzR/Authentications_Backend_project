#Creando una funcion lambda para multipliar, no son aptas para hacer mas de una funcion
mutiplicar = lambda x : x*2
numeros = [1,2,3,4,5,6,7,8,9,10]
def numero_par(numeros):
    for numero in numeros:
        if (numero%2==0):
            return True
        
resultado = numero_par(numeros)
print(resultado)

#usando filter para un disque bucle for
numeros_pares = filter(lambda numero:numero%2==0, numeros)
print(list(numeros_pares))

