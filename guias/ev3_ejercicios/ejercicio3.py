print("Bienvenido al recuento del stock de una farmacia.")

medicamento = input("Ingresa el nombre del medicamento a revisar: ")

while True:
    try:
        stock_farmacia = int(input(f"Ingresa la cantidad de productos disponibles de {medicamento}: "))

        if stock_farmacia <= 0:
            print("Ingresa una cantidad mayor que 0.")
            continue
        else:
            print(f"Entendido, entonces hay {stock_farmacia} unidades de {medicamento}")
            break

    except ValueError:
        print("Ingresa un valor valido.")
        continue