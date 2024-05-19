#Forma no optima de sumar valores
#def suma(lista):
    #numeros_sumados = 0
    #for numero in lista:
     #   numeros_sumados = numeros_sumados + numero
    #return numeros_sumados

#sumaDeLosNumeros = suma([1,56,67,85,34,56,34,56,34])
#print(suma)

#utilizano el paramtro args como 
def suma(nombre, *numeros): #el * transforma lo que venga en uno solo, o sea si son varios numeros los comvierte a lista.
    return f"{nombre} la suma de tus numeros es {sum(numeros)}"
#Si llegas a poner algo despues de args se va a meter a args convirtiendolo en uno solo
#Asi que si quieres mas elementos usando args vas a ponerlos antes

resultado = suma("daniel", 1,56,67,85,34,56,34,56,34)
print(resultado)