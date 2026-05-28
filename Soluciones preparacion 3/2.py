
while True:
    try:
        cantidad = int(input("Ingrese cantidad de unidades"))
        if cantidad < 0:
            print("Porfavor ingrese una cantidad valida")
            continue
        else:
            print(f"Stock registrado: {cantidad} unidades disponibles.")
            break
    except ValueError:
        print("Dato inválido. Ingresa un entero positivo para el stock.")