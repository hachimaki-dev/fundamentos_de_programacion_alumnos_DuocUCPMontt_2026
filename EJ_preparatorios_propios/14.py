caja = 0

print("==="*12)
print("SISTEMA DE CAJA CAFETERIA CAMPUS")
print("==="*12)


while True:
    print("1. Ver saldo en Caja \n2. Registrar venta \n3. Registrar Gastos \n4. Salir")
    print()

    try:
        opcion_elegida = int(input("Ingrese que opcion desea realizar :  "))
        
        if opcion_elegida == 4:
            print(f"Cierre de caja : ${caja} . Hasta mañana")
            break
        elif opcion_elegida == 1:
            print(f"El saldo de la caja es ${caja}")
        elif opcion_elegida == 2:
            print()
            while True:
                try:
                    registrar_venta = int(input("Ingrese su monto a registrar :  "))
                    if registrar_venta < 0:
                        print("El numero ingresado debe ser un entero positivo")
                        continue
                    else:
                        caja += registrar_venta
                        print(f"Saldo de la caja : {caja}")
                        break
                except ValueError:
                    print("ingrese una opcion valida ")
                    continue
        elif opcion_elegida == 3:
            print()
            while True:
                try:
                    registrar_gasto = int(input("Ingrese el monto que desea gastar :   "))
                    if registrar_gasto < 0:
                        print("El numero ingresado debe ser un entero positivo")
                        continue
                    elif registrar_gasto > caja:
                        print("Lo ingresado debe de ser menor de lo que hay en la caja")
                        continue
                    else:
                        caja -= registrar_gasto
                        print(f"Saldo de la caja : {caja}")
                        break
                except ValueError:
                    print("ingrese una opcion valida")
                    continue
    except ValueError:
        print("Ingrese una opcion valida")
        continue