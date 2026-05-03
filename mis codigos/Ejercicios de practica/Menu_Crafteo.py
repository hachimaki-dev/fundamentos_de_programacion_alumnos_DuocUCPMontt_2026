print("Menú de crafteo.")

while True:
    print("1. Craftear Espada de Diamante \n2. Craftear Pico \n3. Salir de la Mesa de Crafteo")
    opcion_elegida = int(input(f"Elija una opción "))

    if opcion_elegida == 1:
        print("¡Espada Crafteada!")
    elif opcion_elegida == 2:
        print("¡Pico listo!")
    elif opcion_elegida == 3:
        break
    else:
        print("Receta desconocida")