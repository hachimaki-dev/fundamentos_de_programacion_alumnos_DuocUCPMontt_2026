while True:
    try:
        numero_de_pasajeros = int(input("ingrese el numero de pasajeros"))
        if numero_de_pasajeros < 0:
            print("ingrese un numero mayor que 0")
            continue
        else:
            print(f"vuelo registrado con {numero_de_pasajeros} pasajeros")
            break

    except ValueError:
      print("Error: ingresa un número entero positivo de pasajeros.")
       
    
    