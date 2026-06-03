while True:
    try:
        edad = int(input("Ingrese su edad: "))
        if edad <= 0:
            print("Entrada inválida. Ingresa un número entero positivo.")
        else:
            print(f"Edad registrada: {edad} años.")
            
    except ValueError:
        print("Dato invalido: Solo se permiten numeros enteros positivos.")