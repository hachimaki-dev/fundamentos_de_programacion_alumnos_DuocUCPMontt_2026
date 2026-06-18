# Ejercicio 1A — Solo capturar ValueError (calentamiento)

while True:
    try:
        numero_entero = int(input("Ingrese un número entero: "))
        print(f"Numero recibido {numero_entero}")
        break
    except ValueError:
        print("Error, eso no es un número entero")