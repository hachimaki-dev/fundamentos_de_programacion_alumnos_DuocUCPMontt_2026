print("Bienvenido al registro de pasajeros!")

while True:
    try:
        pasajeros = int(input("Ingresa el número de pasajeros que abordaron este vuelo: "))

        if pasajeros > 0:
            print(f"Muy bien!, entonces se realizo el vuelo con {pasajeros} pasajeros.")
            break
        else:
            print("Ingresa un número mayor a 0")

    except ValueError:
        print("Ingresa un valor valido.")