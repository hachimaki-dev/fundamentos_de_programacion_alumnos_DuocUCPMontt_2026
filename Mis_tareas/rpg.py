mana=20
vida_jefe=150
vida_jugador=100
opcion=""
print("Te encuentras luchando a muerte contra tu archienemigo")
while vida_jefe > 0 and vida_jugador > 0:
    print(f"Tu vida: {vida_jugador} mana restante: {mana}") 
    print(f"Vida del jefe: {vida_jefe} ")
    print("1-Atacar")
    print("2-Magia")
    print("3-Pocion")
    opcion=input("elije lo que quieres hacer: ")
    if opcion == "1":
        print("atacaste")
        vida_jefe -= 20 
        vida_jugador -= 15
    elif opcion== "2":
        if mana >0:
            print("Atacaste con tu magia mas fuerte")
            vida_jefe -= 50
            vida_jugador -= 15
        else:
            print("No tienes mana...")
            vida_jugador -=15
    elif opcion== "3":
        if vida_jugador == 100:
            print("No es necesario curarse por ahora")
        elif vida_jugador<100:
            print("Te tomaste una pocion pero sientes como todo tu mana se drena")
            mana=0
            vida_jugador += 30
    else:
        print("Opcion no valida")
if vida_jefe >0:
    print("Has perdido")
else:
    print("Has ganado")
print("====FINAL====")