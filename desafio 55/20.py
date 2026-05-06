saldo = 50000
limite_diario = 200000
monto_a_retirar = 60000



print("-----Bienvenido a TU Banco-----")
print("Elige una opcion:")
print("1. Consultar saldo.")
print("2. Retirar dinero.")
print("3. Salir del banco.")

opcion = int(input("Ingrese su opcion:"))

while opcion != 3:

    if opcion == 1:
        print(f"Su saldo es: {saldo}.")

        break

    elif opcion == 2:
        retirar = int(input("Cuanto desea retirar?"))

        if retirar >= 60000:
            print("Te excediste, no tienes ese monto en tu cuenta bancaria, ingresa un monto de retiro valido.")


        elif retirar <=60000:
            print(f"Retiraste {retirar} de tu cuenta bancaria.")

            break
