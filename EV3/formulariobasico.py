while True:
    try:
        edad = int(input("Ingrese su edad: "))
        if edad > 0:
            break
        else:
            print("Entrada invalida. Ingrese un numero entero positivo")
    except ValueError:
        print("Error. Ingrese un numero")
        
print(f"edad registrada: {edad} años.")
