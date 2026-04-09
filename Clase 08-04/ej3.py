"""
3. Simulación de Banco Virtual (Ciclos IF Anidados)
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
"""
Saldo = 50000
opcion = 0
while opcion != 4:
    opcion = int(input("""Menú:
1) Ver Saldo
2) Girar Dinero
3) Inversión
4) Salir 
"""))
    if opcion == 1:
        print(f"Saldo actual: ${Saldo}")
    elif opcion == 2:
        Giro = int(input("Por cuanto quieres girar?"))
        if Giro % 5000 == 0 and Giro <= Saldo and Giro > 0:
            print(f"Hiciste un giro por ${Giro}")
            Saldo = Saldo - Giro
        elif Giro >= Saldo:
            print("Saldo insuficiente")
        elif Giro <= 0:
            print("Giro no valido")  
        elif Giro % 5000 != 0:
            print("Giro no valido")
    elif opcion == 3:
        inversion = int(input("Cuantos quieres invertir?"))
        if inversion <= Saldo and inversion > 0:
            Saldo = Saldo + inversion * 2
            print(f"Felicidades tu inversion se convirtio en ${inversion * 2} extra")
        else:
            print("Saldo insuficiente")
    elif opcion == 4:
        break
    else:
        print("Opción inválida")
print("Cajero apagado")