error = True
while error:
    try:
        edad = int(input("Ingrese la edad del conductor: "))
        error = False
    except ValueError:
        print("Dato inválido. Ingresa un entero positivo para el stock.")

    if not error:
        if edad > 0:
            print(f"Edad registrada: {edad} año(s).")
        else:
            print("Dato inválido. Ingresa un entero positivo para el stock.")
            error = True