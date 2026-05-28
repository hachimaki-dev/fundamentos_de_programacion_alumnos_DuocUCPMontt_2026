while True:
    try:
        edad_camionero=int(input("Ingrese la edad del camionero: "))
        if edad_camionero>0:
            print(f"Edad registrada: {edad_camionero} años")
            break
        elif edad_camionero<0:
            print("Dato inválido. Ingresa una edad valida")
            continue
    except:
        print("Dato inválido. Ingresa una edad valida")