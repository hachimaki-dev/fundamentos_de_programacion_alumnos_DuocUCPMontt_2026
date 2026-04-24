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
            print("QUE DESEA BEBER")
            print("(1) CERVEZA DUFF [30 FICHAS]")
            print("(2) Piscola [50 FICHAS]") 
            print("(3) VODKA [110 FICHAS]")
            print("(4) Blue Label [200 fichas]")
            print("(5) Salir del bar")   
            bebida_0 = int(input(""))
        
            if bebida_0 == 5:
                break

            valor_bebida = 0
            if bebida_0 == 1:
                valor_bebida = Chela
            elif bebida_0 == 2:
                valor_bebida = Piscola
            elif bebida_0 == 3:
                valor_bebida = Vodka
            elif bebida_0 == 4:
                valor_bebida = blue_label
            if bebida_0 == 1 or bebida_0 == 2 or bebida_0 == 3 or bebida_0 ==4:
                if fichas -valor_bebida < 10:
                    print("No se puede comprar el objerto y quedarte con menos de 10 fichas")
                else:
                    fichas = fichas - valor_bebida
                    inventario[0] = fichas
                    print("si")

    elif Opcion_usuario == 2:
        while True:
            print("--- BIENVENIDO A LA RULETA ---")
            print("Fichas disponibles:", fichas)
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

                        if color_apuesta == color_ganador:
                            ganancia = apuesta * 2
                            fichas = fichas + ganancia
                            inventario[0] = fichas
                            print("!Ganaste¡ ahora tienes", fichas, "fichas")
                        else:
                            print("Perdiste la apuesta. Ahora tienes", fichas, "fichas")
                    
                    elif tipo_apuesta == 2:
                        num_apuesta = int(input("¿A qué número apuesta? (0 - 36): "))

                        if num_apuesta == numero_ganador:
                            ganancia = apuesta * 36
                            fichas = fichas + ganancia
                            inventario[0] = fichas
                            print("¡Acertaste el número! Ahora tienes", fichas, "fichas")
                        else:
                            print("Perdiste la apuesta. Ahora tienes", fichas, "fichas")
    elif opcion_usuario == 3:
        # Metan el codigo del tragamonedas xat
        print("metanlo aca")
    elif Opcion_usuario == 4:
        break
