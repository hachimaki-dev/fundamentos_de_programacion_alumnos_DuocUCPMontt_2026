# Calculadora simple en Python
# El programa asume que el usuario ingresa un número válido, en caso contrario dará un error al no poder parsear el valor a integer.

numero1 = int(input("Ingrese su primer número: "))

operacion = input("Indique el número de la operación que desea realizar. Opciones válidas: +    -    x    :     ")

numero2 = int(input("Ingrese su segundo número: "))

if operacion == "+":
    resultado = numero1 + numero2
    print(f"{numero1} + {numero2} = {resultado}")
elif operacion == "-":
    resultado = numero1 - numero2
    print(f"{numero1} - {numero2} = {resultado}")
elif operacion == "x":
    resultado = numero1 * numero2
    print(f"{numero1} x {numero2} = {resultado}")
elif operacion == ":":
    resultado = numero1 / numero2
    print(f"{numero1} : {numero2} = {resultado}")
else:
    print("Operación inválida.")
