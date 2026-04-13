saldo = 50000

print("Hola, bienvenido a Banco Estado")


while True:
    opcion_escogida = int(input("¿Que operaciòn necesita realizar?\n(1)Ver saldo\n(2)Girar dinero\n(3)Inversiòn\n(4)Salir\n"))

    if opcion_escogida == 1:
        
        print(f"Su saldo es de {saldo}")
        
        otra_operacion = input("¿Desea realiar otra operaciòn?").lower()
        
        if otra_operacion == "no":
            print("Cajero cerrado")
            break
        elif otra_operacion == "si":
            print()
            continue
        while otra_operacion != "si" and otra_operacion != "no":
            otra_operacion = input("Opcion invàlida")
            

    elif opcion_escogida == 2:
        
        retiro = int(input("¿Cuanto dinero desea retirar?"))
        
        if retiro > saldo:
            print(f"Error. Recuerde que su saldo es de {saldo}")
       
        elif retiro <= saldo:
            saldo = saldo - retiro
            print(f"Dinero retirado {retiro}. Ahora su saldo es de {saldo}")
            otra_operacion = input("¿Desea realizar otra operaciòn?").lower()
           
            if otra_operacion == "no":
                print("Gracias por elegir Banco Estado")
                break
           
            elif otra_operacion == "si":
                print()
           
            while otra_operacion != "si" and otra_operacion != "no":
                otra_operacion = input("Opcion invàlida")

    elif opcion_escogida == 3:
        inversion = int(input("¿cuanto desea invertir?"))
        
        if inversion <= saldo:
            inversion = inversion * 2
            saldo = inversion + saldo
            print(f"Felicidades. Su sueldo actual es de {saldo}")
            otra_operacion = input("¿Desea realizar otra operaciòn?")
           
            if otra_operacion == "no":
                print("Gracias por elegir Banco Estado")
                break
       
            elif otra_operacion == "si":
                print()


        
        while inversion > saldo:
            inversion = input(f"Excede de tu presupuesto. Intente con una cantidad menor, recuerde que su saldo es de {saldo}")
        print(f"Felicidades. Su sueldo actual es de {saldo}")
        otra_operacion = input("¿Desea realizar otra operaciòn?").lower()
        
        if otra_operacion == "no":
            print("Gracias por elegir Banco Estado")
            exit()
       
        elif otra_operacion == "si":
            print()

    elif opcion_escogida == 4:
        print("Cajero apagado")
        break




            
    

    

