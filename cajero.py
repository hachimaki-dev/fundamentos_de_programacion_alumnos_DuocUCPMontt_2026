saldo = 50000
PIN = 1234
intentos = 0
max_intentos = 3

while intentos < max_intentos:
    intento = int(input(f"Intento {intentos + 1}/{max_intentos} Ingrese su PIN de 4 digitos: "))
    intentos += 1

    if intento != PIN:
        print("Tarjeta bloqueada por seguridad")

else:
    print("Ha ingresado correctamente")
    
    print("BIENVENIDO AL MENU DE RETIRO")
    print("***¿Cuanto desea retirar?***")
    print("")

    if  > saldo