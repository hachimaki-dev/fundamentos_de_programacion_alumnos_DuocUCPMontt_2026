while True:
    try:
        edad = int(input("Por favor, ingresa la edad del conductor: "))
        
        if edad > 0:
            print(f"Edad registrada: {edad} años.")
            break
        else:
            print("Error: La edad debe ser un número entero mayor a cero.")
            
    except ValueError:
        print("Error: Entrada inválida. Debes ingresar un número entero.")