vida_del_jugador = 100
mana_del_jugador = 20
vida_del_jefe = 150

print("---"*14)
print("Mini Juego")
print("---"*14)
print("***"*14)
print("Derrota al Jefe Final")
print("***"*14)

while vida_del_jugador > 0 and vida_del_jefe > 0:
    print("1. Atacar(20 de daño al jefe)\n2. Magia(gasta 5 de mana)/(Pero ase 50 de daño al jefe )\n3. Pocion de vida (Recuperas 30 de" \
    "vida a cambio te quedas sin mana )")
    accion_del_jugador = int(input("Que accion va a Realizar:  "))
    if accion_del_jugador == 1:
        vida_del_jefe -= 20
    elif accion_del_jugador == 2:
        if mana_del_jugador >= 5:
            mana_del_jugador -= 5
            vida_del_jefe -= 50
        else:
            print("Mana Insuficiente para este Ataque")
    elif accion_del_jugador == 3:
        vida_del_jugador += 30
        print("Recuperaste 30 de vida , Pero te as quedado sin mana ")
        mana_del_jugador = 0
    else:
        print("Accion no Valida")
    
    if vida_del_jefe > 0:
        print("El jefe te aserto un ataque equivalente a 15 de daño")
        vida_del_jugador -= 15

if vida_del_jefe <= 0:
    print("Felicitaciones as derrotado al Jefe Final")
elif vida_del_jugador <= 0:
    print("Que lastima el Jefe te a Derrotado")

