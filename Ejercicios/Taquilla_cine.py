numero_entradas = int(input("¿Cuantas entradas desea comprar? "))
contador_entradas = 1
precio_final = 0
while contador_entradas <= numero_entradas:
    edad_persona = int(input(f"¿Que edad tiene la persona N°{contador_entradas}? "))
    if edad_persona < 12:
        precio_final = precio_final + 3000
        contador_entradas = contador_entradas + 1
    elif edad_persona >= 65:
        precio_final = precio_final + 4000
        contador_entradas = contador_entradas + 1
    elif edad_persona >= 12:
        precio_final = precio_final + 6000
        contador_entradas = contador_entradas + 1
print(f"El precio de las entradas será de: ${precio_final}")