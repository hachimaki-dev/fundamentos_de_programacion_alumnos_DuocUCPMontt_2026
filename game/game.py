import random

print(50*"-")
print("\tBienvenido a CASINO DUOC")
print(50*"-")

while True:
    saldo_inicial = int(input("Antes de empezar a jugar, ingresa la cantidad de dinero con el que entras al casino: $"))

    if saldo_inicial <= 0:
        print("Por favor, ingresa una cantidad de dinero válida")
    else:
        break

saldo = saldo_inicial
puede_jugar = 1

while True:
    if saldo > 0:
        while True:
            print("\nJuegos disponibles\n")
            
            print("1. Blackjack")
            print("2. Rueda Big Six")
            print("3. Tragamonedas")
            print("4. Ruleta europea")

            print("\n5. Salir")

            opcion_juego = int(input("Selecciona tu opción: "))

            if opcion_juego not in [1,2,3,4,5]:
                print("Por favor, ingresa una opción válida")
            else:
                break
    else:
        break

    if opcion_juego == 1:
        while True:
            print("\nBienvenido a BLACKJACK")
            print(f"Saldo actual: ${saldo}")

            print("Las reglas son:")
            print("1. El número mas cercano a 21, gana")
            print("2. Si te pasas de 21, pierdes")
            print("3. Si superas la mano de la casa, ganas")
            print("¡A disfrutar!")
            desicion_de_jugar = input("Presiona (c) para continuar o (v) para volver: ").lower()
            
            if desicion_de_jugar == "c":
                dinero_a_jugar  = int(input("¿Cuánto quieres apostar?: $"))
                
                if dinero_a_jugar <= saldo and dinero_a_jugar > 0:
                    carta1casa = random.randint(1,13)
                    carta2casa = random.randint(1,13) 

                    carta1 = random.randint(1,13) 
                    carta2 = random.randint(1,13)
                
                    cartas1y2 = carta1 + carta2
                    cartacasa1y2 = carta1casa + carta2casa 
                
                    print(f"Carta 1 casa: {carta1casa}")
                    print(f"Carta 2 casa: {carta2casa}")
                    print(f"La casa tiene: {cartacasa1y2}") 
                
                    print(f"Tu carta 1: {carta1}")  
                    print(f"Tu carta 2: {carta2}")
                    print(f"Tienes: {cartas1y2}")

                    if cartacasa1y2 > 21 and cartas1y2 <= 21:
                        print("La casa pierde, ¡Ganaste!")
                        saldo = saldo + dinero_a_jugar 
                        print(f"Tu nuevo saldo es: ${saldo}")
                        break
                    elif cartas1y2 > 21:
                        print("Perdiste")
                        saldo = saldo - dinero_a_jugar
                        print(f"Tu nuevo saldo es: ${saldo}")
                        break
                    elif cartas1y2 > 21 and cartacasa1y2 > 21:
                        print("Empate")
                        print(f"Tu nuevo saldo es: ${saldo}")
                        break
                    elif cartas1y2 > cartacasa1y2 and cartas1y2 <= 21:
                        saldo = dinero_a_jugar + saldo
                        print("Ganaste")
                        print(f"Tu nuevo saldo es: ${saldo}")
                        break
                    elif cartas1y2 < cartacasa1y2 and cartas1y2 <= 21:
                        print("Perdiste")
                        saldo = saldo - dinero_a_jugar
                        print(f"Tu nuevo saldo es: ${saldo}")
                        break
                    elif cartas1y2 == cartacasa1y2:
                        print("VAYA EMPATE")
                        print(f"te quedas con: {saldo}")
                        break
                    elif cartas1y2 < 21 and cartas1y2 < cartacasa1y2:
                        desicion = input("Presiona (s) para sacar otra carta o (j) para jugar: ").lower()
                    
                        if desicion == "s":
                            #joker = 1
                            carta3 = random.randint(1,13)

                            carta123 = cartas1y2 + carta3
                            print(f"Tienes un total de: {carta123}") 
            
                            if carta123 >= 21 and carta123 > cartacasa1y2:
                                print("ganaste")
                                saldo = saldo + dinero_a_jugar
                                print(f"te quedas con: {saldo}")
                                break
                            elif carta123 < 21 and carta123 < cartacasa1y2:
                                print("perdiste")
                                saldo = saldo + dinero_a_jugar
                                print(f"te quedas con: {saldo}")
                                break
                            else:
                                print("perdiste")
                                saldo = saldo - dinero_a_jugar
                                print(f"te quedas con: {saldo}")
                                break
                        elif desicion == "j":
                            continue
                else:
                    print("no valido")     
                    continue
            elif desicion_de_jugar == "v":
                print("es una pena adios ")
                break
            else:
                print("no valido empieza de nuevo")
                continue
    elif opcion_juego == 2:
        dolar1 = 60000
        dolar2 = 120000
        dolar3 = 90000
        perdida = 20

        premios = [0, 0, 0, dolar1, dolar2, dolar3]

        print("\nBienvenido a Rueda Big Six")
        print(f"Saldo actual: ${saldo}\n")
        
        print("Cada giro cuesta $20 (las perdidas se multiplican)")

        while saldo >= 20:
            jugada = int(input("Escribe '1' para jugar, '2' para salir "))
            
            if jugada != 1 and jugada != 2:
                print("ingresa un número válido.")
                continue
            
            if jugada == 2:
                print("Has decidido retirarte de la mesa.")
                break
            elif jugada == 1:
                print("Girando la rueda", end="")
                for i in range(6):
                    print("\n.", end="")
                perdida = perdida * 5
                
                resultado = random.choice(premios)
                
                if resultado == 0:
                    print(" La rueda cayó en 0.")
                    print(f"Pierdes ${perdida}.")
                    saldo -= perdida  
                else:
                    print(f" La rueda cayó en una casilla ganadora.")
                    print(f"Ganaste ${resultado}")
                    saldo += resultado
                    
                print("-" * 35)
            else:
                print(" Opción no válida")

        # Mensaje final de despedida
        if saldo < 20:
            print(" Te has quedado sin saldo suficiente para seguir jugando.")
            puede_jugar = False
            
        print(f"tu saldo final para llevar a casa es: ${saldo}.")
    elif opcion_juego == 3:
        iconos = ["🍒", "🔔", "💎", "⭐"]
        tiradas = 0
        prestamo = False
        deuda_prestamo = 0
        salida = False

        print()
        print("🎰 Bienvenido al TRAGAMONEDAS 🎰")
        print("  🎰========================🎰")
        print("    || 🍒 | 🔔 | 💎 | ⭐ ||")
        print("    >> ⭐ | 🍒 | 🔔 | 💎 <<")
        print("    || 💎 | ⭐ | 🍒 | 🔔 ||")
        print("  🎰========================🎰")
        print("          🎮 GIRAR 🎮")

        while True:
            print(f"\n💰 Saldo actual:💲{saldo}")

            if saldo <= 0 and prestamo == False:
                print()
                print("💀 Vaya, parece que te quedaste sin dinero...\n"
                    "El casino le está ofreciendo un préstamo de💲2000\n")

                opcion_prestamo = input("¿Deseas el préstamo? (si/no): ").lower()

                if opcion_prestamo == "si":
                    saldo += 2000
                    deuda_prestamo += 2000
                    prestamo = True
                    print(f"\nHas adquirido el préstamo, tu nuevo 💰 saldo es💲{saldo}")

                else:
                    print("💀 Fin del juego.\n")
                    break

            if saldo > 2000 and tiradas >= 6 and prestamo == True:
                pago_prestamo = input("¿Deseas pagar el préstamo? (si/no): ").lower()
                tiradas = 0

                if pago_prestamo == "si":
                    saldo -= deuda_prestamo
                    prestamo = False
                    print(f"Préstamo pagado. Su 💰 saldo actual es:💲{saldo}")
                else:
                    continue

            if saldo <= 0 and prestamo == True:
                print()
                print("💀 Te quedaste sin dinero.🕴️🕴️  Unos hombres vestidos de negro vienen a tu casa.\nFin del juego.\n")
                break

            print()

            if salida == True:
                salida = input("¿Deseas continuar? (si/no): ").lower()
                if salida != "si":
                    print("💀 Fin del juego.\n")
                    break

            entrada = input("¿Cuánto desea apostar?:💲")
            salida = True

            es_numero = True
            for c in entrada:
                if c < "0" or c > "9":
                    es_numero = False

            if entrada == "" or es_numero == False:
                print("Ingrese un número válido")
                continue

            saldo_de_apuesta = int(entrada)

            if saldo_de_apuesta <= 0:
                print("Ingrese un monto válido")
                continue

            if saldo_de_apuesta > saldo:
                print("No tienes suficiente 💰 saldo")
                continue

            saldo -= saldo_de_apuesta

            superior1 = random.choice(iconos)
            superior2 = random.choice(iconos)
            superior3 = random.choice(iconos)
            superior4 = random.choice(iconos)

            resultado1 = random.choice(iconos)
            resultado2 = random.choice(iconos)
            resultado3 = random.choice(iconos)
            resultado4 = random.choice(iconos)

            inferior1 = random.choice(iconos)
            inferior2 = random.choice(iconos)
            inferior3 = random.choice(iconos)
            inferior4 = random.choice(iconos)

            print()
            print("        LAS VEGAS SLOTS")
            print("  🎰========================🎰")
            print(f"    || {superior1} | {superior2} | {superior3} | {superior4} ||")
            print(f"    >> {resultado1} | {resultado2} | {resultado3} | {resultado4} <<")
            print(f"    || {inferior1} | {inferior2} | {inferior3} | {inferior4} ||")
            print("  🎰========================🎰")

            if resultado1 == resultado2 == resultado3 == resultado4:
                premio = saldo_de_apuesta * 5
                saldo += premio
                print()
                print(f"🎉 ¡JACKPOT! 🎉 Ganaste💲{premio}")

            elif (
                resultado1 == resultado2 == resultado3 or
                resultado1 == resultado2 == resultado4 or
                resultado1 == resultado3 == resultado4 or
                resultado2 == resultado3 == resultado4
            ):
                premio = saldo_de_apuesta * 2
                saldo += premio
                print()
                print(f"✨ Ganaste💲{premio}")

            else:
                print()
                print("😢 Perdiste la apuesta")
            tiradas += 1
    elif opcion_juego == 4:
        OPCIONES_VALIDAS = list(range(1,9)) # 1 - 8

        SECUENCIA = list(range(0,37))       # 0 - 36

        ROJOS = [1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36]
        NEGROS = [2, 4, 6, 8, 10, 11, 13, 15, 17, 20, 22, 24, 26, 28, 29, 31, 33, 35]

        PARES = list(range(0,37,2))
        IMPARES = list(range(1,36,2))

        FALTA = list(range(1,19))           # 1 - 18
        PASA = list(range(19,37))           # 19 - 36

        DOCENA_1 = list(range(1,13))        # 1 - 12
        DOCENA_2 = list(range(13,25))       # 13 - 24
        DOCENA_3 = list(range(25,37))       # 25 - 36

        COLUMNA_1 = list(range(1,35,3))
        COLUMNA_2 = list(range(2,36,3))
        COLUMNA_3 = list(range(3,37,3))

        TIPOS_APUESTAS = {                  # Nombre: Multiplicador
            "rojo o negro": 1, 
            "par o impar": 1,
            "falta o pasa": 1,
            "docenas": 2,
            "columnas": 2,
            "pleno": 35,
            "calle": 11
            }

        print("---------- Ruleta Europea ----------")
        print(f"Saldo: ${saldo}")

        while True:
            while True:
                if saldo <= 0:
                    break

                print("\n¿Donde quieres apostar?\n")

                print("1. Rojo o Negro (Paga x1)")
                print("2. Par o Impar (Paga x1)")
                print("3. Falta o Pasa (Paga x1)")
                print("4. Docenas (Paga x2)")
                print("5. Columnas (Paga x2)")
                print("6. Pleno (Paga x35)")
                print("7. Calle (Paga x11)")
                print("8. Salir")

                opcion_apuesta = int(input("Selecciona tu opción: "))

                if opcion_apuesta not in OPCIONES_VALIDAS:
                    print("Por favor, ingrese una opción válida")
                else:
                    break

            if opcion_apuesta == 8 or saldo <= 0:
                break

            while True:
                monto_apuesta = int(input("Ingresa el monto a apostar: $"))
                print("")

                if monto_apuesta > saldo:
                    print("No tienes dinero suficiente, ingresa otro monto")
                elif monto_apuesta < 1:
                    print("No puede apostar ese monto, ingresa otro monto")
                else:
                    break

            num_aleatorio = random.choice(SECUENCIA)            # Se escoge el número aleatorio

            if opcion_apuesta == 1:                             # Rojo o Negro
                multiplicador = TIPOS_APUESTAS.get("rojo o negro")

                while True:
                    print("¿A cuál color quieres apostar?")
                    print("1. Rojo")
                    print("2. Negro\n")

                    eleccion_apuesta = int(input("Selecciona tu opción: "))

                    if eleccion_apuesta != 1 and eleccion_apuesta != 2:
                        print("Por favor, ingresa una opción válida")
                    else:
                        break
                
                print(50*"-")
                print(f"La bola cayó en {num_aleatorio}")
                print(50*"-")

                if eleccion_apuesta == 1:                       # Escogió rojo
                    if num_aleatorio in ROJOS:                      # Ganó
                        saldo += monto_apuesta * multiplicador
                        print("¡Ganaste!, es rojo 🔴")
                        print(f"Tu nuevo saldo es: ${saldo}")
                    else:                                           # Perdió
                        saldo -= monto_apuesta
                        print("Perdiste, es negro ⚫")
                        print(f"Tu nuevo saldo es: ${saldo}")
                else:                                           # Escogió negro
                    if num_aleatorio in NEGROS:                     # Ganó
                        saldo += monto_apuesta * multiplicador
                        print("¡Ganaste!, es negro ⚫")
                        print(f"Tu nuevo saldo es: ${saldo}")
                    else:                                           # Perdió
                        saldo -= monto_apuesta
                        print("Perdiste, es rojo 🔴")
                        print(f"Tu nuevo saldo es: ${saldo}")
            elif opcion_apuesta == 2:                           # Par o Impar
                multiplicador = TIPOS_APUESTAS.get("par o impar")

                while True:
                    print("¿A cual opción quieres apostar")
                    print("1. Par")
                    print("2. Impar\n")

                    eleccion_apuesta = int(input("Selecciona tu opción: "))

                    if eleccion_apuesta != 1 and eleccion_apuesta != 2:
                        print("Por favor, selecciona una opción válida")
                    else:
                        break

                print(50*"-")
                print(f"La bola cayó en {num_aleatorio}")
                print(50*"-")

                if eleccion_apuesta == 1:                       # Escogió par
                    if num_aleatorio in PARES:                      # Ganó
                        saldo += monto_apuesta * multiplicador
                        print(f"{num_aleatorio} es par, ¡Ganaste!")
                        print(f"Tu nuevo saldo es: ${saldo}")
                    else:                                           # Perdió
                        saldo -= monto_apuesta
                        print(f"{num_aleatorio} es impar, perdiste")
                        print(f"Tu nuevo saldo es: ${saldo}")
                else:                                           # Escogió impar
                    if num_aleatorio in IMPARES:                      # Ganó
                        saldo += monto_apuesta * multiplicador
                        print(f"{num_aleatorio} es par, ¡Ganaste!")
                        print(f"Tu nuevo saldo es: ${saldo}")
                    else:
                        saldo -= monto_apuesta                      # Perdió
                        print(f"{num_aleatorio} es impar, perdiste")
                        print(f"Tu nuevo saldo es: ${saldo}")
            elif opcion_apuesta == 3:                           # Falta o Pasa
                multiplicador = TIPOS_APUESTAS.get("falta o pasa")

                while True:
                    print("¿A cual opción quieres apostar")
                    print("1. Falta (1 - 18)")
                    print("2. Pasa (19 - 36)\n")

                    eleccion_apuesta = int(input("Selecciona tu opción: "))

                    if eleccion_apuesta != 1 and eleccion_apuesta != 2:
                        print("Por favor, selecciona una opción válida")
                    else:
                        break

                print(50*"-")
                print(f"La bola cayó en {num_aleatorio}")
                print(50*"-")

                if eleccion_apuesta == 1:                       # Escogió falta
                    if num_aleatorio in FALTA:                      # Ganó
                        saldo += monto_apuesta * multiplicador
                        print(f"{num_aleatorio} está en Falta, ¡Ganaste!")
                        print(f"Tu nuevo saldo es: ${saldo}")
                    else:                                           # Perdió
                        saldo -= monto_apuesta
                        print(f"{num_aleatorio} está en Pasa, perdiste")
                        print(f"Tu nuevo saldo es: ${saldo}")
                else:                                           # Escogió pasa
                    if num_aleatorio in PASA:                      # Ganó
                        saldo += monto_apuesta * multiplicador
                        print(f"{num_aleatorio} está en Pasa, ¡Ganaste!")
                        print(f"Tu nuevo saldo es: ${saldo}")
                    else:
                        saldo -= monto_apuesta                      # Perdió
                        print(f"{num_aleatorio} está en Falta, perdiste")
                        print(f"Tu nuevo saldo es: ${saldo}")
            elif opcion_apuesta == 4:                           # Docenas
                multiplicador = TIPOS_APUESTAS.get("docenas")

                while True:
                    print("¿A cual opción quieres apostar")
                    print("1. 1ra docena (1 - 12)")
                    print("2. 2da docena (13 - 24)")
                    print("3. 3ra docena (25 - 36)")

                    eleccion_apuesta = int(input("Selecciona tu opción: "))

                    if eleccion_apuesta != 1 and eleccion_apuesta != 2 and eleccion_apuesta != 3:
                        print("Por favor, selecciona una opción válida")
                    else:
                        break

                print(50*"-")
                print(f"La bola cayó en {num_aleatorio}")
                print(50*"-")

                if eleccion_apuesta == 1:                       # Escogió 1ra docena
                    if num_aleatorio in DOCENA_1:                   # Ganó
                        saldo += monto_apuesta * multiplicador
                        print(f"{num_aleatorio} está en la 1ra docena, ¡Ganaste!")
                        print(f"Tu nuevo saldo es: ${saldo}")
                    else:                                           # Perdió
                        saldo -= monto_apuesta
                        print(f"{num_aleatorio} no está la 1ra docena, perdiste")
                        print(f"Tu nuevo saldo es: ${saldo}")
                elif eleccion_apuesta == 2:                     # Escogió 2da docena
                    if num_aleatorio in DOCENA_2:                   # Ganó
                        saldo += monto_apuesta * multiplicador
                        print(f"{num_aleatorio} está en la 2da docena, ¡Ganaste!")
                        print(f"Tu nuevo saldo es: ${saldo}")
                    else:                                           # Perdió
                        saldo -= monto_apuesta
                        print(f"{num_aleatorio} no está la 2da docena, perdiste")
                        print(f"Tu nuevo saldo es: ${saldo}")
                else:                                           # Escogió 3ra docena
                    if num_aleatorio in DOCENA_3:                   # Ganó
                        saldo += monto_apuesta * multiplicador
                        print(f"{num_aleatorio} está en la 3ra docena, ¡Ganaste!")
                        print(f"Tu nuevo saldo es: ${saldo}")
                    else:                                           # Perdió
                        saldo -= monto_apuesta
                        print(f"{num_aleatorio} no está la 3ra docena, perdiste")
                        print(f"Tu nuevo saldo es: ${saldo}")
            elif opcion_apuesta == 5:                           # Columnas
                multiplicador = TIPOS_APUESTAS.get("columnas")

                while True:
                    print("¿A cual opción quieres apostar?")
                    print("1. 1ra columna")
                    print("2. 2da columna")
                    print("3. 3ra columna")

                    eleccion_apuesta = int(input("Selecciona tu opción: "))

                    if eleccion_apuesta != 1 and eleccion_apuesta != 2 and eleccion_apuesta != 3:
                        print("Por favor, selecciona una opción válida")
                    else:
                        break

                print(50*"-")
                print(f"La bola cayó en {num_aleatorio}")
                print(50*"-")

                if eleccion_apuesta == 1:                       # Escogió 1ra columna
                    if num_aleatorio in COLUMNA_1:                   # Ganó
                        saldo += monto_apuesta * multiplicador
                        print(f"{num_aleatorio} está en la 1ra columna, ¡Ganaste!")
                        print(f"Tu nuevo saldo es: ${saldo}")
                    else:                                           # Perdió
                        saldo -= monto_apuesta
                        print(f"{num_aleatorio} no está la 1ra columna, perdiste")
                        print(f"Tu nuevo saldo es: ${saldo}")
                elif eleccion_apuesta == 2:                     # Escogió 2da columna
                    if num_aleatorio in COLUMNA_2:                   # Ganó
                        saldo += monto_apuesta * multiplicador
                        print(f"{num_aleatorio} está en la 2da columna, ¡Ganaste!")
                        print(f"Tu nuevo saldo es: ${saldo}")
                    else:                                           # Perdió
                        saldo -= monto_apuesta
                        print(f"{num_aleatorio} no está la 2da columna, perdiste")
                        print(f"Tu nuevo saldo es: ${saldo}")
                else:                                           # Escogió 3ra columna
                    if num_aleatorio in COLUMNA_3:                   # Ganó
                        saldo += monto_apuesta * multiplicador
                        print(f"{num_aleatorio} está en la 3ra columna, ¡Ganaste!")
                        print(f"Tu nuevo saldo es: ${saldo}")
                    else:                                           # Perdió
                        saldo -= monto_apuesta
                        print(f"{num_aleatorio} no está la 3ra columna, perdiste")
                        print(f"Tu nuevo saldo es: ${saldo}")
            elif opcion_apuesta == 6:                           # Pleno
                multiplicador = TIPOS_APUESTAS.get("pleno")

                while True:
                    eleccion_apuesta = int(input("¿A qué número quieres apostar?: "))

                    if eleccion_apuesta not in SECUENCIA:
                        print("Por favor, ingresa un número válido")
                    else:
                        break

                print(50*"-")
                print(f"La bola cayó en {num_aleatorio}")
                print(50*"-")

                if num_aleatorio == eleccion_apuesta:               # Ganó
                    saldo += monto_apuesta * multiplicador
                    print("¡Ganaste!")
                    print(f"Tu nuevo saldo es: ${saldo}")
                else:                                               # Perdió
                    saldo -= monto_apuesta
                    print("Perdiste")
                    print(f"Tu nuevo saldo es: ${saldo}")
            elif opcion_apuesta == 7:                                               # Calle
                multiplicador = TIPOS_APUESTAS.get("calle")

                while True:
                    for i in range(12):
                        n1 = i * 3 + 1
                        n2 = i * 3 + 2
                        n3 = i * 3 + 3
                        print(f"{i+1}. ({n1}, {n2}, {n3})")

                    eleccion_apuesta = int(input("¿A qué calle quieres apostar?: "))

                    if eleccion_apuesta not in list(range(1,13)):
                        print("Por favor, ingresa una opción válida")
                    else:
                        break

                print(50*"-")
                print(f"La bola cayó en {num_aleatorio}")
                print(50*"-")

                num_fila_num_aleatorio = (num_aleatorio - 1) // 3 + 1
                
                if num_fila_num_aleatorio == eleccion_apuesta:      # Ganó
                    saldo += monto_apuesta * multiplicador
                    print("¡Ganaste!")
                    print(f"Tu nuevo saldo es: ${saldo}")
                else:
                    saldo -= monto_apuesta
                    print("Perdiste")
                    print(f"Tu nuevo saldo es: ${saldo}")          # Perdió

        if saldo <= 0:
            print("Se acabó el juego, te quedaste sin dinero")
        else:
            print("¡Gracias por jugar!")
            print(f"Tu saldo final es de: ${saldo}")
    else:
        break

print("\n¡Gracias por visitar nuestro casino!")
print(f"Te fuiste con ${saldo}\n")

if saldo > saldo_inicial:
    print(f"Es decir, ganaste ${saldo - saldo_inicial}")
elif saldo < saldo_inicial:
    print(f"Es decir, perdiste ${saldo_inicial - saldo}")
else:
    print(f"Es decir, no ganaste ni perdiste dinero")