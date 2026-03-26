print("Piedra, papel o tijeras")

while marcado_jugador1 < 3 and marcado_jugador2 < 3 :
    opcion_jugador1 = ""
    opcion_jugador2 = ""

    marcado_jugador1 = 0
    marcado_jugador2 = 0

    print("INICIO CACHIPUM!!!!")
    print("ELIJA ENTRE PIEDRAS - PAPEL - TIJERAS")
    opcion_jugador1 = input("J1 elija su opcion :")
    opcion_jugador2 = input("J2 elija su opcion :")


    #EMPATAN LAS PIEDRAS
    if opcion_jugador1 == "piedra" and opcion_jugador2 == "piedra" :
        print("EMPATE")


    #J1 GANA CON PIEDRA
    elif opcion_jugador1 == "piedra" and opcion_jugador2 == "tijeras" :
        print("EL J1 OBTIENE UNA VICTORIA")
        marcado_jugador1 = marcado_jugador1 + 1
        print(f"EL J1 TIENE {marcado_jugador1}")


    #J1 GANA CON PAPEL
    elif opcion_jugador1 == "papel" and opcion_jugador2 == "piedra" :
        print("EL J1 OBTIENE UNA VICTORIA")
        marcado_jugador1 = marcado_jugador1 + 1
        print(f"EL J1 TIENE {marcado_jugador1}")

    #J1 GANA CON TIJERAS
    elif opcion_jugador1 == "tijeras" and opcion_jugador2 == "papel" :
        print("EL J1 OBTIENE UNA VICTORIA")
        marcado_jugador1 = marcado_jugador1 + 1
        print(f"EL J1 TIENE {marcado_jugador1}")



