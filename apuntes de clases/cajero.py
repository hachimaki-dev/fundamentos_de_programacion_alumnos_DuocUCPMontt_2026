saldo = 50000
PIN = 1604
NUMERO_MAXIMO_INTENTOS = 3
contador_intentos_falllidos = 0


print("BIENVENIDOS AL BANCO ESTADO")

while True :
    pin_ingresado = int(input("Por favor ingrese su clave secreta"))

    if pin_ingresado == PIN :
        print("HAZ ACCEDIDO")
    elif pin_ingresado != PIN :
        print("ingrese una contraseña valida")
        contador_intentos_falllidos = contador_intentos_falllidos + 1
    else:
        print("no haz accedido")
        
        if contador_intentos_falllidos >= 3 :
            break


    print("andibdhaiahdia")

