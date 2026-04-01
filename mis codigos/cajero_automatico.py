saldo = 50000
pin_correcto = 1234
intentos = 0

while intentos < 3:
    pin = int(input("Ingrese su PIN: "))
    if pin == pin_correcto:
        print("PIN correcto")
        break
    else:
        intentos += 1
        print(f"PIN incorrecto! Intento {intentos}/3")
if intentos == 3 and pin != pin_correcto:
    print("Tarjeta bloqueada por seguridad")
else:
    retiro = int(input("Cuanto dinero desea retirar: "))
    if retiro > saldo:
        print("Fondo insuficiente")
    elif retiro == 0:
        print("Monto invalido")
    else:
        saldo -= retiro
        print(f"Retiro exitoso. Su nuevo saldo es: ${saldo}")