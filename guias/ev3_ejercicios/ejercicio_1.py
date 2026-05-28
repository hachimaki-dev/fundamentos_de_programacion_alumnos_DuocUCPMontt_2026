

while True:
    try:
        numero = int(input("Ingresa un Número ENTERO: "))

        print(f"Número recibido es {numero}, muy bien!")
        break
    except ValueError:
        print("Ingresa un valor valido.")
        continue