while True:
    try:
        pasajeros = int(input("Ingresa la cantidad de pasajeros: "))

        if pasajeros < 1:
            print("Error: ingresa un número entero positivo de pasajeros.")
            continue
        else:
            print(f"Vuelo registrado con {pasajeros} pasajeros.")
            break

    except ValueError:
        print("Ha ocurrido un error, se esperaba un número entero")
