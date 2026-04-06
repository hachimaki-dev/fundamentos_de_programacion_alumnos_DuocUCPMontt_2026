precio_unitario = int(input("Ingrese el precio unitario del producto estrella: $"))
unidades_compradas = int(input("Ingrese las unidades compradas por el cliente: "))

if unidades_compradas >= 5:
    if unidades_compradas > 10:
        porcentaje_descuento = 20
    else:
        porcentaje_descuento = 10

    precio_sin_descuento = precio_unitario * unidades_compradas
    precio_final = precio_sin_descuento - (precio_sin_descuento / 100 * porcentaje_descuento)

    print(f"\n¡Felicidades! Obtuvo un {porcentaje_descuento}% de descuento.")
    print(f"Precio original: ${precio_sin_descuento}, ahorro: ${precio_sin_descuento - precio_final}")
    print(f"Precio final: ${precio_final}")

else:
    precio_final = (precio_unitario * unidades_compradas)
    print(f"No obtuvo ningun descuento.\nPrecio final: ${precio_final}")
