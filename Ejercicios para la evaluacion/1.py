try:
    numero = int(input("Escribe un numero entero: "))
    print(f"Escogiste el numero {numero}.")
except ValueError:
    print("¡Error! Debes ingresar un número válido.")