saldo = 50000
pin = "1234"
intentos = 0
permitir_intentos = True

while permitir_intentos:
    pin_ingresado = input("Ingresa tu contraseña: ")

    # Pin correcto
    if pin_ingresado == pin:
        menu_retiro = True
        while menu_retiro:
            print("\n¿Qué acción desea realizar?\n1. Retirar dinero    2. Consultar saldo    3. Salir")
            eleccion_usuario = int(input("Elección: "))

            if eleccion_usuario == 1:
                monto_a_retirar = int(input("\nIngrese el monto que desea retirar. $"))
                if monto_a_retirar > saldo:
                    print("Saldo insuficiente.")
                elif monto_a_retirar == 0:
                    print("Monto inválido.")
                else:
                    saldo = saldo - monto_a_retirar
                    print(f"\nRetiro exitoso. Su nuevo saldo es ${saldo}")
            elif eleccion_usuario == 2:
                print(f"\nSaldo actual: ${saldo}")
            elif eleccion_usuario == 3:
                permitir_intentos = False # Asegurarse de que no vuelva al ciclo de pedir contraseña
                break
            else:
                print("Elección inválida.")

    # Pin incorrecto
    else:
        print("¡Contraseña incorrecta!")
        intentos += 1

    if intentos >= 3:
        print("Tarjeta bloqueada por seguridad.")
        permitir_intentos = False
