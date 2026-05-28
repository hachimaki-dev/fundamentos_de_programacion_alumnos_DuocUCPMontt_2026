while True:
    try:
        edad_conductor = int(input("Ingrese edad: "))
        if edad_conductor <= 0:
            print("Edad debe ser mayor a 0")
            continue
        else:
            print(f"Edad registrada: {edad_conductor} años")
            break
    except:
        print("Error: debe ingresar un entero mayor a cero")
    