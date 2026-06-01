while True:
    try:
        edad_conductor = int(input("Ingrese su edad: "))

        if edad_conductor <= 0:
            print("¡Dato invalido, ingrese un numero entero positivo!")
        else:
            print(f"Edad registrada: {edad_conductor} años")
            break
    
    except ValueError:
        print("¡Dato invalido, ingrese un numero entero positivo!")
