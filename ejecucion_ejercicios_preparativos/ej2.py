while True:
    try:
        medicamentos_disponibles = int(input("¿Cuántos medicamentos tiene disponible en la farmacia? "))
        if medicamentos_disponibles > 0:
            print(f"Stock Registrado: {medicamentos_disponibles} unidades disponibles.")
            break
        else:
            print("Ingresar una cantidad de 0 o menor, no es válido, porfavor vuelva a intentarlo")
    except ValueError:
        print("Dato inválido. Ingresa un entero positivo para el stock.")
