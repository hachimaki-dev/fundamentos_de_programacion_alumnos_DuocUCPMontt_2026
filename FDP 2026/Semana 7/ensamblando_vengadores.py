vengadores = []

while True:
    print("1. Agregar avenger")
    print("2. Mostrar base y modificar")
    print("3. Salir")

    opcion = int(input("Escoge una opcion: "))

    if opcion == 1:
        heroe = input("Ingresa el nombre del heroe")

        vengadores.append(heroe)
    elif opcion == 2:
        for i in range(len(vengadores)):
            print(f"{i}. {vengadores[i]}")
    else:
        break
