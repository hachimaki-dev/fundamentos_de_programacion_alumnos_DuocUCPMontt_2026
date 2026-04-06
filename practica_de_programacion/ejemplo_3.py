# Se requiere programar el menú de un cajero automático muy rudimentario. Tienes un saldo inicial de $50000. El cajero muestra un menú y operará repetidamente hasta que se elija 'Salir'.

"""
Menú:
1) Ver Saldo
2) Girar Dinero
3) Inversión
4) Salir

- Si elige 1: Muestra el saldo actual.
- Si elige 2: Pregunta cuánto girar. A su vez, debes verificar que el monto solicitado sea menor o igual al saldo, y que sea múltiplo de 5000. Si cumple esto, realiza el giro (resta el saldo); si no, muestra el motivo del error ('Saldo insuficiente' o 'Monto no aceptado').
- Si elige 3: Te ofrece invertir tu dinero. Te solicita una cantidad. Si esa cantidad es menor que o igual a tu saldo, te la duplica y la añade al saldo final de retorno, sino, muestra 'Saldo insuficiente'.
- Si elige 4: Termina el programa imprimiendo "Cajero apagado".
- Cualquier otra opción muestra 'Opción inválida'.

"""

saldo_total = 50000
ciclo_de_cajero = True

while ciclo_de_cajero == True:
    print("= M E N U =")
    print("1) Ver Saldo")
    print("2) Girar Dinero")
    print("3) Inversion")
    print("4) Salir")
    try:
        seleccion = int(input("[]: "))
        if seleccion == 1:
            print(f"${saldo_total}")
        if seleccion == 2:
            giro_total = int(input("Cuanto desea girar? (Solo multiplos de $5000!): "))
            if giro_total > saldo_total:
                print("Saldo insuficiente")
            if giro_total % 5000 == 0:
                saldo_total -= giro_total
                print("Giro exitoso!")
            elif giro_total % 5000 != 0:
                print("Monto invalido!")
        if seleccion == 3:
            cantidad_a_invertir = int(input("Ingrese la cantidad que desea invertir: "))
            if cantidad_a_invertir <= saldo_total:
                saldo_total += cantidad_a_invertir * 2
            else:
                print("Saldo insuficiente")
        if seleccion == 4:
            print("Cajero apagado")
            break                
    except:
        print("Opcion invalida")