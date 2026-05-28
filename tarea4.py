while True:
    try:
        edad = (int(input("Ingrese su edad: ")))
        if edad <= 0:
            print("Dato invalido, ingrese un numero entero positivo")
            continue
    except ValueError:
        print("Ingrese un numero entero.")
    else:
        print(f"Edad registrada {edad}")

