saldo_inicial = 50000

while True:
    opción_user = int(input("Menú de opciones. Elija un numero: \n1) Ver saldo \n2) Girar Dinero \n3) Inversión \n4) Salir \n"))
    if opción_user == 1:
        print(f"El saldo actual es de {saldo_inicial} ")
    
    elif opción_user == 2:
        monto_elegido_giro = int(input("Ingrese el monto que desea girar"))
        if monto_elegido_giro <= saldo_inicial and monto_elegido_giro % 5000 == 0:
            saldo_inicial -= monto_elegido_giro
        else:
            print("monto no aceptado. Puede que tu saldo sea insuficiente")
    
    elif opción_user == 3:
        monto_elegido_inversion = int(input("Ingrese el monto que desea invertir"))
        if monto_elegido_inversion <= saldo_inicial:
            monto_elegido_inversion *= 2
            saldo_inicial += monto_elegido_inversion
        else:
            print("Saldo insuficiente")

    elif opción_user == 4
        print("Cajero apagado")
        break
    
    else:
        print("Opción invalida")

