while True:
    try:
        cantidad = int(input("cantidad de medicina"))
        if cantidad <= 0:
            print("ingrese un numero mayor a 0")
            continue
        else:
            print(f"Stock registrado: {cantidad} unidades disponibles.")
            break
    except ValueError:
        print("Dato inválido. Ingresa un entero positivo para el stock.")