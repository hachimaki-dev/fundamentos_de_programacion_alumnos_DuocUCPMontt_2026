saldo = 50000

while True:
    print("1) Ver Saldo")
    print("2) Girar Dinero")
    print("3) Inversión")
    print("4) Salir")
    
    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        print("Saldo actual:", saldo)

    elif opcion == "2":
        monto = int(input("¿Cuánto desea girar?: "))
        
        if monto > saldo:
            print("Saldo insuficiente")
        elif monto % 5000 != 0:
            print("Monto no aceptado")
        else:
            saldo -= monto
            print("Retiro exitoso. Nuevo saldo:", saldo)

    elif opcion == "3":
        inversion = int(input("¿Cuánto desea invertir?: "))
        
        if inversion > saldo:
            print("Saldo insuficiente")
        else:
            saldo -= inversion
            ganancia = inversion * 2
            saldo += ganancia
            print("Inversión realizada. Nuevo saldo:", saldo)

    elif opcion == "4":
        print("Cajero apagado")
        break

    else:
        print("Opción inválida")
        
        
        
        
