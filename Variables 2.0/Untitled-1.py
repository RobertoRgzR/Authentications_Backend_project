def calcular_precio_final(precio):
    descuento = 0.20  # 20% de descuento
    monto_limite_descuento = 200

    if precio > monto_limite_descuento:
        precio_con_descuento = precio - (precio * descuento)
    else:
        precio_con_descuento = precio

    return precio_con_descuento

# Solicitar el precio al usuario
precio = float(input("Ingrese el precio del producto: "))

# Calcular y mostrar el precio final
precio_final = calcular_precio_final(precio)
print(f"El cliente debe pagar: ${precio_final:.2f}")
