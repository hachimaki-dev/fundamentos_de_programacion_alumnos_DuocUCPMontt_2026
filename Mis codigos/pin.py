saldo = 50000
pin_correcto = "1234"
intentos = 0
acceso = False

while intentos < 3:
    pin = input("Ingrese su PIN: ")
    
    if pin == pin_correcto:
        acceso = True
        break
    else:
        intentos += 1
        print("PIN incorrecto.\n")

if not acceso:
    print("Tarjeta bloqueada por seguridad.")
else:
    print("\nAcceso concedido.")

    monto = int(input("¿Cuánto dinero desea retirar?: "))

    if monto > saldo:
        print("Fondos insuficientes.")
    elif monto == 0:
        print("Monto inválido.")
    else:
        saldo -= monto
        print(f"Retiro exitoso. Su nuevo saldo es: ${saldo}")