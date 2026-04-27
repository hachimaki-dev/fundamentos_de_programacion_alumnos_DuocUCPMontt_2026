import random
print("BIENVENIDO BALABET")
#Menú
opcion_usuario = 0
tomar_copete = 1
Ruleta = 2
Tragamonedas = 3
salir = 4
fichas = 100
multiplicador_bebida = 1.0
bebida_0 = 0
valor_Chela = 30
valor_Piscola = 50
valor_vodka = 110
valor_Blue = 200
Inventario = [fichas, bebida_0, 0]
# Menu 
Opcion_usuario = 0
Tomar_copete = 1
Ruleta = 2
Tragamonedas = 3
opcion = 0
 
print(" BIENVENIDO BALABET ")
# Menu 
Opcion_usuario = 0
Tomar_copete = 1
Ruleta = 2
Tragamonedas = 3
Salir = 4
fichas = 100
Chela = 30
Piscola = 50
Vodka = 110
blue_label = 200

bebidas_0 = 0
inventario = [fichas,bebidas_0,0]

while True:
    print("Que desea hacer")
    print("(1)beber algo")
    print("(2)jugar a la ruleta")
    print("(3)jugar a la Tragamonedas")
    print("(4)salir")

    Opcion_usuario = int(input(""))

    if Opcion_usuario == 1:
        bebida_0 = 0
        while True:
            print("BIENVENIDO AL BAR")
            print(f"Fichas disponibles {fichas}")
            print(f"Multiplicador {multiplicador_bebida}")
            print("QUE DESEA BEBER")
            print(f"(1) CERVEZA DUFF [{Chela} FICHAS] (x1.2)")
            print(f"(2) Piscola [{Piscola} FICHAS] (x1.5)") 
            print(f"(3) VODKA [{Vodka} FICHAS] (x2.0)")
            print(f"(4) Blue Label [{blue_label} fichas] (x5.0)")
            print("(5) Salir del bar")   
            bebida_0 = int(input(""))
        
            if bebida_0 == 5:
                break
                valor_bebida = 0
            if bebida_0 == 1:
                valor_bebida= Chela
                multiplicador_bebida = 1.2
            elif bebida_0 == 2:
                valor_bebida = Piscola
                multiplicador_bebida = 1.5
            elif bebida_0 == 3:
                valor_bebida = Vodka
                multiplicador_bebida = 2.0
            elif bebida_0 == 4:
                valor_bebida = blue_label
                multiplicador_bebida = 5.0
            else:
                print("")

            if bebida_0 == 1 or bebida_0 == 2 or bebida_0 == 3 or bebida_0 ==4:
                if (fichas - valor_bebida) < 10:
                    print("No se puede comprar el objerto y quedarte con menos de 10 fichas")
                elif(fichas - valor_bebida) > 10:
                    fichas = fichas - valor_bebida
                    inventario[0] = fichas
                    print(f"Tomas Alcohol y te sientes extraño...")
                    print(f"ACTUALMENTE TIENE {fichas} fichas y un multiplicador de {multiplicador_bebida}")
                else:
                    print("Ingrese una opcion valida. ")
    elif Opcion_usuario == 2:
        while True:
            print("--- BIENVENIDO A LA RULETA ---")
            print(f"Fichas disponibles: {fichas}")
            print("(1) Apostar a un COLOR")
            print("(2) Apostar a un NÚMERO")
            print("(3) Salir de la ruleta")

            tipo_apuesta = int(input(""))

            if tipo_apuesta == 3:
                break

            if tipo_apuesta == 1 or tipo_apuesta == 2:
                apuesta = int(input("¿Cuántas fichas deseas apostar? "))
                if apuesta > fichas or apuesta <= 0:
                    print("Apuesta invalida o sin fondos")
                else:
                    # Se descuentan las fichas antes de jugar
                    fichas = fichas - apuesta   
                    inventario[0] = fichas

                    numero_ganador = random.randint(0, 36)
                    # 0 verde, pares negro, impares rojo
                    if numero_ganador == 0:
                        color_ganador = "verde"
                    elif numero_ganador % 2 ==0:
                        color_ganador = "negro"
                        
                    else:
                        color_ganador = "rojo"

                    if tipo_apuesta == 1:
                        color_apuesta = input("¿A qué color apuesta (rojo/negro/verde: ")
                        print("Cayó el numero", numero_ganador, "y el color es", color_ganador)
                        print(numero_ganador)

                        if color_apuesta == color_ganador:
                           ganancia = apuesta*2
                           premio_final = ganancia * multiplicador_bebida
                           fichas += premio_final
                           inventario[0] = fichas
                           print("!Ganaste¡ ahora tienes", fichas, "fichas")
                        else:
                            print("Perdiste la apuesta. Ahora tienes", fichas, "fichas")
                    
                    elif tipo_apuesta == 2:
                        num_apuesta = int(input("¿A qué número apuesta? (0 - 36): "))

                        if num_apuesta == numero_ganador:
                            ganancia = apuesta * 36
                            premio_final = ganancia * multiplicador_bebida
                            fichas += premio_final
                            inventario[0] = fichas
                            print("¡Acertaste el número! Ahora tienes", fichas, "fichas")
                        else:
                            print("Perdiste la apuesta. Ahora tienes", fichas, "fichas")
    elif Opcion_usuario == 3:
        # Metan el codigo del tragamonedas xat
        apuesta= 0
        slot_1= 0
        slot_2= 0
        slot_3= 0
        fichas = 100
        slots = [slot_1, slot_2, slot_3]
        tope = 7
        multiplicador = 0
        fichas_ganadas = 0

        while True:
            print("===TRAGAMONEDAS GOLOSA===")
            apuesta = int(input("INGRESE UNA APUESTA (minimo 10 fichas): "))


            if apuesta >= 10:
                slot_1 = random.randint(1, 7)
                slot_2 = random.randint(1, 7)
                slot_3 = random.randint(1, 7)
                slots = [slot_1, slot_2, slot_3]
                
                suma = slot_1 + slot_2 + slot_3
            
                print(slots)
                if suma == 0:
                    multiplicador = 0
                elif suma <= 3 and suma > 0:
                    multiplicador = 0.1
                elif suma <= 6 and suma > 3:
                    multiplicador = 0.2
                elif suma <= 9 and suma > 6:
                    multiplicador = 0.3
                elif suma <= 11 and suma > 9:
                    multiplicador = 0.4
                elif suma <= 13 and suma > 11:
                    multiplicador = 0.5
                elif suma <= 14 and suma > 13:
                    multiplicador = 0.9
                elif suma <= 15 and suma > 9:
                    multiplicador = 1.2
                elif suma <= 16 and suma > 15:
                    multiplicador = 1.8
                elif suma <= 18 and suma > 15:
                    multiplicador = 2.0
                elif suma <= 20 and suma > 18:
                    multiplicador = 3.0
                elif suma <= 21 and suma > 20:
                    multiplicador = 10.0
            else:
                print("APUESTA MUY BAJA")    
            
            print(f"SE OBTUBO UN x {multiplicador}")
            fichas_ganadas = apuesta * multiplicador
            premio_final1 = fichas_ganadas * multiplicador_bebida
            fichas_ganadas += premio_final1
            print(f"FICHAS GANADAS {fichas_ganadas}")
            print(f"TOTAL FICHAS: {fichas} fichas")
            print("(1)JUGAR DE NUEVO" \
            "(2)SALIR")
            opcion = int(input(""))
            if opcion == 2:
                break
            elif opcion == 1:
               print("")
    elif Opcion_usuario == 4:
              break
    else:
        print("INGRESE UNA OPCION VALIDA")
        print("metanlo aca")