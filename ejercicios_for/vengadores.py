print("==== BUEN DIA SEÑOR FURY ====")

vengadores = []

while True:
    print("1. Agregar Vengador")
    print("2. Mostrar Base y Modificar")
    print("3. Salir")

    opcion_nick_fury = input("ingrese opcion(1/2/3): ").lower()

    if opcion_nick_fury == "1":

        ingreso_vengador = input("como se llama el vengador que desea añadir?: ")

        vengadores.append(ingreso_vengador)

        print("vengador añadido")

    elif opcion_nick_fury == "2":

        if len(vengadores) == 0:
            print("NO TIENE VENGADORES REGISTRADOS SEÑOR FURY")

        for i in range (len(vengadores)):

            print("=" * 30)

            print(f"{i} - {vengadores[i]}")

            vengadores[i] = vengadores[i].upper()

            print("=" * 30)

    elif opcion_nick_fury == "3":

        print("Hasta luego señor Fury, buena suerte")
        break

    elif opcion_nick_fury == "sacrificar":

        if len(vengadores) == 0:
            print("No hay nadie a quien sacrificar.")
        else:
            for i in range(len(vengadores)):
                print(f"{i} - {vengadores[i]}")
            
            posicion = int(input("¿A quién desea eliminar?:  "))
            
            if posicion < len(vengadores):
                eliminado = vengadores.pop(posicion)
                print(f"Vengador {eliminado} eliminado")

    else:
        print("opcion invalida intente nuevamente")
        continue