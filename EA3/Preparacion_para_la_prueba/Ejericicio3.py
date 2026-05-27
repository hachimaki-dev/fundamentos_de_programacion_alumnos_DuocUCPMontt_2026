# Ejercicio 3 — Edad de un conductor para arriendo de autos
# Una empresa de arriendo de vehículos solicita la edad del conductor. Debe ser un entero positivo (nadie tiene -3 años ni 0 años).

# El programa debe pedir la edad repetidamente hasta recibir un valor válido. Luego muestra:

# "Edad registrada: 29 años."
# Desafío extra: ¿Qué pasa si el usuario ingresa "veintinueve"? ¿Tu código lo maneja?

while True:
    try:
        edad_del_conductor = int(input("Ingrese su edad: "))

        if edad_del_conductor <= 0:
            print("Ingrese números enteros positivos.")
        else:
            print(f"Edad registrada: {edad_del_conductor} años.")
            break

    except ValueError:
        print("Dato inválido. Ingresa un número entero positivo.")
