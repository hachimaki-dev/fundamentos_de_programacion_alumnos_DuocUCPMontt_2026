while True:
    try:
        registro_pasajeros = int(input("Ingrese el numero de pasajeros: "))
        
        if registro_pasajeros <= 0:
            print("Error: ingresa un número entero positivo de pasajeros.")

        else:
            print(f"Vuelo registrado con {registro_pasajeros} pasajeros")
            break
    except ValueError:
        print("Error: ingresa un número entero positivo de pasajeros.")