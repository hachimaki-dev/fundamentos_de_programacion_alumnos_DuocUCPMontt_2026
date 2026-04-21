vengadores = []

while True:
    print("\n=========== BASE AVENGER ===========")
    print("1. Agregar Avenger")
    print("2. Mostrar Base y Modificar")
    print("3. Salir\n")

    eleccion = (input("¿Que opcion va a realizar?: ")).lower()

    if eleccion == "1":
        nombre_heroe = input("\n¿Como se llama el heroe que vas a agregar?: ").lower()
        vengadores.append(nombre_heroe)

    elif eleccion == "2":
        if len(vengadores) == 0:
            print("\n¡No hay ningún heroe en la base!")

        else:
            for i in range (len(vengadores)):
                print(f"Heroe {i} - {vengadores[i]}")
                vengadores[i] = vengadores[i].upper()

    elif eleccion == "3":
        print("\n¡Saliendo de la base Avenger!")
        break

    elif eleccion == "sacrificar":
        if vengadores:
            eliminado = vengadores.pop()
            print(f"\nHemos perdido a {eliminado}. Un sacrificio necesario en esta batalla.")
        else:
            print("\nNo quedan heroes para sacrificar")