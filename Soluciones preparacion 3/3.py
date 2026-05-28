
while True:
    try:
        edad_conductor = int(input("Ingrese su edad, porfavor."))
        if edad_conductor < 0:
            print("Porfavor una edad valida")
            continue
        else:
            print(f"Edad registrada : {edad_conductor}")
            break
    except ValueError:
        print("Dato inválido. Ingresa un entero positivo.")

