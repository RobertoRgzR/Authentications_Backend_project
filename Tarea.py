#Tarea 
def saludar(nombre, sexo):
    sexo = sexo.lower()
    if (sexo == "mujer"):
        adjetivo = "reina"
    elif (sexo == "hombre"):
        adjetivo = "master"
    else: 
        adjetivo = "culo"
    print(f"Hola {nombre}, mi {adjetivo} ¿como estas?")

saludar("manuel", "hombre")

def contraseñaRandom(num):
    chars = "abcdefghij"
    num_entero = str(num)
    num = int(num_entero[0])
    c1 = num - 2
    c2 = num 
    c3 = num - 5
    contraseña = f"{chars[c1]}{chars[c2]}{chars[c3]}{num * 2}"
    return contraseña

password = contraseñaRandom(4)
frase = f"Tu contraseña sera: {password}"
print(frase)