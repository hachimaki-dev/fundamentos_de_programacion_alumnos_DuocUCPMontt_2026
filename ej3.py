saldo_inicial = 50000

opcion_elegida = 0

print("Hola, este es el menú de operaciones")
print("1. Ver Saldo")
print("2. Girar Saldo")
print("3. Inversión")
print("4. Salir")


while opcion_elegida != 4:
    opcion_elegida = int(input("Qué operación desea realizar en el cajero? "))

    if opcion_elegida == 1:
        print(f"Su saldo es de: {saldo_inicial}")

    elif opcion_elegida == 2:
        monto_girado = int(input(f"Cuánto deseas girar: "))

        if monto_girado <= saldo_inicial and monto_girado % 5000 == 0:
            saldo_inicial = saldo_inicial - monto_girado
        elif monto_girado > saldo_inicial or monto_girado % 5000 != 1:
            print("Monto no aceptado.")
            

    elif opcion_elegida == 3:
        monto_a_invertir = int(input("Cuánto desea invertir? "))

        if monto_a_invertir <= saldo_inicial:
            saldo_inicial = saldo_inicial * 2
            print(f"Gracias a su inversión, su saldo se le ha duplicado!")

        elif monto_a_invertir > saldo_inicial:
            print("Saldo insuficiente.")

    
    if opcion_elegida == 4:
        print("Cajero apagado")