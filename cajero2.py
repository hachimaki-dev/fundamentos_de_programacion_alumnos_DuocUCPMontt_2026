""" Se requiere programar el menú de un cajero automático muy rudimentario. 
Tienes un saldo inicial de $50000. El cajero muestra un menú y 
operará repetidamente hasta que se elija 'Salir'.

Menú:
1) Ver Saldo
2) Girar Dinero
3) Inversión
4) Salir

El comportamiento debe ser el siguiente:
- Si elige 1: Muestra el saldo actual.

- Si elige 2: Pregunta cuánto girar. A su vez, debes verificar 
que el monto solicitado sea menor o igual al saldo, y que sea múltiplo de 5000. 
Si cumple esto, realiza el giro (resta el saldo); si no, 
muestra el motivo del error ('Saldo insuficiente' o 'Monto no aceptado').

- Si elige 3: Te ofrece invertir tu dinero. Te solicita una cantidad. 
Si esa cantidad es menor que o igual a tu saldo, te la duplica y 
la añade al saldo final de retorno, sino, muestra 'Saldo insuficiente'.

- Si elige 4: Termina el programa imprimiendo "Cajero apagado".

- Cualquier otra opción muestra 'Opción inválida'.

Usa while y condicionales anidados (if dentro de if equivalentes) para este desafío."""
saldo = 50000

while True:
    menu = int(input("menu 1.ver saldo 2.girar dinero 3.inversion 4.salir"))
    if menu == 1:
        print(f"tu saldo es: {saldo}")

    elif menu == 2:
        giro = int(input("cuanto desea girar ?: "))
        if giro <= saldo and giro >= 0:
            saldo = saldo - giro
        else:
            print("saldo insuficiente")

    elif menu == 3:
        invercion = int(input("cuanto desea invertir?: "))
        if invercion <= saldo:
            saldo = saldo + (invercion * 2)
            print(f"tu retorno es: {invercion*2}")
        else:
            print("saldo insuficiente")
    
    elif menu == 4:
        print("cajero apagado")
        break

    else:
        print("opcion no valida")    

