saldo_inicial = 50000

while True:

    print("====Menú Cajero Automatico====\n")
    print("1. Ver Saldo")
    print("2. Girar Dinero")
    print("3. Inversión")
    print("4. Salir\n")

    opcion_elegida = int(input("Elija una opción del menú"))

    if opcion_elegida == 1:
    
        print(f"\n\t Su saldo es: {saldo_inicial} \n")

    elif opcion_elegida == 2:
        while True:
            print("¿Cuanto desea girar?")
            monto_giro = int(input("Ingrese el monto"))
            if monto_giro <= saldo_inicial and monto_giro % 5000 == 0:
                print("\n===GIRO EXITOSO===\n")
                saldo_inicial = saldo_inicial - monto_giro
                print(f"Su saldo actual es {saldo_inicial}")

            elif monto_giro > saldo_inicial:
                print("\nSaldo insuficiente\n")
    
        
            else:
                print("\nMonto no aceptado. Debe ingresar multiplos de 5000.\n")

            print("\nQue desea hacer ahora?")
            print("\t1. Realizar otro giro.")
            print("\t2. Volver al menú")

            decisión = int(input("Elija una opción"))
            if decisión == 2:
                break
    elif opcion_elegida == 3:
        while True:
            print("¿Cuánto desea invertir?")        
            dinero_invertido = int(input("Ingrese el monto que desea invertir"))
            if dinero_invertido <= saldo_inicial:
                print("Estamos invirtiendo su dinero")
                print("\n ===== INVERSIÓN EXITOSA=======|\n")
                
                saldo_inicial = saldo_inicial +(dinero_invertido*2)

                print("***Su dinero invertido se ha DUPLICADO, revise su saldo para verificar***.\n")
            else:
                print("\n====SALDO INSUFICIENTE====\n")
            print("***¿Qué desea hacer?***")
            print("1. Ingresar otro monto")
            print("2. Volver al menú principal")
            decisión_inversión = int(input("\n\tElija una opción"))

            if decisión_inversión == 2:
                break

            
    elif opcion_elegida == 4:
        print("\t====CAJERO APAGADO=====")
        break
    else: 
        print("\n=====OPCIÓN NO VALIDA=====\n")