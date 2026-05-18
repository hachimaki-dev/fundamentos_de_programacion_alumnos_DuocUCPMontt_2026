operador = input("operador:(+,-,*,/) ")
numero_1 = float(input("nuemro 1: "))
numero_2 = float(input("numero 2: "))

if operador == "+":
    resultado = numero_1 + numero_2
elif operador == "-":
    resultado = numero_1 - numero_2
elif operador == "*":
    resultado = numero_1 * numero_2
elif operador == "/":
    resultado = numero_1 / numero_2
else:
    print("operador no valido")
print(resultado)
