while True:
    try:
        print("\nMesa de Crafteo")
        print("---")
        print("-   1. Craftear Espada de Diamante\n-   1. Craftear Pico\n-   3. Salir de la mesa de Crafteo")
        print("---")
        espada = 1
        pico = 2 
        salir = 3
        eleccion = int(input("selecciona una opcion: "))
    except ValueError:
        print("ingresa una opcion valida")
        
        if eleccion == 1:
            print("¡Espada Crafteada!")
            continue
        elif eleccion == 2:
            print("¡Pico Listo!")
            continue
        elif eleccion == 3:
            print("Saliendo...")
            break
        if eleccion != 1 or 2 or 3:
            print("Receta desconocida. Intenta nuevamente")
