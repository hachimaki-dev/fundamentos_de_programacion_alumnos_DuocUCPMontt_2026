saldo = 50000
Operacion = True
while Operacion == True:
    print(f"""Bienevenido al Banco Santander: 
Elija una opción
1) Ver Saldo
2) Girar Dinero
3) Inversión
4) Salir """)
    
    Opcion = int(input())

    if Opcion == 1:
        print(f"\nSu saldo es ${saldo}")
    elif Opcion == 2:
        print ("¿Cuanto dinero desea retirar?")
        DineroARetirar = int(input("Ingrese cifra a retirar: "))
        if DineroARetirar == 0:
            print("\nMonto inválido")
            print("\n Intente nuevamente")
        elif DineroARetirar > saldo:
            print("\nFondos insuficientes")
            print("\n Intente nuevamente")
        else:
            saldo = saldo - DineroARetirar
            print (f"Retiro exitoso: \nUsted retiro \n${DineroARetirar} \ny su saldo actual es \n${saldo}")
    elif Opcion == 3:
        print ("¿Cuanto dinero desea invertir?")
        DineroInvertir = int(input("Ingrese cifra a invertir: "))
        if DineroInvertir == 0:
            print("\nMonto inválido")
            print("\n Intente nuevamente")
        elif DineroInvertir > saldo:
            print("\nFondos insuficientes")
            print("\n Intente nuevamente")
        else:
            saldo = saldo + (DineroInvertir * 2)
            print (f"Dinero invertido con exito: \nDinero invertido ${DineroInvertir} \n Ganancias = ${DineroInvertir * 2}\nSu saldo actual es \n${saldo}")
    elif Opcion == 4:
        break
    else:
        print("Opcion Invalida")