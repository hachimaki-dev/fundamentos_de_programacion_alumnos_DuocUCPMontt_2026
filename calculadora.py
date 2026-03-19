print("Inicio")
# + suma
# - resta
# * multiplicar
# / dividir
"""
(1) suma
(2) resta
(3) multiplicar
(4) dividir
(5) potencia
"""

def calculadora(num1, num2, op):
    if op == 1:
        print(f"El resultado de la suma es {num1 + num2}")
    elif op == 2:
        print(f"El resultado de la resta es {num1 - num2}")
    elif op == 3:
        print(f"El resultado de la multiplicación es {num1 * num2}")
    elif op == 4:
        print(f"El resultado de la división es {num1 / num2}")
    elif op == 5:
        print(f"El resultado de la potencia es {num1 ** num2}")
    else:
        print("Syntax error")

variable1 = float(input("Introduzca el primer valor: "))
variable2 = float(input("Introduzca el segundo valor: "))
calculadora(variable1, variable2, 1)