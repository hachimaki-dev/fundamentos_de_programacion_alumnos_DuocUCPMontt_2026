while True:
    try:
        edad = int(input("ingrese su edad"))
        if edad <= 0:
            print("ingrese edad valida")
            continue
        else:
            print(f"Edad registrada: {edad} años")
            break
    except ValueError:
        print("ingrese un numero valido")