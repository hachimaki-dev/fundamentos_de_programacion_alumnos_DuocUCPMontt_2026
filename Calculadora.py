print("Bienvenido a la calculadora")

Numero1= float(input("Ingrese el primer número "))

Numero2= float(input("Ingrese el segundo número "))

operacion= input("Ingrese una operacion (+,-,*./) ")

if operacion== "+":
    resultado= (Numero1 + Numero2)

elif operacion== "-":
    resultado= (Numero1 - Numero2)

elif operacion== "*":
    resultado= (Numero1 * Numero2)

elif operacion== "/":
    resultado= (Numero1 / Numero2)

else:
    print("Operacion no valida")

print(f"Resultado: {resultado}")