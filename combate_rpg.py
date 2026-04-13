import time
try:
    
###### DATOS JUGADOR #########
    nombre_jugador = input("Ingresa tu nombre: ")
    ataque_jugador = 50
    vida_jugador = 100
###### DATOS ENEMIGO #########
    nombre_enemigo = "Minina, la cazadora definitiva"
    ataque_enemigo = 30
    vida_minina = 100

    print(f"Bienvenidos al la arena de combate {nombre_jugador}.")
    time.sleep(2)
    print(f"{nombre_enemigo} acaba de aparecer en la arena de combate.")
    time.sleep(2)
###### BUCLE DE COMBATE #########
    while vida_jugador > 0 and vida_minina > 0:
        print(f"La vida actual de {nombre_jugador} es {vida_jugador}. \nLa vida actual de {nombre_enemigo} es {vida_minina} \n¿Que Haras? \n1) ATACAR \n2) NO HACER NADA")
        
        eleccion_jugador = int(input("Elige que harás: "))
        if eleccion_jugador == 1:
            print(f"Haz golpeado con unos poderosos {ataque_jugador} contra la barra de vida de {nombre_enemigo}.")
            time.sleep(2)
            vida_minina -= ataque_jugador
                                   
        else:
                                   print(f"{nombre_enemigo} aprovecha su oportunidad para atacar su presa definitiva {nombre_jugador}")
                                   time.sleep(2)
        if vida_minina > 0:
                                    print(f"Estas apunto de ser atacado brutalmente por {nombre_enemigo}")
                                    time.sleep(2)
                                    vida_jugador -= ataque_enemigo
                                    
    if vida_jugador > 0:
        print(f"{nombre_jugador} derrotado a {nombre_enemigo}, felicidades.")
        
    else:
        print(f"{nombre_enemigo} esta devorando brutalmente a {nombre_jugador}")
        
except ValueError:
    print("Solo puedes poner numeros animal, no letras.")
                            
                                   
                    
                        
