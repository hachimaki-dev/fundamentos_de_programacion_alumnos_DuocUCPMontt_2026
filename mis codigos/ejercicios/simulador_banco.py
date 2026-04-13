saldo_inicial = 50000

while True:

    print("----- MENU -----")
    print("1. Ver Saldo")
    print("2. Girar Dinero")
    print("3. Inversion")
    print("4. Salir\n")
    opcion_seleccionada = int(input("Elija su opcion escribiendo el numero correspondiente: "))

    if opcion_seleccionada == 1:
        print(f"Saldo actual es de ${saldo_inicial}\n")

    elif opcion_seleccionada == 2:
        monto_girar = int(input("¿Cuanto desea girar?:$"))

        if monto_girar > saldo_inicial:
            print(f"Saldo insuficiente, su saldo actual es de ${saldo_inicial}\n")

        elif monto_girar <= saldo_inicial and monto_girar % 5000 == 0:
            saldo_inicial -= monto_girar 
            print(f"El giro se ha realizado con exito, su saldo actual es de ${saldo_inicial}\n")
        else:
            print("Monto no aceptado\n")
    
    elif opcion_seleccionada == 3:
        print("¡Te ofrecemos DUPLICAR tu dinero en nuestro banco mas confiable del mundo! :D\n")
        inversion = int(input("¿Cuanto desea invertir?: $"))

        if inversion <= saldo_inicial:
            saldo_inicial -= inversion
            retorno = inversion * 2
            saldo_inicial += retorno
            print("Gracias por invertir con nosotros :D")
            print(f"Su saldo final de retorno es de ${saldo_inicial}\n")

        else:
            print("Saldo insuficiente\n")

    elif opcion_seleccionada == 4:
        print("----- Cajero apagado -----")
        break

    else:
        print("Opcion invalida")