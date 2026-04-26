saldo=50000
cajero=100000
opcion=0
retiro=0
inversion=0
print("====Bienvenido al cajero automatico====")
while saldo > 0 and cajero > 0:
    print("1-Ver saldo")
    print("2-Girar dinero")
    print("3-Invertir")
    print("4-Salir")
    opcion=int(input("¿Que operacion solicita hacer? "))
    if opcion==1:
        print(f"Su saldo es: {saldo}")
    elif opcion==2:
        retiro =int(input("Cuanto dinero desea retirar (solo billetes de 5 mil) "))
        if retiro > saldo:
            print("Error: Saldo insuficiente")
        elif retiro%5 != 0:
            print("Error: Retiro no disponible")
        elif retiro % 5 ==0:
            print(f"Dinero retirado")
            saldo = saldo-retiro
            cajero= cajero-retiro
    elif opcion==3:
        inversion=int(input("Cuanto desea invertir: "))
        if inversion > saldo:
            print("Error: Saldo insuficiente")
        elif inversion <= saldo:
            print("Inversion hecha con exito")
            inversion *=2
            saldo = inversion + saldo
    elif opcion >= 5:
        print("Error: Ingrese una opcion valida")
    elif opcion<1:
        print("Error: Ingrese una opcion valida")
    else:
        print("Cajero apagado...")
        break
print("====Fin====")
