saldo = 50000
opcion = 0 #opcion para el menú de opciones

while opcion != 4: #porque la opcion 4 es la de salir
    print("\n -----Menú de opciones-----")
    print("1. Consultar Saldo")
    print("2. Retirar Saldo")
    print("3. Invertir")
    print("4. Salir")
    opcion = int(input("Seleccione una opción: "))

    if opcion == 1:
        print(f"Su saldo actual es:${saldo}")
    elif opcion == 2:
        monto_retiro = int(input("Ingrese el monto a retirar: $"))
        if monto_retiro > saldo:
            print("Saldo insuficiente para realizar el retiro.")
        else:
            if monto_retiro % 5000 == 0: #Se pone para comprobar si el monto ingresado es multiplo de X numero
                saldo -= monto_retiro 
                print(f"Retiro exitoso, su nuevo saldo es: ${saldo}")
            else:
                print("Monto no aceptado, El monto debe ser multiplo de 5000.")
    elif opcion == 3:
        monto_inversion= int(input("Ingrese el monto a invertir: "))
        if monto_inversion <= saldo:
            saldo = saldo - monto_inversion #Se resta el saldo menos el monto a invertir
            retorno_inversion = monto_inversion * 2 #Se multiplica por 2 para el retorno luego de invertir
            saldo = saldo + retorno_inversion #Se suma el saldo más el retorno
            print(f"inversion exitosa, Su nuevo saldo es: ${saldo}") 
        else:
            print("Saldo insuficiente para realizar la inversion.")
    elif opcion == 4:
        print("Que tenga buen día.")
    else:
        print("Opcion no valida por favor selecciones una opcion del menu.")#Por si no elige ni la opcion 1,2,3,4.

            

