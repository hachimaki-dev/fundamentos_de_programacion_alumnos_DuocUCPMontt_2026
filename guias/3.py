while True :

    try:
        edad_conductor = int(input("Ingrese su edad: "))

        if edad_conductor < 1 :
            print("Tu edad ingresada debe ser mayor a 0 ")
        else:
            print(f"Edad registrada: {edad_conductor} años")
            break

    except ValueError :
        print("ERROR: ingrese un numero entero positivo")