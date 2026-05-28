while True:
    try:
        edad_conductor = int(input("Ingrese su edad: "))
        if edad_conductor <= 0:
            continue
        else:
            print(f"Edad registrada: {edad_conductor} años")
            break
    except ValueError:
        print("Ingrese una edad válida por favor")