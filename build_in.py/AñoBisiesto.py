nombres = []
kilometros = []
grupos = []
for i in range(5):
    nombre_individual = input(f"Ingrese el nombre del conductor {i+1}")
    nombres.append(nombre_individual)
    for j in range(5):
        kilometros_diarios = int(input(f"Ingrese los km para el dia {j+1} y para {nombre_individual}"))
        kilometros.append(kilometros_diarios)

    
for kilometro in kilometros:
     print(f"Estos fueron los kiloemtros {kilometro}")
