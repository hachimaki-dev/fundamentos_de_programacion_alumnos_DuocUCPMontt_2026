vida_jugador = 100;
mana = 20;
vida_jefe = 150;
while vida_jugador > 0 and vida_jefe > 0:
    menu = input("Elige tu acción: 1) Atacar 2) Magia 3) Poción de vida: ")
    if menu == "1":
        vida_jefe -= 20
        print("Has atacado al jefe. Vida del jefe: ", vida_jefe)
    elif menu == "2" and mana >= 5:
        vida_jefe -= 50 
        mana -= 5
        print("Has usado magia. Vida del jefe: ", vida_jefe, "Mana restante: ", mana)
    elif menu == "3" and mana >= 5:
        vida_jugador += 30 
        mana -= mana;
        print("Has usado una poción de vida. Vida del jefe: ", vida_jefe, "No queda mana.")
    else:
        print("Acción no válida o mana insuficiente.")
    
    if vida_jefe > 0:
        vida_jugador -= 15
        print("El jefe te ha atacado. Vida del jugador: ", vida_jugador)
if vida_jugador <= 0:
    print("Has sido derrotado por el jefe.")
else:    print("¡Has derrotado al jefe!")