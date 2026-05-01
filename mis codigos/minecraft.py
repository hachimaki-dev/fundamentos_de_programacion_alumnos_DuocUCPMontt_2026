while True:
    opcion = int(input("Bienvenido! Elija una opcion: \n1. Craftear espada\n2. Craftear pico\n3. Salir"))
    if opcion == 1:
        print("Espada crafteada!")
    elif opcion == 2:
        print("Pico listo!")
    elif opcion == 3:
        print("Saliendo...")
        break
    else:
        print("Opción no válida. Por favor, elige una opción válida.")