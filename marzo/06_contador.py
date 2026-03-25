bandera = True
contador = 0

while bandera:
    print("¡Hola!")
    contador = contador + 1
    print(f"Valor del contador: {contador}")
    if contador >= 10:
        print(f"El valor de la bandera antes de cambiar es: {bandera}")
        bandera = False
    else:
        continue

print(f"El valor de la bandera después de cambiar es: {bandera}")
