print("############## MESA DE CRAFTEO ##############")

print("1. Craftear Espada de Diamante")
print("2. Craftear Pico")
print("3. Salir de la mesa de crafteo")

bandera = True

while bandera:

    opcion_elegida = int(input("Seleccione su opcion:"))

    if opcion_elegida == 1:
        print("¡Espada crafteada!")

    elif opcion_elegida == 2:
        print("¡Pico listo!")

    elif opcion_elegida == 3:
        break

    else:
        print("Receta desconocida. Intenta nuevamente.")