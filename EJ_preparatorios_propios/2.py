
while True:
    try:
        medicamentos_disponibles = int(input("Ingrese la cantidad de unidades disponibles de un medicamento:  "))
        if medicamentos_disponibles <= 0:
            print("Dato Invalido : Ingrese un numero entero positivo  para el Stock")
            continue
        else:
            print(f"Stock Registrado : {medicamentos_disponibles} unidades disponibles ")
            break
    except ValueError:
        print("Dato Invalido : Ingrese un numero entero positivo  para el Stock")


