while True:
    try:
        pasajeros = int(input("Ingrese el número de pasajeros"))
        
        if pasajeros < 0:
            print("Porfavor ingrese una cantidad valida")
            continue
        else:
            break

    except:
        print("Error: ingresa un número entero positivo de pasajeros.")

