while True:
    try:
        valor= int(input("Ingresa un número: "))
        break
    except ValueError:
        print("Error: eso no es un número entero")