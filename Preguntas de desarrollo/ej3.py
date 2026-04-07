bandera = True
Saldo = 50000

print("Bienvenido al banco virtual de PYTHON")

while bandera:
    print("Tienes las siguientes opciones")
    print("1.Ver SALDO")
    print("2.GIRAR DINERO")
    print("3.INVERSION")
    print("4.SALIR")
    eleccion = int(input("Seleccione su opción (Escoja un numero del 1 al 4)"))

    if eleccion == 1:
        print(f"Su saldo actual es de ${Saldo}CLP")
    if eleccion == 2:
        saldo_a_girar = int(input("¿Cuanto dinero desea retirar?"))
        if saldo_a_girar > 0:
            respuesta = input(f"¿Estas seguro de querer retirar ${saldo_a_girar}CLP (responder con SI y NO)?")
            if respuesta == "SI" and Saldo > saldo_a_girar:
                Saldo = Saldo - saldo_a_girar
                print(f"Perfecto, usted ha retirado ${saldo_a_girar}CLP con exito!!!")
                print(f"Su nuevo saldo es de ${Saldo}CLP")
            elif respuesta == "SI" and Saldo < saldo_a_girar:
                print("Lo sentimos, su saldo es insuficiente...")
            elif respuesta == "NO":
                print("Perfecto, entonces volvemos al menu")
            else:
                print("Caracter INVALIDO")
    if eleccion == 3:
        inversion = int(input("¿Cuanto dinero desea invertir?"))
        if Saldo >= inversion:
            print("Perfecto, su inversion se ha realizado con exito")
            Saldo = Saldo * 2
            print("Haz recuperado el doble de lo invertido")
            print(f"Su saldo actual es de ${Saldo}CLP")
        elif Saldo < inversion:
            print("Saldo insuficiente")
        else:
            print("Caracter Invalido")
    if eleccion == 4:
        print("Cajero apagado")
        import sys
        sys.exit ()