# Ejercicio 13 — Inventario de computadores en una empresa TI

equipos_obsoletos = 0
equipos_vigentes = 0

while True:

    try:
        cantidad_equipos = int(input("Ingrese la cantidad de equipos: "))

        if cantidad_equipos > 0:
            break

        print("Error: debe ingresar un número positivo.")

    except ValueError:
        print("Error: debe ingresar un número entero.")

for i in range(cantidad_equipos):

    while True:

        codigo = input(f"Ingrese el código del equipo {i + 1}: ")

        if len(codigo) >= 6 and " " not in codigo:
            break

        print("Código inválido.")

    while True:

        try:
            anio = int(input("Ingrese el año de fabricación: "))

            if 1990 <= anio <= 2026:
                break

            print("Error: el año debe estar entre 1990 y 2026.")

        except ValueError:
            print("Error: debe ingresar un número entero.")

    if anio < 2018:
        equipos_obsoletos += 1
    else:
        equipos_vigentes += 1

print()
print(f"Equipos obsoletos: {equipos_obsoletos}")
print(f"Equipos vigentes: {equipos_vigentes}")