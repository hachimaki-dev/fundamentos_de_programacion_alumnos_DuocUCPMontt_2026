saldo = 50000
PIN = 1334
contador_de_intentos_fallidos = 0

print("=== BIENVENIDOS A BANCO ESTADO ===")
print("=== Es el mejor Banco del País ===")

while True:

    pin_secreto = int(input("Por favor ingrese su clave secreta: "))

    if pin_secreto == PIN:
        print("Haz Accedido")
        break

    else:
        print("No hay acceso")
        contador_de_intentos_fallidos = contador_de_intentos_fallidos + 1

    if contador_de_intentos_fallidos >= 3:
        break

if contador_de_intentos_fallidos >= 3:
    print("Tarjeta bloqueada por seguridad")