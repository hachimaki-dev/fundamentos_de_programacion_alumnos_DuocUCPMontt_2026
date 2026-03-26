OPCIONES = [1,2,3]
TURNO_PRIMER_JUGADOR = True
TURNO_SEGUNDO_JUGADOR = True
CONTADOR_PRIMER_JUGADOR = 0
CONTADOR_SEGUNDO_JUGADOR = 0
EJECUTANDO_JUEGO = True

def mostrar_opciones(numero_del_jugador):
    if numero_del_jugador == 1:
        print("Turno del primer jugador")
    elif numero_del_jugador == 2:
        print("Turno del segundo jugador")

    print("1.piedra")
    print("2.papel")
    print("3.tijera")

input("Bienvenido al multiplayer de piedra papel y tijera PRESIONA ENTER")

while EJECUTANDO_JUEGO :
    
    mostrar_opciones(1)

    ELECCION_PRIMER_JUGADOR = int(input(""))     

    mostrar_opciones(2)

    ELECCION_SEGUNDO_JUGADOR = int(input(""))

    if ELECCION_PRIMER_JUGADOR == ELECCION_SEGUNDO_JUGADOR :
        print("EMPATE")
                
    elif(ELECCION_PRIMER_JUGADOR == 3 and ELECCION_SEGUNDO_JUGADOR == 2) or \
        (ELECCION_PRIMER_JUGADOR == 2 and ELECCION_SEGUNDO_JUGADOR == 1) or \
        (ELECCION_PRIMER_JUGADOR == 1 and ELECCION_SEGUNDO_JUGADOR == 3) :
                    
        CONTADOR_PRIMER_JUGADOR = CONTADOR_PRIMER_JUGADOR + 1
        print(f"El jugador 1 a sumado {CONTADOR_PRIMER_JUGADOR} punto ")
    else :
        CONTADOR_SEGUNDO_JUGADOR = CONTADOR_SEGUNDO_JUGADOR + 1
        print(f"El jugador 2 a sumado {CONTADOR_SEGUNDO_JUGADOR} punto ")



    if CONTADOR_PRIMER_JUGADOR == 3 :
        EJECUTANDO_JUEGO = False
        print("HA GANADO EL JUGADOR 11111")
    if CONTADOR_SEGUNDO_JUGADOR == 3 :
        EJECUTANDO_JUEGO = False
        print("HA GANADO EL JUGADOR 22222")
                                                            


            