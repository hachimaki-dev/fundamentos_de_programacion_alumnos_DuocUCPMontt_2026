vida_de_jefe = 1000
print("ataca al jefe (1000 de vida)")
while vida_de_jefe > 0:
    daño_del_jugador = int(input("introduce tu daño: "))
    if daño_del_jugador > 0:
        vida_de_jefe = vida_de_jefe - daño_del_jugador
        print(f"hiciste {daño_del_jugador} de daño!")
        print(f"---la vida del jefe es {vida_de_jefe}---")
    else:
        print("---fallaste intentalo de nuevo---")

print("---FELICIDADES GANASTE---")