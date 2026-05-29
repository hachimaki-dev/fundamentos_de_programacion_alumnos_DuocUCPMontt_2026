while True:
    try:
        edad_conductor = int(input("ingrese edad del conductor"))
        if edad_conductor < 0:
            print("ingrese un numero mayor a 0")
        else:
            print(f"Edad registrada: {edad_conductor}.")
            break
    except ValueError:
        print("ingresa un numero valido")