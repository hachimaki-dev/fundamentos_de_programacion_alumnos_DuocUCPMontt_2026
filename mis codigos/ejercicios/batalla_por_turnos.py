vida_jugador = 100
mana = 20
vida_jefe_final = 150

while vida_jugador > 0 and vida_jefe_final > 0:

    print("\n------ TU TURNO ------")
    print(f"Vida: {vida_jugador} | Maná = {mana}\n")
    print("1. Atacar (-20 de vida al Jefe)")
    print("2. Magia (Gasta 5 de maná)")
    print("3. Pocion de Vida (Gasta todo el Maná)\n")

    eleccion = int(input("¿Que deseas realizar?:"))

    if eleccion == 1:
        vida_jefe_final -= 20
        print("¡Le has hecho 20 de daño al Jefe!\n")
        print(f"¡La vida actual del Jefe es de: {vida_jefe_final} de vida restante!\n")

    elif eleccion == 2:
        if mana >= 5:
            mana -= 5
            vida_jefe_final -= 50
            print("\n~~ ¡Le has hecho 50 de daño al Jefe! ~~\n")
            print(f"La vida actual del Jefe es de: {vida_jefe_final} de vida restante\n")
        
        else:
            print("¡No tienes maná suficiente para realizar esta accion!\n")

    elif eleccion == 3:
        vida_jugador += 30
        mana -= mana
        print(f"~~ ¡Tu mana ahora es de: {mana}! ~~")

    if vida_jefe_final > 0:
        vida_jugador -= 15
        print(f"~~ ¡El Jefe te ha contraatacado quitandote 15 de vida! ~~\n")

print("------ FIN DEL COMBATE ------")
if vida_jugador > 0:
    print("¡Jefe final derrotado!. Enhorabuena has completado el juego. :D\n")

else:
    print("~~ El Jefe te ha derrotado :c ~~\n")