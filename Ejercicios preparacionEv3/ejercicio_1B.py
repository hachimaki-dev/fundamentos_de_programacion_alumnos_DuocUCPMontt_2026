while True:
    try:
        cantidad_pasajeros = int(input("Ingrese la cantidad de pasajeros en el vuelo: "))
        
        if cantidad_pasajeros > 0:
            print(f"Cantidad de pasajeros en vuelo son: {cantidad_pasajeros}.")
            break
        else:
            print("Ingrese un número mayor a 0")
            continue
    except:
        print("ERROR, Ingresa un numero entero positivo de pasajeros.")
