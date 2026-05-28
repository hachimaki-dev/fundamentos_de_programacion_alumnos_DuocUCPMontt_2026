while True:
    try:
        usuario_ingresa_numero = int(input("Ingrese solo un numero :"))
    except ValueError:
        print("Error : no es un numero entero")
