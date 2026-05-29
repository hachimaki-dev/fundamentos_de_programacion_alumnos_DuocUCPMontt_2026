while True:
    try:
        edad = int(input("Ingrese su edad: "))
        if edad <= 0:
            print("Debe ser un número positivo")
        elif 1 <= edad <= 17:
            print("Debes tener mayor de edad para conducir")
        else:
            print(f"Edad registrada: {edad} años.")
            break
    except ValueError:
        print("Debe ser un número entero, no otra cosa")