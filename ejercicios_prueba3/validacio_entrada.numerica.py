while True:
    try:
        numero_recibido = int(input("Ingrese porfavor un numero entero: "))
        break
    except ValueError:
        print("ERROR debe ingresar un numero entero")
    else:
        print(f"numero corecto {numero_recibido}")