while True:
    try:
        pasajeros = int(input("Ingrese numeros de pasajero: "))
        if pasajeros <= 0:
            print("El numero debe ser mayor a cero")
            continue
    except ValueError:
        print("Error: ingresa un número entero positivo de pasajeros.")
    else:
        print(f"Vuelo registrado con {pasajeros} pasajeros.")
        break
    


