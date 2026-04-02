import sys

saldo_user = 50000
monto_retirar = 0
pin_user = "1020"
pin_ingresado = ""

intento = 0
intentos_totales = 3

while intento < intentos_totales:
    pin_ingresado = input("Ingrese su PIN: ")
    if intento + 1 == intentos_totales:
        print("Tarjeta bloqueada por seguridad")
        sys.exit()

    if pin_ingresado == pin_user:
        break
    else:
        print(f"PIN Incorrecto, intentos restantes: {intentos_totales-(intento+1)}")
        intento += 1

monto_retirar = int(input("¿Cuanto dinero quiere retirar?: $"))

if monto_retirar > saldo_user:
    print("Fondos insuficientes")
elif monto_retirar <= 0:
    print("Monto inválido")
else:
    saldo_user -= monto_retirar
    print(f"Retiro exitoso, su nuevo saldo es: ${saldo_user}")