# Programa que suma los números naturales del 1 hasta el número N ingresado por el usuario

acumulador = 0
numero_n = int(input("Ingresa un número natural: "))
rango = range(1, numero_n + 1)

for x in rango:
    print(f"Número: {x}")
    acumulador += x
    print(f"Total al sumar = {acumulador}")
