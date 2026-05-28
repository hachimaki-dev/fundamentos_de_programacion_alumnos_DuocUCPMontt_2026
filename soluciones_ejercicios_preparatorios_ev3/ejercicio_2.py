while True:
    try:
        stock_de_farmacia = int(input("Ingrese el stock de la farmacia del doctor simi "))
        if stock_de_farmacia <= 0:

            continue
        else:
            print(f"Stock registrado: {stock_de_farmacia} unidades disponibles")
            break
    except ValueError:
        print("Coloque un numero mayor a 0 ")