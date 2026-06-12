while True:
    
    try:
        pasajero = int(input("ingrese un numero de pasajero: "))
        if pasajero > 0:
            print(f"el vuelo lleva registrado {pasajero} pasajeros")
            break
        else:
            print("Error: ingrese un numero positivo de pasajero")
    except ValueError:
        print("debes de regristar un numero entero")

    