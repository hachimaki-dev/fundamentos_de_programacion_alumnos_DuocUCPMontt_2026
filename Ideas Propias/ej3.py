print("Cajero Automático")

saldo = 50000
opcion = 0

while opcion != 4:

    print("\n1) Ver Saldo")
    print("2) Girar Dinero")
    print("3) Inversión")
    print("4) Salir")

    opcion = int(input("Seleccione una opción: "))

    if opcion == 1:
        print("Su saldo actual es:", saldo)

    elif opcion == 2:
        monto = int(input("Ingrese el monto a girar: "))

        if monto <= saldo:
            if monto % 5000 == 0:
                saldo = saldo - monto
                print("Giro realizado. Nuevo saldo:", saldo)
            else:
                print("Monto no aceptado")
        else:
            print("Saldo insuficiente")

    elif opcion == 3:
        inversion = int(input("Ingrese monto a invertir: "))

        if inversion <= saldo:
            ganancia = inversion * 2
            saldo = saldo + ganancia
            print("Inversión exitosa. Nuevo saldo:", saldo)
        else:
            print("Saldo insuficiente")

    elif opcion == 4:
        print("Cajero apagado")

    else:
        print("Opción inválida")