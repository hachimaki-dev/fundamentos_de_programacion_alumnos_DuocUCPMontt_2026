# Juego de una nave espacial contra un alien

vida_jugador = 100
bateria_laser = 20
vida_alien = 150
daño_alien = 15

turno = 1 
escudo_activo = False

while vida_jugador > 0 and vida_alien > 0: 
    print("👾======Bienvenido a Batalla Espacial======👾")
    print(f"Turno: {turno}")
    print(f"Energia: {vida_jugador} Bateria: {bateria_laser}")
    print(f"Vida Alien: {vida_alien}")


    print("Acciones")
    print("1. Disparo basico (-20)")
    print("2. Laser potente (-50)")
    print("3. Reparar (+30)")
    print("4. Activar escudo (-50 bateria, reduce daño enemigo)")
    print("5. Recargar bateria (+10)")
    print("6. Ataque critico (Daño alto)")

    opcion = int(input("Escoge una opcion"))

    if opcion == 1: 
        daño = 20
        vida_alien -= daño
        turno+=1
        vida_jugador -= daño_alien
        print(f"Disparo basico: {daño} de daño")

    elif opcion == 2: 
        if bateria_laser >= 5:
            daño = 50
            vida_alien -= daño
            bateria_laser -= 5 
            vida_jugador -= daño_alien
            turno+=1
            print(f"Laser potente: {daño} de daño")
            print(f"Vida nave: {vida_jugador}")
        else: 
            print("Bateria Insuficiente")
            continue 

    elif opcion == 3: 
        if bateria_laser > 0: 
            vida_jugador += 30
            bateria_laser = 0
            vida_jugador -= daño_alien
            turno+=1
            print("Reparacion completada")
        else: 
            print("No tienes bateria")
            continue 

    elif opcion == 4: 
        bateria_laser += 10
        escudo_activo = True 
        bateria_laser -= 10
        vida_jugador -= daño_alien
        turno+=1
        print("Escudo activado (reduce daño del enemigo)")
    
    elif opcion == 5: 
        if bateria_laser >= 10: 
            daño = 80
            bateria_laser -= 10
            vida_jugador -= daño_alien
            print("Ataque critico")
        else: 
            daño = 10
            print("Ataque debil")
            vida_alien -= daño

    else: 
        print("opcion invalida")
        continue 

    #evento aleatorio

    if turno %2 == 0: 
        bateria_laser += 5
        print("Encontraste energia extra (+5 bateria)")

    elif turno % 3 == 0: 
        vida_jugador += 5
        print("Pequeña reparacion automatica (+5 energia)")
    
    elif turno %5 == 0: 
        vida_jugador += 10
        print("Bonus. Recarga grande de bateria (+10)")

    elif turno % 7 == 0: 
        bateria_laser -= 10
        print("Falla. Pierdes energia (-10)")

    else: 
        print("No ocurrio ningun evento este turno")

        # Turno de enemigo
        if vida_alien > 0: 
            daño_alien = 15

            if turno % 4 == 0: 
                daño_ememigo += 5
                print("El enemigo hizo un ataque fuerte")
            vida_jugador -= daño_ememigo
            print(f"El enemigo ataca, -{daño_ememigo}")
            turno += 1 

if vida_alien <= 0: 
    print("====Alien derrotado====")

elif vida_jugador <= 0: 
    print("Has perdido :(")


print ("Juego finalizado")


