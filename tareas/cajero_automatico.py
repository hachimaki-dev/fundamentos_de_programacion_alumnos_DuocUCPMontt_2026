saldo = 80000
intentos = 3
pin = 2417
print("BIENVENIDO AL CAJERO AUTOMATICO")
while intentos != 0:
    print("-----por favor ingrese su pin de 4 digitos------")
    pin_usuario = int(input())
    if pin_usuario == pin :
        print("pin correcto")
        break
    elif pin_usuario != pin: 
        print("pin incorrecto")
        intentos = intentos - 1
        print("vuelva a intentar")
        print(f"le quedan {intentos}")
        if intentos == 0:
            print("tarjeta bloqueada---")
            break
            
while intentos != 0:
    

    monto = int(input("introdusca monto a retirar"))
    if monto > saldo:
       print("saldo insuficiente")
    elif monto <= 0:
     print("monto invalido")

    else:
     saldo = saldo - monto
     print(f"retiraste exitosamente {monto}")
     print(f"saldo actual es de {saldo}")
     
    if saldo == 0:
        print("saldo insuficiente para hacer mas retiros")
        break


