saldo = 50000

while True:
    print("\n1) Ver saldo")
    print("2) Girar dinero")
    print("3) Inversión")
    print("4) Salir")

    opcion_escogida = int(input("\nIngrese su opción: "))

    match opcion_escogida:
        case 1:
            print(f"Su saldo es: ${saldo}")
            continue
        case 2:
            cant_giro = int(input("¿Cuanto quiere girar?: $"))

            if cant_giro > saldo:
                print("Saldo insuficiente")
                continue
            elif cant_giro % 5000 != 0:
                print("Monto no aceptado, debe ser múltiplo de $5000")
                continue
            elif cant_giro < 1:
                print("La cantidad del giro debe ser mayor a $0")
            else:
                print("Giro realziado con éxito")
                saldo -= cant_giro
        case 3:
            cant_inversion = int(input("Ingrese la cantidad de dinero a invertir: $"))

            if cant_inversion > saldo:
                print("Saldo insuficiente")
                continue
            elif cant_inversion < 1:
                print("El dinero a invertir debe ser mayor a $0")
                continue
            else:
                saldo *= 2
        case 4:
            print("Cajero apagado")
            break
        case _:
            print("Opción inválida")
            continue