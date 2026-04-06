# 3. Simulación de Banco Virtual (Ciclos IF Anidados)
# Se requiere programar el menú de un cajero automático muy rudimentario. Tienes un saldo inicial de $50000. El cajero muestra un menú y operará repetidamente hasta que se elija 'Salir'.

# Menú:
# 1) Ver Saldo
# 2) Girar Dinero
# 3) Inversión
# 4) Salir

# El comportamiento debe ser el siguiente:
# - Si elige 1: Muestra el saldo actual.
# - Si elige 2: Pregunta cuánto girar. A su vez, debes verificar que el monto solicitado sea menor o igual al saldo, y que sea múltiplo de 5000. Si cumple esto, realiza el giro (resta el saldo); si no, muestra el motivo del error ('Saldo insuficiente' o 'Monto no aceptado').
# - Si elige 3: Te ofrece invertir tu dinero. Te solicita una cantidad. Si esa cantidad es menor que o igual a tu saldo, te la duplica y la añade al saldo final de retorno, sino, muestra 'Saldo insuficiente'.
# - Si elige 4: Termina el programa imprimiendo "Cajero apagado".
# - Cualquier otra opción muestra 'Opción inválida'.

# Usa while y condicionales anidados (if dentro de if equivalentes) para este desafío.

saldo = 5000

while True:
    opcion_usuario = int(input("\n" \
    "Menú:\n" \
    "1) Ver Saldo\n" \
    "2) Girar Dinero\n" \
    "3) Inversión\n" \
    "4) Salir\n" \
    "Eliga una opción: "))

    if opcion_usuario == 1:
        print(" ")
        print(f"Saldo actual es: ${saldo}")
        print(" ")
        realizar_operacion = int(input("Desea realizar otra operación     1) SI   |   2) NO     :"))
        if realizar_operacion == 2:
            break

    if opcion_usuario == 2:
        girar_dinero = int(input("Monto a retirar: $"))
        if girar_dinero > saldo:
            print(" ")
            print("Saldo insuficiente")
            print(" ")
            realizar_operacion = int(input("Desea realizar otra operación     1) SI   |   2) NO     :"))
            if realizar_operacion == 2:
                break
        elif girar_dinero <= saldo:
            saldo -= girar_dinero
            print(" ")
            print(f"Usted a retirado ${girar_dinero}")
            print(f"Su nuevo saldo es ${saldo}")
            print(" ")
            realizar_operacion = int(input("Desea realizar otra operación     1) SI   |   2) NO     :"))
            if realizar_operacion == 2:
                break

    if opcion_usuario == 3:
        opcion_invertir = int(input("¿Desea invertir su dinero?    1) SI   |   2) NO     :"))
        if opcion_invertir == 1:
            monto_inversion = int(input("Ingrese el monto a invertir: $"))
            if monto_inversion > saldo:
                print("")
                print("Saldo insuficiente")
                print(" ")
                realizar_operacion = int(input("Desea realizar otra operación     1) SI   |   2) NO     :"))
                if realizar_operacion == 2:
                    break

            elif monto_inversion <= saldo:
                print(" ")
                print(f"Su monto de ${monto_inversion} esta invertido")
                saldo += (monto_inversion * 2)
                print(" ")
                print(f"Su inversion se a duplicado ahora su nuevo saldo es ${saldo}")
                realizar_operacion = int(input("Desea realizar otra operación     1) SI   |   2) NO     :"))
                if realizar_operacion == 2:
                    break
    if opcion_usuario == 4:
        print("")
        print("Cajero apagado")
        print("")
        break
    
    else:
        print("")
        print("Opción no vailda")

