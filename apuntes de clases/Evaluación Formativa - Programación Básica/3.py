saldo = 50000

print("****** Cajero Automatico *******")

while True:
    print("M E N U :")
    print("1) Ver Saldo ")
    print("2) Girar Dinero")
    print("3) Inversion ")
    print("4) Salir ")
    opcion_elegida = int(input("Que opcion desea ejecutar (1/2/3/4):   "))
    if opcion_elegida == 1:
        print(f"Su Saldo es ${saldo}")
    elif opcion_elegida == 2:
        girar_dinero = int(input("¿Cuanto dinero desea girar?:  "))
        if girar_dinero <= saldo and girar_dinero % 5000 == 0:
            saldo -= girar_dinero
            print(f"Giro exitoso. Nuevo saldo: ${saldo}")
        else:
            print("Saldo insuficiente o Monto no aceptado")
    elif opcion_elegida == 3:
        invertir = int(input("Cuanto Dinero Desea Invertir:  "))
        if invertir <= saldo:
            ganancia = invertir * 2
            saldo += ganancia
            print(f"Inversión realizada. Nuevo saldo: ${saldo}")
        else:
            print("Saldo insuficiente")
    elif opcion_elegida == 4:
        print("Cajero apagado")
        break
    else:
        print("Opción inválida")
        