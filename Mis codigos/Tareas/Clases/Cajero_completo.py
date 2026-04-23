saldo = 50000
intentos_fallidos = 0
pin = 1604
numero_maximo_intentos = 3
contador_intentos_fallidos = 0

print("****BIENVENIDOS A BANCO ESTADO****")

while True:
    pin_ingresado = int(input("Por favor, ingrese su clave secretita"))

    if pin_ingresado == pin :
        print("Haz accedido")
        while pin_ingresado == pin:
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
        
                while retiro > saldo:
                    retiro = int(input(f"Error. Recuerde que su saldo es de {saldo}\n"))
       
                if retiro <= saldo:
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
                    saldo = saldo - inversion
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
                    break
       
                elif otra_operacion == "si":
                    print()

            elif opcion_escogida == 4:
                print("Cajero apagado")
                break
        
    elif pin_ingresado != pin :
        contador_intentos_fallidos = contador_intentos_fallidos + 1
        print("No haz accedido")
    else:
        print("Ingrese una contraseña vàlida")
    if contador_intentos_fallidos >= 3:
        break