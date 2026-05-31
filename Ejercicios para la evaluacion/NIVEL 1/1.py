flag = True
while flag:
    try:
        numero = int(input("Escribe un numero entero: "))
        flag = False
    except ValueError:
        print("¡Error! Debes ingresar un número válido.")
print(f"Escogiste el numero {numero}.")