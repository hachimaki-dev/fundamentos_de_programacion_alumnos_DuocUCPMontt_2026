# 3. Simulación de Banco Virtual (Ciclos IF Anidados)
# Se requiere programar el menú de un cajero automático muy rudimentario. 
# Tienes un saldo inicial de $50000. El cajero muestra un menú y operará repetidamente hasta que se elija 'Salir'.

# Menú:
# 1) Ver Saldo
# 2) Girar Dinero
# 3) Inversión
# 4) Salir

# El comportamiento debe ser el siguiente:
# - Si elige 1: Muestra el saldo actual.
# - Si elige 2: Pregunta cuánto girar. A su vez, debes verificar que el monto solicitado sea menor o igual al saldo, y que sea múltiplo de 5000. 
#           Si cumple esto, realiza el giro (resta el saldo); si no, muestra el motivo del error ('Saldo insuficiente' o 'Monto no aceptado').
# - Si elige 3: Te ofrece invertir tu dinero. Te solicita una cantidad. Si esa cantidad es menor que o igual a tu saldo,
#           te la duplica y la añade al saldo final de retorno, sino, muestra 'Saldo insuficiente'.
# - Si elige 4: Termina el programa imprimiendo "Cajero apagado".
# - Cualquier otra opción muestra 'Opción inválida'.

# Usa while y condicionales anidados (if dentro de if equivalentes) para este desafío.

print(" BANCO VIRTUAL ".center(30, "-"))

saldo = 50000

while True:
    print("-----------------")
    print("      MENU \n1) Ver Saldo\n2) Girar Dinero\n3) Inversion\n4) Salir")
    print("-----------------")
    opcion_elegida = int(input("Ingrese su opción: "))
    
    if opcion_elegida == 1:
        print(f"Saldo actual: {saldo}")
    elif opcion_elegida == 2:
        monto_retiro = int(input("Monto a retirar: "))
        if monto_retiro%5000 == 0:
            if monto_retiro <= saldo:
                saldo -= monto_retiro
                print(f"Monto retirado: ${monto_retiro} | Saldo restante: ${saldo}")
            else:
                print("Saldo insuficiente")     
        else:
            print("Monto a retirar debe ser multiplo de 5")
    elif opcion_elegida == 3:
        # Si esa cantidad es menor que o igual a tu saldo,
        # te la duplica y la añade al saldo final de retorno
        print("Invierte tu dinero")
        monto_inversion = int(input("Monto a invertir: "))
        if monto_inversion <= saldo:
            saldo = saldo + monto_inversion*2 #??
            print(f"Nuevo saldo: ${saldo}")
        else:
            print("Saldo Insuficiente")
    elif opcion_elegida == 4:
        print("--------------")
        print("Cajero Apagado")
        print("--------------")
        break
    else:
        print("Opcion invalida")

