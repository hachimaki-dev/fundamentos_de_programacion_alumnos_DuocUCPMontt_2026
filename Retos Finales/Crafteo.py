print("Entrando a la mesa de crafteo")
while True:
    print("Escoja su opción")
    print("1. Craftear espada de diamante")
    print("2. Craftear pico")
    print("3. salir del menu")
    opcion_elegida = int(input("Escoja una opcion (Del 1 al 3)"))
    if opcion_elegida == 1:
        print("Espada crafteada")
    elif opcion_elegida == 2:
        print("Pico crafteado")
    elif opcion_elegida == 3:
        print("Saliendo del menu de crafteo")
        break
    else:
        print("Receta desconocida")