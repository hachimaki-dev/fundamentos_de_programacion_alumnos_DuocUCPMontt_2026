# Ejercicio 19 — Registro de vehículos en una empresa de transporte de carga

vehiculos = []

camiones_pesados = 0
camiones_livianos = 0

while True:

    try:
        cantidad_vehiculos = int(input("Ingrese la cantidad de vehículos: "))

        if cantidad_vehiculos > 0:
            break

        print("Error: debe ingresar un número positivo.")

    except ValueError:
        print("Error: debe ingresar un número entero.")

for i in range(cantidad_vehiculos):

    print(f"\nVehículo {i + 1}")

    while True:

        patente = input("Ingrese la patente: ")

        if len(patente) == 6 and " " not in patente:
            break

        print("Error: patente inválida.")

    while True:

        try:
            capacidad = int(input("Ingrese capacidad de carga (toneladas): "))

            if capacidad > 0:
                break

            print("Error: debe ingresar un número positivo.")

        except ValueError:
            print("Error: debe ingresar un número entero.")

    if capacidad > 15:
        categoria = "Camión pesado"
        camiones_pesados += 1
    else:
        categoria = "Camión liviano"
        camiones_livianos += 1

    vehiculo = {
        "patente": patente,
        "capacidad": capacidad,
        "categoria": categoria
    }

    vehiculos.append(vehiculo)

print("\nLISTA DE VEHÍCULOS")

for vehiculo in vehiculos:
    print(vehiculo)

print()
print(f"La flota cuenta con {camiones_pesados} camiones pesados y {camiones_livianos} camiones livianos. Registro completado.")