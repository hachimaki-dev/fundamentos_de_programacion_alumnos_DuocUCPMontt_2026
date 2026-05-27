# Ejercicio 1B — Registro de pasajeros en un vuelo
# Una aerolínea necesita saber cuántos pasajeros abordaron un vuelo. El número debe ser mayor que cero (no puede haber un vuelo con cero o menos pasajeros).

# Escribe un programa que pida el número de pasajeros y que no avance hasta recibir un entero positivo. Si el dato es inválido, muestra:

# "Error: ingresa un número entero positivo de pasajeros."
# Cuando el dato sea válido, muestra el valor que el usuario ingresó:

# "Vuelo registrado con {pasajeros} pasajeros."
# (Ejemplo: si el usuario ingresa 142, se muestra "Vuelo registrado con 142 pasajeros.")

# Casos de prueba que debes intentar: 0, -5, "abc", 3.7, 200

while True:
    try:
        cantidad_de_pasajeros = int(input("¿Cúantos pasajeros abordar el vuelo?: "))

        if cantidad_de_pasajeros <= 0:
            print("No puede haber un vuelo con cero o menos pasajeros")
        else:
            print(f"Vuelo registrado con {cantidad_de_pasajeros} pasajeros.")
            break

    except ValueError:
        print("Error: ingresa un número entero positivo de pasajeros.")
