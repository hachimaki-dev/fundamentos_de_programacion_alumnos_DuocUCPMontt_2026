import getpass
PIN_correcto= 3412
numero_maximo_intentos= 3

import random
numero_secreto= random.randint(1,100)
intentos= 0

print(">>>>>>>HOLA SOY BRAIAN, TU ASISTENTE VIRTUAL<<<<<<<<")
print("\nMENU")
print("1. Calculadora")
print("2. Juego N* aleatorio")
print("3. Tomar mate")
print("4. Banca Virtual")
print("5. Musica")
print("6. Bombardear")
print("7. Salir")

while True:
    eleccion_usuario= int(input("Que quieres hacer el dia de hoy? (1/2/3/4/5/6/7): "))
    while True:
        if eleccion_usuario == 1:
            print("Haz elegido la calculadora!")
            numero1= float(input("Ingresa el primer numero: "))
            numero2= float(input("Ingresa el segundo numero: "))

            operacion= input("Elige la operacion deseada (+, -, *, /): ")
            if operacion == "+":
                resultado= numero1 + numero2
                print(f"El resultado es: {resultado}")
                continuar= input("Deseas seguir utilizando la calculadora? (si/no): ").lower()
                if continuar == "si":
                    continue
                elif continuar == "no":
                    break
                else:
                    print("Ingresa algo valido")
                    break
            elif operacion == "-":
                resultado= numero1 - numero2
                print(f"El resultado es: {resultado}")
                continuar= input("Deseas seguir utilizando la calculadora? (si/no): ").lower()
                if continuar == "si":
                    continue
                elif continuar == "no":
                    break
                else:
                    print("Ingresa algo valido")
                    break
            elif operacion == "*":
                resultado= numero1 * numero2
                print(f"El resultado es: {resultado}")
                continuar= input("Deseas seguir utilizando la calculadora? (si/no): ").lower()
                if continuar == "si":
                    continue
                elif continuar == "no":
                    break
                else:
                    print("Ingresa algo valido")
                    break
            elif operacion == "/":
                resultado= numero1 - numero2
                print(f"El resultado es: {resultado}")
                continuar= input("Deseas seguir utilizando la calculadora? (si/no): ").lower()
                if continuar == "si":
                    continue
                elif continuar == "no":
                    break
                else:
                    print("Ingresa algo valido")
                    break
            else:
                print("Ingresa algo valido!")
                break
        elif eleccion_usuario == 2:
            print("Bienvenido a adivina el numero secreto!")
            while True:
                numero_ingresado= int(input("Ingresa el numero"))
                if numero_ingresado == numero_secreto:
                    print("Adivinaste!, Felicidades!")
                    break
                elif numero_ingresado < numero_secreto:
                    print("Lo siento, no adivinaste")
                    print("El numero secreto es mas alto")
                    continue
                elif numero_ingresado > numero_secreto:
                    print("Lo siento, no adivinaste")
                    print("El numero secreto es más bajo")
                    continue                
                else:
                    print("Ingresa algo valido")
                    break
        elif eleccion_usuario == 3:
            print("Hagamos una pausa y tomemos MATE")
            print("\nMenu")
            print("1. Tipo de mate")
            print("2. Yerba mate")
            print("3. Disfrutar")
            
            while True:
                eleccion= int(input("Que elegimos primero? (1/2/3): "))
                if eleccion == 1:
                    print("Tenemos varios tipos de mate:")
                    print("\nImperial")
                    print("Torpedo")
                    print("Camionero")
                    print("Calabaza")
                    mate_elegido= input("Elige un mate: ").lower()
                    continue
                elif eleccion == 2:
                    print("Elige tu Yerba preferida")
                    print("\nCanarias")
                    print("Baldo")
                    print("Mañanitas")
                    print("Playadito")
                    print("Pipore")
                    print("Taragui")
                    Yerba_elegida= input("Elige tu Yerba: ")
                elif eleccion == 3:
                    print(f"Ahora disfruta de un buena Yerba {Yerba_elegida} en tu precioso mate {mate_elegido}")
                    input("Cuando estes listo presiona cualquier tecla para volver: ")
                    break
                
        elif eleccion_usuario == 4:
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
