print("haz pasado a la tercera pelea")
print("ha sido un camino largo, haz estado cerca de morir varias veces, pero haz logrado sobrevivir")
print("te encuentras frente a un nuevo enemigo, su nombre es shepyroth")
print("sientes que esta eplea sera la ms dificil de todas")
print("tu vida se ha restablecido, es momento de pelear")



vida_jugador = 1000
vida_jefe = 10000
rasen_shuriken = 1000
chidogan = 1000
super_genkidama = 2000
espada_infernus = 2500
contador_super_genkidama = 0

print("¡el jefe se dirige rapido hacia ti, debes elegir un ataque!")
print("¡recuerda que por cada ataque que haga el jefe te hara daño!")

print("1. rasen shuriken")
print("2. chidogan")
print("3. super genkidama")
print("4. espada infernus")



while vida_jefe > 0:
    while vida_jugador <= 0:
        print("shepyroth te ha derrotado")
        print("game over")

        continuar_3 =int(input("¿deseas continuar? 1) si , 2) no"))
        if continuar_3 == 1:
            vida_jefe = 10000
            vida_jugador = 1000
        elif continuar_3 == 2:
            print(" juego finalizado ")
            exit()
    
            
    ataque_jugador = int(input("elige un ataque(1-4):"))


    if ataque_jugador == 1:
        vida_jefe -= rasen_shuriken
        print("¡usaste rasen shuriken!")
        print("¡recuerda que puedes usar ataque mas fuertes en tu inventario!")
        print("¡puedes usar este ataque las veces que quieras")
    elif ataque_jugador == 2:
        vida_jefe -= chidogan
        print("¡usaste chidogan!")
        print("¡recuerda que puedes usar ataque mas fuertes en tu inventario!")
        print("¡puedes usar este ataque las veces que quieras!")
    elif ataque_jugador == 3:
        vida_jefe -= super_genkidama
        print("usaste super genkidama")
        print("¡recuerda que puedes usar este ataque solo dos veces!")
        contador_super_genkidama += 1
        if contador_super_genkidama >= 2:
            super_genkidama = 0    
    elif ataque_jugador == 4:
        vida_jefe -= espada_infernus
        print("¡usaste espada infernus!")
        print("¡recuerda que solo puedes usar este ataque una vez")
        espada_infernus = 0
    else:
        print("ataque invalido")
    vida_jugador -= 120
    print(f"tu vida se ha reducido considerablemente...{vida_jugador}") 
    print(f"la vida de shepýroth es {vida_jefe}")

if vida_jefe <= 0:
    print("¡haz derrotado al tercer jefe")
    print("¡felicidades, haz ganado el juego!")
    print("haz derrotado a todos los jefes, haz demostrado ser un gran guerrero")
    print("juego terminado, el guerrero a vuelto a casa con su familia")

    



















