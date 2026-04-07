'''
Se requiere programar el menú de un cajero automático muy rudimentario. Tienes un saldo inicial de $50000. El cajero muestra un menú y operará repetidamente hasta que se elija 'Salir'.

Menú:
1) Ver Saldo
2) Girar Dinero
3) Inversión
4) Salir

El comportamiento debe ser el siguiente:
- Si elige 1: Muestra el saldo actual.
- Si elige 2: Pregunta cuánto girar. A su vez, debes verificar que el monto solicitado sea menor o igual al saldo, y que sea múltiplo de 5000. Si cumple esto, realiza el giro (resta el saldo); si no, muestra el motivo del error ('Saldo insuficiente' o 'Monto no aceptado').
- Si elige 3: Te ofrece invertir tu dinero. Te solicita una cantidad. Si esa cantidad es menor que o igual a tu saldo, te la duplica y la añade al saldo final de retorno, sino, muestra 'Saldo insuficiente'.
- Si elige 4: Termina el programa imprimiendo "Cajero apagado".
- Cualquier otra opción muestra 'Opción inválida'.

Usa while y condicionales anidados (if dentro de if equivalentes) para este desafío.
'''

SALDO_INICIAL = 50000
saldo_actual = SALDO_INICIAL

while True :
    print("")
    print("1) Ver Saldo")
    print("2) Girar Dinero")
    print("3) Inversión")
    print("4) Salir")

    opcion = int (input("Seleccione una opción: "))

    match opcion :
        case 1 :
            print(f"Saldo actual: {saldo_actual}")
        case 2 :
            monto_giro = int (input("¿Cuánto quiere girar? "))

            if monto_giro > saldo_actual :
                print("Saldo insuficiente.")
            elif monto_giro % 5000 != 0 :
                print("Monto de giro no aceptado.")
            else :
                print("Giro realizado.")
                saldo_actual -= monto_giro
        case 3 :
            monto_inversion = int (input("Ingrese la cantidad a invertir: "))

            if monto_inversion <= saldo_actual :
                saldo_actual += monto_inversion * 2
                print(f"Saldo total tras la inversión: {saldo_actual}")
            else :
                print("Saldo insuficiente.")
        case 4 :
            print("Cajero apagado.")
            break
        case _ :
            print("Opción inválida.")