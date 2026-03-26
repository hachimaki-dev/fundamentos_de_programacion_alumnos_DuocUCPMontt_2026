opcion1 = ""
opcion2 = ""

puntuacion1 = 0
puntuacion2 = 0

print("====Inicio duelo del cachipun====")
puntuacion_alcanzable = int(input("ingrese la puntuacion a alcanzar: "))

while puntuacion1 < puntuacion_alcanzable and puntuacion2 < puntuacion_alcanzable:
    print(f"la puntuacion va {puntuacion1} a {puntuacion2}")
    opcion1=input("Jugador 1-Elija piedra papel o tijeras: ")
    opcion2=input("Jugador 2-Elija piedra papel o tijeras: ")
    if opcion1 == "piedra" and opcion2 == "piedra":
        print("empate")
    elif opcion1 == "piedra" and opcion2 == "papel":
        print("gana jugador 2")
        puntuacion2 += 1
    elif opcion1 == "piedra" and opcion2 == "tijeras":
        print("gana jugador 1")
        puntuacion1 += 1
    elif opcion1 == "papel" and opcion2 == "papel":
        print("empate")
    elif opcion1 == "papel" and opcion2 == "piedra":
        print("gana jugador 1")
        puntuacion1 += 1
    elif opcion1 == "papel" and opcion2 == "tijeras":
        print("gana jugador 2")
        puntuacion2 += 1
    elif opcion1 == "tijeras" and opcion2 == "tijeras":
        print("empate ")
    elif opcion1 == "tijeras" and opcion2 == "papel":
        print("gana jugador 1")
        puntuacion1 += 1
    elif opcion1 == "tijeras" and opcion2 == "piedra":
        print("gana jugador 2")
        puntuacion2 += 1
if puntuacion1 > puntuacion2:
    print("el jugador 1 ha ganado la partida")
else:
    print("el jugador 2 ha ganado la partida")
print("====FIN DEL JUEGO====")