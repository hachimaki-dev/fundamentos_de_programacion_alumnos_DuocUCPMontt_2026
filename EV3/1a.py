error = True
while error:
    try:
        num_entero = int(input("Ingrese un número entero: "))
        print(f"Número recibido: {num_entero}")
        error = False
    except ValueError:
        print("Error: eso no es un número entero.")