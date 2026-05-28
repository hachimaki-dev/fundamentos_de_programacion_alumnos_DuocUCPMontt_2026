while True:
    try:
        edad = int(input("Ingrese su edad: "))

        if edad > 0:
            print(f"Edad registrada: {edad} años.")
            break
        else:
            print("Error, la edad debe ser un numero entero positivo")
    except ValueError:
        print("Error, la edad debe ser un numero entero positivo")

        