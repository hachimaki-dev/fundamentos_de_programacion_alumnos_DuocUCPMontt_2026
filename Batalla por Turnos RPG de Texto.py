vida_jugador = 100
vida_jefe = 150
mana_jugador = 20

print("Que comience la batalla")

while vida_jugador > 0 and vida_jefe > 0:
    print(f"vida del jugador: {vida_jugador}, Mana del jugador: {mana_jugador}")
    print(f"vida del jefe: {vida_jefe}")

    print("Elige tu accion")
    print("1. Atacar")
    print("2. Magía")
    print("3. Curación")

    accion = int(input("Realizar una accion: "))
    
    if accion == 1:
        vida_jefe = vida_jefe - 20
        print(f"Has atacado al jefe, vida del jefe: {vida_jefe}")
    elif accion == 2:
        if mana_jugador >=5:
            mana_jugador = mana_jugador - 5
            vida_jefe = vida_jefe - 50
            print(f"Has lanzado un hechizo al jefe, vida del jefe: {vida_jefe}, mana del jugador: {mana_jugador}")
        else:
            print("No tienes suficiente mana para lanzar un hechizo, pierdes un turno")
    elif accion == 3:
        vida_jugador = vida_jugador + 30
        mana_jugador = 0
        print(f"Has utilizado una pocion de curacion, vida del jugador: {vida_jugador}, mana del jugador: {mana_jugador}")
    else:
        print("Acción no valida, pierdes un turno")

    #Turno del jefe siempre y cuando siga vivo
    if vida_jefe > 0:
        vida_jugador = vida_jugador - 15
        print(f"El jefe ha atacado al jugador, vida del jugador: {vida_jugador}")
    
#Determinar ganador
if vida_jugador <= 0:
    print("Has sido derrotado por el jefe final.")
else:
    print("Felicidades has derrotado al jefe final")

