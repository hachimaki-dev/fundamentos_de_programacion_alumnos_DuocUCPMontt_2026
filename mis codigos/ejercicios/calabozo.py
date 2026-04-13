print("---------- CALABOZO ----------")

habilidad = input("¿Elijes ser Ladron o Guerrero?: ").lower()

for i in range (1,4):
    print("\n=========================================")
    print(f"ESTAS EN LA HABITACION {i} DEL CALABOZO")
    print("=========================================\n")

    intentos = 0
    abierta = False

    while intentos < 3 and not abierta:
        
        print("------- PUERTA CERRADA -------\n")
        print(f"Tu intento numero: {intentos + 1}/3")
        print("1. Forzar")
        print("2. Ganzua")
        print("3. Buscar Llave\n")

        eleccion = int(input("¿Que opcion vas a realizar?: "))

        if eleccion == 1:
            if habilidad == "guerrero":
                print("Has Logrado desbloquear la puerta y avanzaste a la siguiente habitacion :D")
                print(f" ~~ Saliendo de la habitacion {i} ~~\n")
                abierta = True
            else:
                intentos += 1
                print("No has podido desbloquear la puerta\n")

        elif eleccion == 2:
            if habilidad == "ladron":
                print("Has Logrado desbloquear la puerta y avanzaste a la siguiente habitacion :D")
                print(f"~~ Saliendo de la habitacion {i} ~~\n")
                abierta = True
            else:
                intentos += 1
                print("No has podido desbloquear la puerta\n")

        elif eleccion == 3:
            numero_elegido = int(input("Elije un numero entre el 1 al 6: "))
            if 1 <= numero_elegido <= 6:
                if numero_elegido % 2 == 0:
                    print(f"¡Acertaste! Has encontrado la llave y has podido desbloquear la puerta y avanzaste a la siguiente habitacion :D")
                    print(f"~~ Saliendo de la habitacion {i} ~~\n")
                    abierta = True
                else:
                    intentos += 1
                    print("Lo siento, no pudiste desbloquear la puerta\n")

            else:
                print("¡Elije una opcion valida!\n")

    if not abierta:
        print("------------ GAME OVER ------------\n")
        print(f"No lograste abrir la puerta de la habitacion {i} tras 3 intentos\n")
        break

print("------- FIN DEL CALABOZO -------\n")
if i == 3 and abierta:
    print("Enhorabuena has logrado atrevesar las 3 habitaciones :D\n")
else:
    print("Perdiste, no has podido atravesar las 3 habitaciones :c\n")