# Repite la solicitud hasta que el usuario ingrese un entero válido (puede ser cualquier entero, positivo, negativo o cero)
while True:
    try:
        usuario_ingresa_numero = int(input("Ingrese solo un numero :"))
        print(f"numero ingresado {usuario_ingresa_numero}")
    except ValueError:
        print("Error : no es un numero entero")
