import random

nombres_jugadores = []
vidas_jugadores = []

CANTIDAD_MAXIMA_DE_JUGADORES = 2

########################
# HABILIDADES GUERRERO #
########################

habilidad_guerrero_1 = {
    "Nombre" : "Golpe contundente",
    "Descripcion" : "Inflige daño a un enemigo.",
    "Costo" : 3,
    "Daño" : 80,
    "Precision" : 100,
    "Critico" : 5
}

habilidad_guerrero_2 = {
    "Nombre" : "Ataque con frenesí",
    "Descripcion" : "Inflige mucho daño, pero es más propenso a fallar.",
    "Costo" : 5,
    "Daño" : 150,
    "Precision" : 85,
    "Critico" : 5
}

#######################
# HABILIDADES SANADOR #
#######################

habilidad_sanador_1 = {
    "Nombre" : "Sanación masiva",
    "Descripcion" : "Sana a todos los miembros del equipo.",
    "Costo" : 8,
    "Sanacion" : 100,
    "Precision" : 100,
    "Critico" : 5
}

habilidad_sanador_2 = {
    "Nombre" : "Protección",
    
    "Costo" : 5,
    "Defensa_Aumentada" : 30,
    "Precision" : 100,
    "Descripcion" : "Aumenta 30 pts. la defensa de todos los miembros del equipo.",
}

####################
# HABILIDADES MAGO #
####################

habilidad_mago_1 = {
    "Nombre" : "Bola de fuego",
    "Descripcion" : "Inflige mucho daño mágico a un enemigo. Ignora la defensa del enemigo.",
    "Costo" : 10,
    "Daño" : 50,
    "Precision" : 100,
    "Critico" : 10
}

habilidad_mago_2 = {
    "Nombre" : "Rayo",
    "Descripcion" : "Inflige poco daño mágico a un enemigo, pero casi siempre es crítico. Ignora la defensa del enemigo.",
    "Costo" : 7,
    "Daño" : 30,
    "Precision" : 100,
    "Critico" : 50
}

habilidades_guerrero = [habilidad_guerrero_1, habilidad_guerrero_2]
habilidades_sanador = [habilidad_sanador_1, habilidad_sanador_2]
habilidades_mago = [habilidad_mago_1, habilidad_mago_2]

#print(habilidad1_sanador.get("Costo"))
#habilidad1_sanador["Costo"] = 1
#print(habilidad1_sanador.get("Costo"))

print(habilidades_sanador[0]["Costo"])
habilidades_sanador[0]["Costo"] = 1
print(habilidades_sanador[1]["Descripcion"])


clase_guerrero = {
    "Clase" : "Guerrero",
    "Vida" : 150,
    "Mana" : 15,
    "Ataque" : 20,
    "Defensa" : 15,
    "Velocidad" : 30,
    "Habilidades" : habilidades_guerrero
}

clase_sanador = {
    "Clase" : "Sanador",
    "Vida" : 90,
    "Mana" : 30,
    "Ataque" : 2,
    "Defensa" : 6,
    "Velocidad" : 25,
    "Habilidades" : habilidades_sanador
}

clase_mago = {
    "Clase" : "Mago",
    "Vida" : 80,
    "Mana" : 60,
    "Ataque" : 4,
    "Defensa" : 8,
    "Velocidad" : 25,
    "Habilidades" : habilidades_mago
}

clases = [clase_guerrero, clase_sanador]


habilidad_enemigo_1 = {
    "Nombre" : "Ataque en área",
    "Daño" : 30,
    "Precision" : 95,
    "Critico" : 5,
    "Ataca a todos" : True,
    "Aturde" : False
}

habilidad_enemigo_2 = {
    "Nombre" : "Ataque directo",
    "Daño" : 50,
    "Precision" : 100,
    "Critico" : 10,
    "Ataca a todos" : False,
    "Aturde" : False
}

habilidad_enemigo_3 = {
    "Nombre" : "Aturdimiento",
    "Daño" : 0,
    "Precision" : 95,
    "Critico" : 0,
    "Ataca a todos" : False,
    "Aturde" : True
}

habilidades_enemigo = [habilidad_enemigo_1, habilidad_enemigo_2, habilidad_enemigo_3]

enemigo = {
    "Vida" : 800,
    "Mana" : 60,
    "Ataque" : 4,
    "Defensa" : 8,
    "Velocidad" : 30,
    "Habilidades" : habilidades_enemigo 
}


jugadores = []

contador_personajes_creados = 0

while contador_personajes_creados < CANTIDAD_MAXIMA_DE_JUGADORES :

    
    print("Escoja su clase: ")

    print("1) Guerrero")
    print("2) Sanador")
    print("3) Mago")
   # print("4) Tanque")
    #print("5) Asesino")

    index_clase = int (input())

    index_clase -= 1   # Esta resta es para que coincida el input con el index de la lista.

    match index_clase :
        case 0 :
            if len(jugadores) > 0 :
                if jugadores[0] == clase_guerrero :
                    print("Ya se ha escogido la clase Guerrero. Escoja otra.")
                    continue

            jugador_nuevo = clase_guerrero
            contador_personajes_creados += 1
        case 1 :
            if len(jugadores) > 0 :
                if jugadores[0] == clase_sanador :
                    print("Ya se ha escogido la clase Sanador. Escoja otra.")
                    continue

            jugador_nuevo = clase_sanador
            contador_personajes_creados += 1
        case 2 : 
            if len(jugadores) > 0 :
                if jugadores[0] == clase_mago :
                    print("Ya se ha escogido la clase Mago. Escoja otra.")
                    continue

            jugador_nuevo = clase_mago

            print(jugador_nuevo["Ataque"])
            contador_personajes_creados += 1
            '''
        case 3 :
            if jugador1 == clase_tanque :
                print("Ya se ha escogido la clase Tanque. Escoja otra.")
                continue

            jugador_nuevo = clase_tanque
            contador_personajes_creados += 1
        case 4 :
            if jugador1 == clase_asesino :
                print("Ya se ha escogido la clase Asesino. Escoja otra.")
                continue

            jugador_nuevo = clase_asesino
            contador_personajes_creados += 1'''
        case _ :
            print(f"Error. Escoja una opción entre 1 y {len(clases)}.")
            continue
    
    jugadores.append(jugador_nuevo)



has_ganado = False

while True :
    for i in range(len(jugadores)) :
        print(f"Jugador {i+1}:")
        print(f"{jugadores[i]["Clase"]}")
        print(f"Vida: {jugadores[i]["Vida"]}")
        print(f"Maná: {jugadores[i]["Mana"]}")
        print("")
    break


#numero_aleatorio = random.randint(int (velocidad_asesino * 0.8), int (velocidad_asesino * 1.2))

#print(numero_aleatorio)

