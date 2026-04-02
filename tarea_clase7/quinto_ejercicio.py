saldo_banco = 77700
pin_secreto = 7777
intentos_pin = 3

print("Bienvenido al cajero automatico")
print(f"Usted tiene {intentos_pin} para acceder a su cuenta\nO de lo contario su tarjeta sera bloqueada.")

while True:
    try:
        respuesta = int(input("Ingrese la clave de su tarjeta: "))
        if respuesta == pin_secreto:
            print("Clave correcta, Puede proseguir.")
            break
        else:
            intentos_pin -= 1
            print(f"Vuelva a intentarlo, tiene {intentos_pin} oportunidades más.")
            if intentos_pin == 0:
                print("Has fallado todos los intentos")
                print("Tu tarjeta ha sido bloqueada.")
                break
    except ValueError:
        print("Ingresa SOLAMENTE números.")
        intentos_pin -= 1
        print(f"Te quedan {intentos_pin} oportunidades más.")
        if intentos_pin == 0:
            print("Has fallado todos los intentos")
            print("Tu tarjeta ha sido bloqueada.")

while intentos_pin > 0:
    try:
        eleccion = int(input("Que desea realizar?\n1. Retirar dinero\n2. Depositar dinero\n3. Salir\nIngrese su elección: "))
        if eleccion == 1:
            print(f"Has seleccionado la opción {eleccion}")
            monto = int(input("Ingrese el monto a retirar: "))
            if monto <= 0:
                print("Monto invalido")
            elif monto > saldo_banco:
                print(f"Saldo insuficiente, solo tienes {saldo_banco}$")
            else:
                saldo_banco -= monto
                print(f"Operación realizada con exito, te quedan {saldo_banco} pesos.")
        elif eleccion == 2:
            print(f"Has seleccionado la opción {eleccion}")
            monto = int(input("Ingrese el monto a depositar: "))
            if monto <= 0:
                print("Monto invalido")
            else:
                saldo_banco += monto
                print(f"Operación realizada con exito, tienes en la cuenta de banco un saldo de {saldo_banco}$ pesos.")
        elif eleccion == 3:
            print("Entendido, en breves se apagara el sistema.")
            break
        else:
            print("Opción invalida")
    except ValueError:
         print("Opción invalida, solo puedes ingresar números.")

print("Apagando sistema....")

