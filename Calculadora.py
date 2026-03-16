print("Bienvenido a la calculadora")

Numero1= int(input("Ingrese el primer número "))

Numero2= int(input("Ingrese el segundo número "))

operacion= input("Ingrese una operacion (+,-,*./) ")

if operacion== "+":
    resultado= int(Numero1 + Numero2)

elif operacion== "-":
    resultado= int(Numero1 - Numero2)

elif operacion== "*":
    resultado= int(Numero1 * Numero2)

elif operacion== "/":
    resultado= int(Numero1 / Numero1)

else:
    print("Operacion no valida")

print(f"Resultado: {resultado}")