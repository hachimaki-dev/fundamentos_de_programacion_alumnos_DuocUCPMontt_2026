while True:
    try:
        pasajeros=int(input("Ingrese el número de pasajeros en el avión: "))
        if pasajeros>0:
            print(f"Vuelo registrado con {pasajeros} pasajeros.")
            break
        elif pasajeros<0:
            print("Error: ingresa un número entero positivo de pasajeros")
            continue
    except:
        print("Error: ingresa un número entero positivo de pasajeros.")