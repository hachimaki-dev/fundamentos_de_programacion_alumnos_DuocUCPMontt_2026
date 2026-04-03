#hacer una calculadora en python para sumar, restar, multiplicar y dividir

tipo_de_modo = input("Elige modo (Sumar, Restar, Multiplicar, Dividir): ")

numero1 = input("Ingrese su primer numero: ")
numero2 = input("Ingrese el segundo numero: ")

#if = si (el programa hace una desición)
#El doble "==" es una comparación

# tradución si tipo de mode es igual a Sumar entonces resultado es la suma del numero1 y el numero2
if tipo_de_modo == "Sumar":
    resultado = int(numero1) + int(numero2)

if tipo_de_modo == "Restar":
    resultado = int(numero1) - int(numero2)

if tipo_de_modo == "Multiplicar":
    resultado = int(numero1) * int(numero2)

if tipo_de_modo == "Dividir":
    resultado = int(numero1) / int(numero2)

print(f"El resultado la operación es {resultado}")