while True:
    try:
        numero_pasajeros = int(input("ingresa el numero de pasajeros: "))
        if numero_pasajeros > 0:
            print(f"Vuelo registrado la cantidad de pasajeros es {numero_pasajeros}")
            break
        elif numero_pasajeros < 0:
            print("Error: ingresa un numero positivo de pasajeros")
    except:
        print("Error: ingresa un numero positivo de pasajeros")