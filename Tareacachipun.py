opcion_jugador1 = ""
opcion_jugador2 = ""

marcador_jugador1 = 0
marcador_jugador2 = 0

print("--inicio caxipummm")
print("--elija entre piedra, papel o tijera")
opcion_jugador1 = input("j1 - elija su opcion")
opcion_jugador2 = input("j2 - elija su opcion")

while marcador_jugador1 <3 and marcador_jugador2 <3 :
    if opcion_jugador1 == "piedra" and opcion_jugador2 == "piedra" :
        print("empate")
    elif opcion_jugador1 == "piedra" and opcion_jugador2 == "tijera" :
        print("el j1 tiene 1 victoria")
        marcador_jugador1 = marcador_jugador1 + 1
        print(f"el j1 tiene {marcador_jugador1}")

    elif opcion_jugador1 == "piedra" and opcion_jugador2 == "papel" :
        print("el j2 tiene 1 victoria")
        marcador_jugador2 = marcador_jugador2 + 1
        print(f"el j2 tiene {marcador_jugador2}")

    elif opcion_jugador1 == "papel" and opcion_jugador2 == "papel" :
        print("empate")
    elif opcion_jugador1 == "papel" and opcion_jugador2 == "tijera" :
        print("el j1 tiene 1 victoria")
        marcador_jugador1 = marcador_jugador1 + 1
        print(f"el j1 tiene {marcador_jugador1}")

    elif opcion_jugador1 == "papel" and opcion_jugador2 == "piedra" :
        print("el j1 tiene 1 victoria")
        marcador_jugador1 = marcador_jugador1 + 1
        print(f"el j1 tiene {marcador_jugador1}")

if marcador_jugador1 > marcador_jugador2 :
    print(f"Fin del juego el ganador es j1 con {marcador_jugador1}")       
else :
    print(f"fin del juego el ganador es j2 con {marcador_jugador2}")