saldo = 50000
PIN = 6547
intentos = 0
max_intentos = 3
acceso_concedido = False

print("/////////////////////////////BIENVENIDO AL CAJERO PYTHON/////////////////////////////")

while intentos < max_intentos:
    intento = int(input(f"Intento {intentos + 1}/{max_intentos} Ingrese su PIN de 4 digitos: "))
    intentos += 1

    if intento == PIN:
        print("Has ingresado correctamente")
        print("/////////////////////////////BIENVENIDO AL MEU DE RETIRO/////////////////////////////")
        acceso_concedido = True
        break

    else:
        if intentos < max_intentos:
            print("¡PIN incorrecto! Intente de nuevo.")

if not acceso_concedido:
    print("!!!!!! Tarjeta bloqueada por seguridad !!!!!!")
else:
    retiro = int(input("¿Cuanto dinero desea retirar?: $"))

    if retiro == 0:
        print("Monto invalido")
        
    elif retiro > saldo:
        print("Fondos insuficientes")
    
    else:
        saldo -= retiro
        print(f"Retiro exitoso. Su nuevo saldo es: ${saldo}") 