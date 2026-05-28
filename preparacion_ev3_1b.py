while True:
    try:
        pasajeros = int(input("Ingrese el número de pasajeros: "))
        if pasajeros == 1:
            print(f"Vuelo registrado con {pasajeros} pasajero.")
            break
        elif pasajeros >= 2:
            print(f"Vuelo registrado con {pasajeros} pasajeros.")
            break
        else:
            print("Debe ser un número entero positivo")
    except ValueError:
        print("Error: ingresa un número entero positivo de pasajeros.")