Piedra = "piedra"
Papel = "papel"
Tijeras = "tijeras"
puntaje_J1 = 0
puntaje_J2 = 0
max_victorias =3
opcion_jugador1 = ""
opcion_jugador1 = ""

while puntaje_J1 != max_victorias and puntaje_J2 != max_victorias:
    

    print("piedra papel o tijeras")
    print(f"Jugador1 tiene {puntaje_J1} puntos y Jugador2 tiene {puntaje_J2}")
    opcion_jugador1 = input("J1 elija su opción ")
    opcion_jugador2 = input("J2 elija su opción ")

    if opcion_jugador1 == "piedra" and opcion_jugador2 == "piedra":
        print("empate")
    elif opcion_jugador1 == "piedra" and opcion_jugador2 == "tijeras":
        print("J1 gana un punto")
        puntaje_J1 = puntaje_J1 +1
    elif opcion_jugador1 == "piedra" and opcion_jugador2 == "papel":
        print("J2 gana un punto")
        puntaje_J2 = puntaje_J2 +1
    
    if opcion_jugador1 == "papel" and opcion_jugador2 == "papel":
        print("empate")
    elif opcion_jugador1 == "papel" and opcion_jugador2 == "piedra":
        print("J1 gana un punto")
        puntaje_J1 = puntaje_J1 +1
    elif opcion_jugador1 == "papel" and opcion_jugador2 == "tijeras":
        print("J2 gana un punto")
        puntaje_J2 = puntaje_J2 +1

    if opcion_jugador1 == "tijeras" and opcion_jugador2 == "tijeras":
        print("empate")
    elif opcion_jugador1 == "tijeras" and opcion_jugador2 == "papel":
        print("J1 gana un punto")
        puntaje_J1 = puntaje_J1 +1
    elif opcion_jugador1 == "tijeras" and opcion_jugador2 == "piedra":
        print("J2 gana un punto")
        puntaje_J2 = puntaje_J2 +1

if puntaje_J1 > puntaje_J2:
    print("el ganador es el jugador 1")
elif puntaje_J1 < puntaje_J2:
    print("el ganador es el jugador 2")
else:
    print("EMPATE")

print(f"puntaje jugador 1 ({puntaje_J1} -- {puntaje_J2})")
print("FIN")
