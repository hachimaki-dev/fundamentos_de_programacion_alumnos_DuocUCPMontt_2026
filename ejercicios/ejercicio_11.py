# Ejercicio 11 — Registro de despachos en una empresa de transporte

carga_pesada = 0
carga_normal = 0
peso_total = 0

while True:

    try:
        cantidad_paquetes = int(input("Ingrese la cantidad de paquetes: "))

        if cantidad_paquetes > 0:
            break

        print("Error: debe ingresar un número positivo.")

    except ValueError:
        print("Error: debe ingresar un número entero.")

for i in range(cantidad_paquetes):

    while True:

        try:
            peso = int(input(f"Ingrese el peso del paquete {i + 1}: "))

            if peso > 0:
                break

            print("Error: el peso debe ser positivo.")

        except ValueError:
            print("Error: debe ingresar un número entero.")

    while True:

        codigo = input("Ingrese el código del paquete: ")

        if len(codigo) >= 6 and " " not in codigo:
            break

        print("Código inválido.")

    peso_total += peso

    if peso > 20:
        carga_pesada += 1
    else:
        carga_normal += 1

print()
print(f"Cargas pesadas: {carga_pesada}")
print(f"Cargas normales: {carga_normal}")
print(f"Peso total despachado: {peso_total} kg")