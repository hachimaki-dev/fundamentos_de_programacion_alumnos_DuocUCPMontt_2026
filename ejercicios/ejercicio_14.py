# Ejercicio 14 — Sistema de caja de una cafetería

saldo = 0

while True:

    print("=== SISTEMA DE CAJA CAFETERÍA CAMPUS ===")
    print("1. Ver saldo en caja")
    print("2. Registrar venta")
    print("3. Registrar gasto")
    print("4. Salir")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        print(f"Saldo actual: ${saldo}")

    elif opcion == "2":

        try:
            venta = int(input("Ingrese monto de la venta: "))

            if venta > 0:
                saldo += venta
            else:
                print("El monto debe ser positivo.")

        except ValueError:
            print("Debe ingresar un número entero.")

    elif opcion == "3":

        try:
            gasto = int(input("Ingrese monto del gasto: "))

            if gasto <= 0:
                print("El monto debe ser positivo.")

            elif gasto > saldo:
                print("No hay saldo suficiente.")

            else:
                saldo -= gasto

        except ValueError:
            print("Debe ingresar un número entero.")

    elif opcion == "4":
        print(f"Cierre de caja: ${saldo} en caja. Hasta mañana.")
        break

    else:
        print("Opción inválida.")