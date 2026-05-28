while True:
    try:
        numero_ingresado = int(input("Ingrese su numero entero: "))
        resultado_numero_ingresado = numero_ingresado 
        print(f"Numero recibido {resultado_numero_ingresado}")
        
    except ValueError:
        print("Error: eso no es un numero entero.")