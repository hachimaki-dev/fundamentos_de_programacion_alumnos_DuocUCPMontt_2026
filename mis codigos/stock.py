while True:
    try:
        stock = int(input("cuando es el stock que hay? "))
        if stock >0:
            print(f"el stock que hay es de {stock} de medicamentos")
            break
        elif stock < 0:
            print("no se aceptan numeros negativos")
            continue
    except:
        print("no se acpetan fracciones ni letras")
