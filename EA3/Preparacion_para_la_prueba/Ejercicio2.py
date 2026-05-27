# Ejercicio 2 — Stock de una farmacia
# Una farmacia necesita ingresar la cantidad de unidades disponibles de un medicamento. No puede ser cero ni negativo (una farmacia con stock negativo no tiene sentido).

# Escribe un programa que pida la cantidad de unidades. Si es inválida, muestra:

# "Dato inválido. Ingresa un entero positivo para el stock."
# Cuando sea válido, muestra el valor que el usuario ingresó:

# "Stock registrado: {cantidad} unidades disponibles."
# (Ejemplo: si el usuario ingresa 350, se muestra "Stock registrado: 350 unidades disponibles.")

# Piensa: ¿Qué diferencia hay entre capturar ValueError y validar con > 0? ¿Necesitas ambas cosas?

while True:
    try:
        cantidad_de_unidades = int(input("Ingrese la cantidad de unidades disponibles del medicamnto: "))

        if cantidad_de_unidades <= 0:
            print("No puede ser cero ni negativo")
        else:
            print(f"Stock registrado: {cantidad_de_unidades} unidades disponibles.")
            break

    except ValueError:
        print("Dato inválido. Ingresa un entero positivo para el stock.")