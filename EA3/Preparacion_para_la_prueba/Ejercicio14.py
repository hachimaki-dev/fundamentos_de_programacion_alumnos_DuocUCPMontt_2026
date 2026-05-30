# Ejercicio 14 — Sistema de caja de una cafetería
# Una cafetería comienza con $0 en caja. El cajero trabaja con el siguiente menú:

# === SISTEMA DE CAJA CAFETERÍA CAMPUS ===
# 1. Ver saldo en caja
# 2. Registrar venta (ingresa monto)
# 3. Registrar gasto (ingresa monto)
# 4. Salir
# Reglas:

# Las ventas suman al saldo
# Los gastos restan, pero no se puede gastar más de lo que hay en caja
# Monto siempre es entero positivo (validar)
# El menú se repite hasta que se elija salir
# Al salir: "Cierre de caja: $45.300 en caja. Hasta mañana."

saldo_de_la_caja = 0

print(" === SISTEMA DE CAJA CAFETERÍA CAMPUS ===")
while True:
    try:
        opcion_elegida = int(input("1. Ver saldo en caja\n" \
        "2. Registrar venta (ingresa monto)\n" \
        "3. Registrar gasto (ingresa monto)\n" \
        "4. Salir\n" \
        "Ingresa una opción: "))

        if opcion_elegida == 1:
            print(f"El saldo de la caja es {saldo_de_la_caja}\n")

        elif opcion_elegida == 2:
            while True:
                try:
                    saldo_ingresado_en_caja = int(input("Ingrese el monto de la venta: "))

                    if saldo_ingresado_en_caja > 0:
                        print(f"Ingreso existo de ${saldo_ingresado_en_caja}\n")
                        saldo_de_la_caja += saldo_ingresado_en_caja
                        break
                    else:
                        print("Ingrese un monto positivo\n")
                except ValueError:
                    print("ValueError: Ingrese un número entero positivo\n")

        elif opcion_elegida == 3:
            while True:
                try:
                    saldo_egresado_en_caja = int(input("Ingrese el monto del gasto: "))

                    if saldo_egresado_en_caja <= 0:
                        print("Ingrese un monto positivo\n")

                    elif saldo_egresado_en_caja > saldo_de_la_caja:
                        print("Fondos insuficientes para el gasto\n")

                    else:
                        saldo_de_la_caja -= saldo_egresado_en_caja
                        print("Gasto registrado\n")
                        break

                except ValueError:
                    print("ValueError: Ingrese un número entero positivo\n")

        elif opcion_elegida == 4:
            print(f"Cierre de la caja: ${saldo_de_la_caja} en caja. Hasta mañana\n")
            break

        else:
            print("Opción no Valida ingrese un número entre el 1 al 4\n")
    except ValueError:
        print("ValueError: Opción no valida ingrese un número entero positivo\n")        