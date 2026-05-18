saldo = 50000

limite_diario = 200000

# monto_retiro = 60000

while True:

    monto_retiro = int(input("Ingrese el monto que desea retirar: "))

    if monto_retiro > limite_diario:
        print("¡Excede limite diario!")
        break

    elif monto_retiro > saldo:

        print("¡Saldo Insuficiente!")
        break

    elif monto_retiro % 5000 != 0:
        print("¡El monto de retiro debe ser múltiplo de 5000!")
        print("El cajero no dispensa monedas")
        print("Por favor, ingresa un monto válido.")

    else:
        saldo -= monto_retiro
        print(f"¡Retiro exitoso! Tu nuevo saldo es: ${saldo}")
        break