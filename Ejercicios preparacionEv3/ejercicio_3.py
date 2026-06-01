while True:
    try:
        edad_conductor = int(input("Ingrese su edad: "))

        if edad_conductor > 0 and edad_conductor < 18:
            print("No puedes conducir aún")
            break
        elif edad_conductor > 0:
            print(f"Edad registrada: {edad_conductor} años")
            break
        else:
            print("Ingresa una edad valida!")
    except ValueError:
        print("Dato invalido, ingresa algo valido.")