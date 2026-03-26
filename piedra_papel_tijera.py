import getpass


print("########BIENVENIDO#######")
print("###A PIEDRA-PAPEL-TIJERA###")

input("Presiona enter para Jugar ")

print("Opciones: PIEDRA-PAPEL-TIJERA")

puntaje_jugador1= 0
puntaje_jugador2= 0

while puntaje_jugador1 < 3 and puntaje_jugador2 < 3 :
    
    eleccion_jugador1= getpass.getpass("Opcion jugador1").lower()
    eleccion_jugador2= getpass.getpass("Opcion jugador2").lower()
    
    if eleccion_jugador1 == "piedra" and eleccion_jugador2 == "piedra" :
        print("Han empatado, nadie suma puntos")
        print(f"Puntos: J1: {puntaje_jugador1} J2: {puntaje_jugador2}")

    elif eleccion_jugador1 == "piedra" and eleccion_jugador2 == "papel" :
        print("Jugador2 ha ganado")
        puntaje_jugador2= puntaje_jugador2 + 1
        print(f"Puntos: J1: {puntaje_jugador1} J2: {puntaje_jugador2}")

    elif eleccion_jugador1 == "piedra" and eleccion_jugador2 == "tijera" :
        print("Jugador1 ha ganado")
        puntaje_jugador1= puntaje_jugador1 + 1
        print(f"Puntos: J1: {puntaje_jugador1} J2: {puntaje_jugador2}")

    elif eleccion_jugador1 == "papel" and eleccion_jugador2 == "papel" :
        print("Han empatado, nadie suma puntos")
        print(f"Puntos: J1: {puntaje_jugador1} J2: {puntaje_jugador2}")

    elif eleccion_jugador1 == "papel" and eleccion_jugador2 == "piedra" :
        print("Jugador1 ha ganado")
        puntaje_jugador1= puntaje_jugador1 + 1
        print(f"Puntos: J1: {puntaje_jugador1} J2: {puntaje_jugador2}")

    elif eleccion_jugador1 == "papel" and eleccion_jugador2 == "tijera" :
        print("Jugador2 ha ganado")
        puntaje_jugador2= puntaje_jugador2 + 1
        print(f"Puntos: J1: {puntaje_jugador1} J2: {puntaje_jugador2}")

    elif eleccion_jugador1 == "tijera" and eleccion_jugador2 == "tijera" :
        print("Han empatado, nadie suma puntos")
        print(f"Puntos: J1: {puntaje_jugador1} J2: {puntaje_jugador2}")

    elif eleccion_jugador1 == "tijera" and eleccion_jugador2 == "papel" :
        print("Jugador1 ha ganado")
        puntaje_jugador1= puntaje_jugador1 + 1
        print(f"Puntos: J1: {puntaje_jugador1} J2: {puntaje_jugador2}")

    elif eleccion_jugador1 == "tijera" and eleccion_jugador2 == "piedra" :
        print("Jugador2 ha ganado")
        puntaje_jugador2= puntaje_jugador2 + 1
        print(f"Puntos: J1: {puntaje_jugador1} J2: {puntaje_jugador2}")
if puntaje_jugador1 > puntaje_jugador2 :
    print("HAZ GANADO JUGADOR 1")

else :
    print("HAZ GANADO JUGADOR 2")