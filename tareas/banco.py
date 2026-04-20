saldo = 50000
opcion = 0
while opcion != 4:
    print("banco estao")
    print("--menu--")
    print("1 . ver saldo")
    print("2 . girar dinero")
    print("3 . inversion")
    print("4 . salir")
    opcion = int(input("Ingrese su opcion (del 1 al 4) :"))
if opcion == 1:
    print(f"su saldo disponible es : {saldo}")
elif opcion == 2:
    monto_retiro = int(input("Cuanto desea retirar"))
    if monto_retiro > saldo :
        print("Saldo insuficiente")
    else :
        if monto_retiro % 5000 == 0:
            saldo = saldo - monto_retiro
            print(f"Su nuevo saldo es : {saldo}")
elif opcion == 3:
    print("Ha ingresado al menu de inversion")
    monto_deposito = float("Ingrese monto a invertir")
    if monto_deposito <= saldo:
        saldo = saldo - monto_deposito
        retorno_de_inversion = monto_deposito*2
        print(f"su monto de retorno es : {retorno_de_inversion}")
elif opcion == 4:
    print("Ha salido del menu")
else :
    print("Ingrese opcion valida")