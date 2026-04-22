import getpass
pin= 3412
intentos= 0
maximo_intentos= 3

berlin= 1500
brazo_reina= 2000
queque= 1000
pie_limon= 1500
metodo_pago= ""

total= 0
print("BIENVENIDO A LA PASTELERIA")
print("Opciones")
print("1. Berlines/2. Brazo reina/3. Queque/4. Pie limon/5. Salir")

while True:
    eleccion= input("Que desea llevar? (1/2/3/4): ")
    if eleccion == "1":
        print(f"De acuerdo, su total es de {berlin}")
        total= total + berlin
        seguir_comprando= input("desea comprar algo mas? (SI/NO): ").lower()
        if seguir_comprando == "si":
            continue
        elif seguir_comprando == "no":
            print(f"el total es de {total}")
            metodo_pago= input("Como desea cancelar? (Efectivo/Tarjeta): ").lower()
            if metodo_pago == "tarjeta":
                print("Ingrese o acerque su tarjeta")
                while intentos < maximo_intentos:
                    pin_ingresado= int(getpass.getpass("Ingrese su PIN secreto: "))
                    if pin_ingresado != pin:
                        print("Te haz equivocado, intenta de nuevo")
                        intentos += 1
                        continue
                    elif pin_ingresado == pin:
                        print("Se ha completado la transaccion!")
                        break
                    else:
                        print("Ingrese algo valido")
                        continue
            break
    elif eleccion == "2":
        print(f"De acuerdo, su total es de {brazo_reina}")
        total= total + brazo_reina
        seguir_comprando= input("desea comprar algo mas? (SI/NO): ").lower()
        if seguir_comprando == "si":
            continue
        elif seguir_comprando == "no":
            metodo_pago= input("Como desea cancelar? (Efectivo/Tarjeta): ").lower() 
            if metodo_pago == "tarjeta":
                print("Ingrese o acerque su tarjeta")
                while intentos < maximo_intentos:
                    pin_ingresado= int(getpass.getpass("Ingrese su PIN secreto: "))
                    if pin_ingresado != pin:
                        print("Te haz equivocado, intenta de nuevo")
                        intentos += 1
                        continue
                    elif pin_ingresado == pin:
                        print("Se ha completado la transaccion!")
                        break
                    else:
                        print("Ingrese algo valido")
                        continue
            break
    elif eleccion == "3":
        print(f"De acuerdo, su total es de {queque}")
        total= total + queque
        seguir_comprando= input("desea comprar algo mas? (SI/NO): ").lower()
        if seguir_comprando == "si":
            continue
        elif seguir_comprando == "no":
            metodo_pago= input("Como desea cancelar? (Efectivo/Tarjeta): ").lower()
            if metodo_pago == "tarjeta":
                print("Ingrese o acerque su tarjeta")
                while intentos < maximo_intentos:
                    pin_ingresado= int(getpass.getpass("Ingrese su PIN secreto: "))
                    if pin_ingresado != pin:
                        print("Te haz equivocado, intenta de nuevo")
                        intentos += 1
                        continue
                    elif pin_ingresado == pin:
                        print("Se ha completado la transaccion!")
                        break
                    else:
                        print("Ingrese algo valido")
                        continue           
            elif metodo_pago == "efectivo":
                dinero_ingresado= int(input("Ingresa efectivo (1000/2000/5000): "))
                while dinero_ingresado > total:
                    if dinero_ingresado == 1000:
                        

            
            break

    elif eleccion == "4":
        print(f"De acuerdo, su total es de {pie_limon}")
        total= total + pie_limon
        seguir_comprando= input("desea comprar algo mas? (SI/NO): ").lower()
        if seguir_comprando == "si":
            continue
        elif seguir_comprando == "no":
            metodo_pago= input("Como desea cancelar? (Efectivo/Tarjeta): ").lower()
            print("Ingrese o acerque su tarjeta")
            while intentos < maximo_intentos:
                pin_ingresado= int(getpass.getpass("Ingrese su PIN secreto: "))
                if pin_ingresado != pin:
                    print("Te haz equivocado, intenta de nuevo")
                    intentos += 1
                    continue
                elif pin_ingresado == pin:
                    print("Se ha completado la transaccion!")
                    break
                else:
                    print("Ingrese algo valido")
                    continue
        else:
            print("Ingrese algo valido")
            continue
        break
    elif eleccion == "5":
        print("Muchas gracias")
    else:
        print("Ingresa una opcion valida!")
        continue