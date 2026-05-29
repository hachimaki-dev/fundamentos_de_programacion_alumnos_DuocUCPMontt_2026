while True:
    try:
        medicamentos = int(input("Ingrese la cantidad de medicamentos: "))

        if medicamentos < 1:
            print("Dato inválido. Ingresa un entero positivo para el stock.")
            continue
        else:
            print(f"Stock registrado: {medicamentos} unidades disponibles.")
            break
    
    except ValueError:
        print("Ha ocurrido un error, esperaba un número entero")