bandera = True

while bandera == True:
    print("¿Qué tipo de chiste quieres?")
    print("1. Chiste nanai")
    print("2. Chiste no nanai")
    print("3. Salir del programa")

    eleccion_chiste = int(input("Elige una opción: "))

    if eleccion_chiste == 1:
        print("Elige un chiste nanai")
        print("1. Chiste 1")
        print("2. Chiste 2")
        print("3. Chiste 3")

        eleccion_chiste_nanai = int(input("Elige: "))

        if eleccion_chiste_nanai == 1:
            print("Aquí irá el chiste nanai 1")
        elif eleccion_chiste_nanai == 2:
            print("Aquí irá el chiste nanai 2")
        elif eleccion_chiste_nanai == 3:
            print("Aquí irá el chiste nanai 3")
        else:
            print("Elección inválida")

    elif eleccion_chiste == 2:
        print("Elige un chiste no nanai")
        print("1. Chiste 1")
        print("2. Chiste 2")
        print("3. Chiste 3")

        eleccion_chiste_no_nanai = int(input("Elige: "))

        if eleccion_chiste_nanai == 1:
            print("Aquí irá el chiste nanai 1")
        elif eleccion_chiste_nanai == 2:
            print("Aquí irá el chiste nanai 2")
        elif eleccion_chiste_nanai == 3:
            print("Aquí irá el chiste nanai 3")
        else:
            print("Elección inválida")

    elif eleccion_chiste == 3:
        print("Saliendo del programa")
        bandera = False
    else:
        print("Elección inválida")