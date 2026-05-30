while True:
    numero1 = 100
    numero2 = 0
    try:
        resultado = numero1 / numero2
    except ZeroDivisionError:
        print("Ocurrio un error de division")
        break