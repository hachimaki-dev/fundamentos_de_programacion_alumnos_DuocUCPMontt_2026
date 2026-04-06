#Batalla por turnos, RPG TEXTO.

#Crea un simulador de combate de un juego de rol. El jugador tiene 100 de Vida y 20 de Maná. El Jefe Final tiene 150 de Vida.

vida_jefe = 150
vida_jugador = 100
turnos = 0
mana = 20
print("="*50)
print("Bienvenido a una increible aventura!\nDeberás de matar al jefe.")
print("="*50)

while vida_jefe > 0 and vida_jugador > 0:
    try:
        opcion = int(input(f"Que desea realizar en el turno {turnos + 1}?\n1. Atacar\n2. Magia (Gasta 5 de mana)\n3. Poción de vida (Te cura 30 puntos de vida pero gasta todo el maná)\n: "))
        if opcion == 1:
            print(f"Has decidido atacar al jefe, le quitaste 15 puntos de vida.")
            vida_jefe -= 15
            print(f"Al jefe le restan {vida_jefe} puntos de vida.")
            if vida_jefe > 0:
                print("Ahora es turno de que el jefe te ataque.")
                vida_jugador -= 15
                print(f"El jefe te ha quitado 15 puntos de vida, te quedan {vida_jugador}")
        elif opcion == 2:
            if mana >= 5:
                print(f"Has usado un ataque magico, perdiste 5 de maná.")
                mana -= 5
                vida_jefe -= 30
                print(vida_jefe)
                print(f"Al jefe le quedan {vida_jefe} puntos de vida")
                print(f"Te quedan {mana} reservas de mana")
            else:
                print("No tienes mana para esta acción.")
                continue
            if vida_jefe > 0:
                print("Ahora es turno de que el jefe te ataque.")
                vida_jugador -= 15
                print(f"El jefe te ha quitado 15 puntos de vida, te quedan {vida_jugador}")
        elif opcion == 3:
            if mana > 0:
                print("Se te añadiran 30 puntos de vida.")
                vida_jugador += 30
                mana = 0
                print(f"Ahora tienes un total de {vida_jugador} puntos de vida y te quedan {mana} reservas de mana.")
            else:
                print("No tienes mana para está acción.")
                continue
            if vida_jefe > 0:
                print("Ahora es turno de que el jefe te ataque.")
                vida_jugador -= 15
                print(f"El jefe te ha quitado 15 puntos de vida, te quedan {vida_jugador}")
        else:
            print("Mana insuficiente.")
            continue
        



    except ValueError:
        print("Ingresa una opción valida.")

if vida_jefe <= 0:
    print("Felicidades, has derrotado al jefe!")
elif vida_jugador <= 0:
    print("No solo has caido tu, sino que todos los de tu reino han perecido....")