opcion_jugador1 = ""
opcion_jugador2 = ""

marcador_jugador1 = 0
marcador_jugador2 = 0

print("*********INICIO CACHIPUNCITO*********")
print("*********Elija entre piedra papel o tijeras*********")

while marcador_jugador1 < 3 and marcador_jugador2 < 3 :
    opcion_jugador1 = input("J1 - ingrese su opción")
    opcion_jugador2 = input("J2 - ingrese su opción")

    #EMpatan las PIEDRAS
    if opcion_jugador1 == "piedra" and opcion_jugador2 == "piedra" :
        print("Empate")

    #j1 gana usando Piedra
    elif opcion_jugador1 == "piedra" and opcion_jugador2 == "tijeras" :
        print("El J1 obtiene 1 victoria")
        marcador_jugador1 = marcador_jugador1 + 1
        print(f"El J1 tiene {marcador_jugador1}")

    #j2 Pierde piedra
    elif opcion_jugador1 == "piedra" and opcion_jugador2 == "papel" :
        print("El J2 obtiene 1 victoria")
        marcador_jugador2 = marcador_jugador2 + 1
        print(f"El J2 tiene {marcador_jugador2}")

    #EMpatan las PIEDRAS
    elif opcion_jugador1 == "papel" and opcion_jugador2 == "papel" :
        print("Empate")

    #j1 gana usando papel
    elif opcion_jugador1 == "papel" and opcion_jugador2 == "piedra" :
        print("El J1 obtiene 1 victoria")
        marcador_jugador1 = marcador_jugador1 + 1
        print(f"El J1 tiene {marcador_jugador1}")

    #j2 Pierde papel
    elif opcion_jugador1 == "papel" and opcion_jugador2 == "tijeras" :
        print("El J2 obtiene 1 victoria")
        marcador_jugador2 = marcador_jugador2 + 1
        print(f"El J2 tiene {marcador_jugador2}")


    #EMpatan las tijeras
    elif opcion_jugador1 == "tijeras" and opcion_jugador2 == "tijeras" :
        print("Empate")

    #j1 gana usando tijeras
    elif opcion_jugador1 == "tijeras" and opcion_jugador2 == "papel" :
        print("El J1 obtiene 1 victoria")
        marcador_jugador1 = marcador_jugador1 + 1
        print(f"El J1 tiene {marcador_jugador1}")

    #j2 Pierde tijeras
    elif opcion_jugador1 == "tijeras" and opcion_jugador2 == "piedra" :
        print("El J2 obtiene 1 victoria")
        marcador_jugador2 = marcador_jugador2 + 1
        print(f"El J2 tiene {marcador_jugador2}")

    
if marcador_jugador1 > marcador_jugador2 :
    print(f"FIN DEL JUEGO EL GANADOR ES j1 con {marcador_jugador1}")
else:
    print(f"FIN DEL JUEGO EL GANADOR ES j2 con {marcador_jugador2}")

print("FIN DEL JUEGO c:")