# Una aerolínea necesita saber cuántos pasajeros abordaron un vuelo. El número debe ser mayor que cero (no puede haber un vuelo con cero o menos pasajeros).

# Escribe un programa que pida el número de pasajeros y que no avance hasta recibir un entero positivo. Si el dato es inválido, muestra:
while True:
    try:
        ingresado_numero_pasajeros = int(input("Ingrese la cantidad de pasajeros"))
        if ingresado_numero_pasajeros > 0:
            print(f"vuelo registrado con {ingresado_numero_pasajeros}")
    except ValueError:
        print("Error : ingresa un numero entero positivo de pasajeros")