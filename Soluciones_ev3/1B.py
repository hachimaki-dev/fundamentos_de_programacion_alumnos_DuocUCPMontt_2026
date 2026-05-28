while True:
    try:
        pasajeros = int(input("Cuantos pasajeros abordaron el vuelo?: "))
        print(f"Vuelo registrado con {pasajeros} pasajeros.")
        break
    except ValueError:
        print("Error: ingresa un número entero positivo de pasajeros.")
