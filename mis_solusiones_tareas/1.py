while True:
    try:
        numeros_enteros = int(input("inresa un numero entero"))
        print(f"numero resibido: {numeros_enteros}")
        break
    except ValueError:
        print("error: eso no es un numero entero")
