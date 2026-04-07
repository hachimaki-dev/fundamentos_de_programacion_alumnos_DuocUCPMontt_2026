saldo_inicial = 50000
menu = input("1) Ver saldo 2) Girar Dinero 3) Inversión 4) Salir: ")
while True:
    if menu == "1":
        print("Su saldo actual es: ", saldo_inicial)
    elif menu == "2":
        giro = int(input("Ingrese el monto a girar: "))
        if giro <= saldo_inicial and giro % 5000 == 0:
            saldo_inicial -= giro
            print("Giro realizado. Su nuevo saldo es: ", saldo_inicial)
        else:
            print("Saldo insuficiente o monto no aceptado.")
    elif menu == "3":
        inversion = int(input("Ingrese el monto a invertir: "))
        if inversion <= saldo_inicial:
            inversion = inversion * 2
            print("Su nuevo saldo después de la inversión es: ", saldo_inicial + inversion)
        else:
            print("Saldo insuficiente.")
    elif menu == "4":
        print("Cajero apagado.")
    else:
        print("Opción inválida.")
    
    menu = input("1) Ver saldo\n2) Girar Dinero\n3) Inversión\n4) Salir: ")