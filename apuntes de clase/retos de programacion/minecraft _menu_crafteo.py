

espada = 1
pico = 2
salir = 3
opciones = [espada, pico, salir]

while True:
    try:
        print("\nMesa de Crafteo")
        print("---")
        print("-   1. Craftear Espada de Diamante\n-   2. Craftear Pico\n-   3. Salir de la mesa de Crafteo")
        print("---")
        eleccion = int(input("selecciona una opcion: "))
        if eleccion not in opciones:
            print("Receta desconocida. Intenta nuevamente")
            continue

        if eleccion == espada:
            print("¡Espada Crafteada!")
        elif eleccion == pico:
            print("¡Pico Listo!")
        elif eleccion == salir:
            print("Saliendo...")
            break
    except ValueError:
        print("ingrese una opcion valida")    
    