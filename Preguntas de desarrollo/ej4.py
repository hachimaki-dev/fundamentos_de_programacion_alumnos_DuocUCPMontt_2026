vida_jugador = 100
vida_jefe = 150
mana = 20
bandera = True

print("Bienvenido al RPG de python")
print("Tu como jugador tienes 100 puntos de vida y 20 de mana")
print("Para tu mala suerte, hay un Gran Boss que tiene 150 puntos de vida")
print("Como jugador tienes 3 opciones")

while bandera:
    print("1. Atacar")
    print("2. Mana")
    print("3. Curar (Ocupa todo tu restante de Mana)")
    eleccion = int(input("¿Que opción escojes? (Solamento numeros del 1 al 3)"))
    if eleccion == 1:
        print("Le has quitado 20 puntos de vida al gran boss")
        vida_jefe = vida_jefe - 20
        if vida_jefe > 0:
            print("El Gran Boss te ha quitado 15 puntos de vida")
            vida_jugador = vida_jugador - 15
            print(f"Tu vida actual es de {vida_jugador} Puntos")
            print(f"Vida del gran boss es de {vida_jefe} Puntos")
    if eleccion == 2:
        if mana >= 5:
            print("Le has quitado 50 puntos de vida al gran boss")
            vida_jefe = vida_jefe - 50
            print("Se te ha restado 5 de mana")
            mana = mana - 5
            print(f"Tu mama actual es de {mana}")
            if vida_jefe > 0:
                print("El Gran Boss te ha quitado 15 puntos de vida")
                vida_jugador = vida_jugador - 15
                print(f"Tu vida actual es de {vida_jugador} Puntos")
                print(f"Vida del gran boss es de {vida_jefe} Puntos")
        elif mana < 5:
            print("Mana insuficinete")
    if eleccion == 3:
        if mana > 0:
            print("Te has curado por completo ")
            mana = 0
            vida_jugador = 100
            print(f"Tu vida es de {vida_jugador} y tu mana es de {mana}")
        elif mana <= 0:
            print("Mana insuficiente")
        
        
    if vida_jugador <= 0 or vida_jefe <= 0:
        print("El juego ha terminado")
        if vida_jugador > 0 and vida_jefe <=0:
            print("FELICIDADES, HAZ GANADO AL GRAN BOSS")
            import sys
            sys.exit ()
        elif vida_jugador < 0 and vida_jefe >=0:
            print("Que lastima, te ha ganado el jefe")
            import sys
            sys.exit ()