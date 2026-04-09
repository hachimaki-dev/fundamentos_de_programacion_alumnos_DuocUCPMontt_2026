import getpass
saldo= 50000
numero_maximo_intentos= 3
intentos= 0
PIN_correcto= 3412
print("=========BIENVENIDO A TU BANCO VIRTUAL=======")
while intentos < numero_maximo_intentos:
    PIN_ingresado= int(getpass.getpass("Ingresa tu PIN secreto: "))
    if PIN_ingresado == PIN_correcto:
        while True:
            print("HAZ ACCEDIDO")
            print("\n>>>>>>>>MENU<<<<<<<<")
            print("1.- VER SALDO")
            print("2.- GIRAR DINERO")
            print("3.- INVERTIR")
            print("4.- SALIR")
            operacion_elegida= input("ELIGE TU OPERACION: ").lower()
            if operacion_elegida == "ver saldo":
                print(f"TU SALDO ES DE {saldo}")
                otra_operacion= input("DESEA REALIZAR OTRA OPERACION? (SI/NO): ").lower()
                if otra_operacion == "no":
                    print("HASTA LUEGO")
                    break
                else:
                    continue
            elif operacion_elegida == "girar dinero":
                monto_a_retirar= int(input("Ingrese monto a retirar: "))
                if monto_a_retirar > saldo:
                    print("GIRO INVALIDO, SALDO INSUFICIENTE")
                    break
                else:
                    saldo= saldo - monto_a_retirar
                    print(f"PERFECTO! TU NUEVO SALDO ES DE {saldo}")
                    otra_operacion= input("DESEA REALIZAR OTRA OPERACION? (SI/NO): ").lower()
                    if otra_operacion == "no":
                        break
                    else:
                        continue
            elif operacion_elegida == "invertir":
                dinero_invertido= int(input("CUANTO DINERO DESEA INVERTIR? "))
                saldo= saldo - dinero_invertido
                if dinero_invertido >= saldo:
                    print("SALDO INSUFICIENTE")
                    otra_operacion= input("DESEA REALIZAR OTRA OPERACION? (SI/NO): ").lower()
                    if otra_operacion == "no":
                        break
                    else:
                        continue
                else:
                    print("FELICIDADES, TU INVERSION HA SIDO UN EXITO!")
                    saldo= saldo + dinero_invertido * 2
                    print(f"TU SALDO AHORA ES DE {saldo}")
                    otra_operacion= input("DESEA REALIZAR OTRA OPERACION? (SI/NO): ").lower()
                    if otra_operacion == "no":
                        break
                    else:
                        continue
            else:
                break
        break
    elif PIN_ingresado!= PIN_correcto:
        intentos += 1
        print("PIN INCORRECTO, INTENTA DE NUEVO")
    else:
        print("PIN INVALIDO")
    
print("FIN DEL PROGRAMA")