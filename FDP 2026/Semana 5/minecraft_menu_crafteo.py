while True:
    print("1. Craftear Espada de Diamante\n2. Craftear Pico\n3. Salir de la Mesa de Crafteo")

    opcion = int(input("Ingresa una opción: "))

    if opcion == 1:
        print("Espada crafteada")
    elif opcion == 2:
        print("Pico listo")
    elif opcion == 3:
        break
    else:
        print("Receta desconocida")