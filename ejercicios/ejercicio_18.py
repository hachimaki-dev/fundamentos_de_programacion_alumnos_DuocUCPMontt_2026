# Ejercicio 18 — Sistema de registro de técnicos en una empresa minera

tecnicos = []

tecnicos_maestros = 0
tecnicos_operarios = 0

while True:

    try:
        cantidad_tecnicos = int(input("Ingrese la cantidad de técnicos: "))

        if cantidad_tecnicos > 0:
            break

        print("Error: debe ingresar un número positivo.")

    except ValueError:
        print("Error: debe ingresar un número entero.")

for i in range(cantidad_tecnicos):

    print(f"\nTécnico {i + 1}")

    while True:

        codigo = input("Ingrese el código del técnico: ")

        if len(codigo) >= 6 and " " not in codigo:
            break

        print("Error: código inválido.")

    while True:

        try:
            experiencia = int(input("Ingrese años de experiencia: "))

            if experiencia > 0:
                break

            print("Error: debe ingresar un número positivo.")

        except ValueError:
            print("Error: debe ingresar un número entero.")

    if experiencia > 10:
        categoria = "Técnico Maestro"
        tecnicos_maestros += 1
    else:
        categoria = "Técnico Operario"
        tecnicos_operarios += 1

    tecnico = {"codigo": codigo, "experiencia": experiencia, "categoria": categoria}

    tecnicos.append(tecnico)

print("\nLISTA DE TÉCNICOS")

for tecnico in tecnicos:
    print(tecnico)

print()
print(f"La planta cuenta con {tecnicos_maestros} Técnicos Maestros y {tecnicos_operarios} Técnicos Operarios. Sistema listo.")