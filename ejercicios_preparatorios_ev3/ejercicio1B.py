while True:
    try:
        registro_pasajeros = int(input("Ingrese el numero de pasajeros: "))
        pasajeros_abordo = registro_pasajeros
        if registro_pasajeros <= 0:
            print("Error: ingresa un número entero positivo de pasajeros.")
            continue
        else:
            print(f"Vuelo registrado con {pasajeros_abordo} pasajeros")
            break
    except ValueError:
        print("Error: ingresa un número entero positivo de pasajeros.")