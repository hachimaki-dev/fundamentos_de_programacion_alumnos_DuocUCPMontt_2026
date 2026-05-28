while True:
    try:
        cantidad_pasajeros = int(input("Ingrese cantidad de pasajeros: "))
        if cantidad_pasajeros < 0:
            print("No puede ingresar un numero negativo")
            continue
        else:
            print(f"Vuelo registrado con {cantidad_pasajeros} pasajeros")
            break
    except:
        print("Error: ingresa un numero entero positivo de pasajeros")