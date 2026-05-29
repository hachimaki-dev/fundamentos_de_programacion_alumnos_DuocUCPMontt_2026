while True: 
    try:
        pasajeros = int(input("ingrese cuanto pasajeros hay"))
        if pasajeros <= 0:
            print("ingrese un numero mayor a cero")
            continue 
        else:
            print(f"Vuelo registrado con {pasajeros} pasajeros.")
            break
    except ValueError:
        print("Error: ingresa un número entero positivo de pasajeros")