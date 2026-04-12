saldo_inicial = 50000
ver_saldo = 1
girar_dinero = 2
invertir = 3
salir = 4
accion = 0
monto_a_girar=0
multiplo5 = 0
while accion != 4:

    print("Bienvenido al banco Pelluco")
    print("¿Qué operación desea realizar?")
    print("""
        (1) Ver saldo
        (2) Girar dinero
        (3) Invertir
        (4) Salir""")
    accion = int(input(""))
    #VER SALDO
    if accion == 1:
        print(f"Su saldo actualmente es de: ${saldo_inicial} pesos")
    #GIRAR DINERO
    elif accion == 2:
        print("Ingrese el monto a girar. (Ejemplo: $5000, $10000, $15000, etc.")
        monto_a_girar = int(input("$"))
        multiplo5 = monto_a_girar % 5000
        if monto_a_girar > saldo_inicial:
            print("Saldo insuficiente")
        elif multiplo5 != 0 or monto_a_girar < 5000:
            print("Monto no aceptado")
            print(multiplo5)
        else:
            int(monto_a_girar)
            print(f"Excelente, retire sus ${monto_a_girar}")
            saldo_inicial=saldo_inicial - monto_a_girar
    #INVERTIR     
    elif accion == 3:
        print("Inversiones Pelluco SA")
        print("Ingrese el monto a invertir")
        monto_a_girar = int(input("$"))
        if monto_a_girar > saldo_inicial:
            print("Saldo insuficiente")
        elif monto_a_girar == saldo_inicial or monto_a_girar < saldo_inicial:
            print("INVIRTIENDO EN ETFS...")
            monto_a_girar = monto_a_girar *2
            saldo_inicial = saldo_inicial + monto_a_girar
            print("consulte su monto para ver sus resultados")
    else:
        print("")
print("Apagando Cajero")
print("Zzz...")