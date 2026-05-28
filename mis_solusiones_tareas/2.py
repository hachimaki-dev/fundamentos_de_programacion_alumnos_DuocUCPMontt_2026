while True:
    try:
        cantidad_de_medicamentos = int(input("Ingrese el stock de medicamentos: "))

        if cantidad_de_medicamentos > 0:
            print(f"Stock registrado: {cantidad_de_medicamentos} unidades disponibles")
        else:
            print("No se puede tener este stock deve ser un numero positivo, por favor intenta de nuevo.")

    except:
        print("Error: el stock debe ser un número.")