continuar = True
while continuar:
    try:
        edad_cliente = int(input("Ingrese su edad, conductor: "))
        if edad_cliente <= 0:
            print("Debe ingresar una edad válida.")
        else:
            print(f"Edad registrada : {edad_cliente} años.")
            continuar = False
    except ValueError:
        print("Error, ingerese numeros enteros positivos.")