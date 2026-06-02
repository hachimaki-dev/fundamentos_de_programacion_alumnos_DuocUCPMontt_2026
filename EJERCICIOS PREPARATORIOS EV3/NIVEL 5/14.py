opcion = 0
venta = 0
gasto = 0
total = 0

while opcion != 4:

    print("\n=== SISTEMA DE CAJA CAFETERÍA CAMPUS ===")
    print("1. Ver saldo en caja")
    print("2. Registrar venta (ingresa monto)")
    print("3. Registrar gasto (ingresa monto)")
    print("4. Salir")

    while True:
        try:
            opcion = int(input("Ingresa número de la opción: "))
            if 1 <= opcion <= 4:
                break
            else:
                print("Error: Ingrese una opción válida")
        except ValueError:
            print("Error: Ingrese una opción válida")
    
    if opcion == 4:
        print(f"Cierre de caja: ${total} en caja. Hasta mañana")
        break

    elif opcion == 1:
        print(f"El saldo de la caja es: ${total}")

    elif opcion == 2:
        while True:
            try:
                registro_venta = int(input("Monto de la venta: $"))
                if registro_venta > 0:
                    break
                else:
                    print("Error: El monto debe ser mayor a 0.")
            except ValueError:
                print("Error: El monto debe estar en formato númerico, entero positivo")
        venta += registro_venta
        total += registro_venta
        print(f"Registraste venta: ${registro_venta}")
        print(f"Total ventas: ${venta}")
    
    else:
        while True:
            try:
                registro_gasto = int(input("Monto del gasto : $"))
                if registro_gasto > 0:
                    break
                else:
                    print("Error: El monto debe ser mayor a 0.")
            except ValueError:
                print("Error: El monto debe estar en formato númerico, entero positivo")

        if registro_gasto > total:
            print("Error: no puedes gastar más dinero del que hay en caja.")
        else:
            gasto += registro_gasto
            total -= registro_gasto
            print(f"Registraste gasto: ${registro_gasto}")
            print(f"Total gastos: ${gasto}")