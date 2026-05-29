while True:
    try:
        edad = int(input("Ingrese la edad: "))
        if edad <= 0:
            print("El numero debe ser mayor a cero")
            continue
    except ValueError:
        print("Dato inválido. Ingresa un entero positivo para el stock.")
    else:
        print(f"Edad registrada: {edad} años")
        break
