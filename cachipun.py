opcion_jugador1 = ""
opcion_jugador2 = ""

marcador_jugador1 = 0
marcador_jugador2 = 0
print("-----------------inicio cachipunt --------------------")
print("------------piedra-------papel-----tijera-------------")
while marcador_jugador1 < 3 and marcador_jugador2 < 3 :
 opcion_jugador1 = input("J1 - ingrese su opcion: ")
 opcion_jugador2 = input("J2 - ingrese su opcion: ")

    if opcion_jugador1 == "piedra" and opcion_jugador2 == "piedra" :
        print("empate")

    elif opcion_jugador1 == "piedra" and opcion_jugador2 == "tijera":
        print("J1 - obtiene 1 punto")

    elif opcion_jugador1 == "piedra" and opcion_jugador2 == "papel":
        print("J2 - obtiene 1 punto")

    elif opcion_jugador1 == "papel" and opcion_jugador2 == "tijera":
        print("J2 - obtiene 1 punto")

    elif opcion_jugador1 == "papel" and opcion_jugador2 == "piedra":
        print("J1 - obtiene 1 punto")

    elif opcion_jugador1 == "papel" and opcion_jugador2 == "papel" :
        print("empate")

    elif opcion_jugador1 == "tijera" and opcion_jugador2 == "tijera" :
        print("empate")

    elif opcion_jugador1 == "tijera" and opcion_jugador2 == "papel" :
        print("J1 - obitiene 1 punto")

    elif opcion_jugador1 == "tijera" and opcion_jugador2 == "piedra" :
        print("J2 - obitiene 1 punto")

if marcador_jugador1 > marcador_jugador2:
    print(f"FIN DEL JUEGO EL GANADOR ES J1 CON {marcador_jugador1}")
if marcador_jugador2 > marcador_jugador1:
    print(f"FIN DEL JUEGO EL GANADOR ES J2 CON {marcador_jugador2}")

print("FIN ")