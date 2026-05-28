error = True
while error:
    try:
        cant_pasajeros = int(input("Ingrese la cantidad de pasajeros: "))
        error = False
    except ValueError:
        print("Error: ingresa un número entero positivo de pasajeros.")

    if not error:
        if cant_pasajeros <= 0:
            print("Error: ingresa un número entero positivo de pasajeros.")
            error = True
        else:
            print(f"Vuelo registrado con {cant_pasajeros} pasajeros.")