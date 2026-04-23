import random

nombres_jugadores = []
vidas_jugadores = []

########################
# HABILIDADES GUERRERO #
########################

habilidad1_guerrero = {
    "Nombre" : "1",
    "Descripcion" : "Inflige daño a un enemigo",
    "Costo" : 3,
    "Daño" : 80,
    "Precisión" : 100
}

habilidad2_guerrero = {
    "Nombre" : "2",
    "Descripcion" : "Inflige mucho daño, pero es más propenso a fallar.",
    "Costo" : 5,
    "Daño" : 150,
    "Precisión" : 85
}

#######################
# HABILIDADES SANADOR #
#######################

habilidad1_sanador = {
    "Nombre" : "Sanación masiva",
    "Descripcion" : "Sana a todos los miembros del equipo.",
    "Costo" : 8,
    "Sanacion" : 100,
    "Precisión" : 100
}

habilidad2_sanador = {
    "Nombre" : "Aumentar defensa",
    "Descripcion" : "Aumenta la defensa de todos los miembros del equipo.",
    "Costo" : 5,
    "Defensa Aumentada" : 30,
    "Precisión" : 100
}

####################
# HABILIDADES MAGO #
####################

habilidad1_mago = {
    "Nombre" : "Aumentar defensa",
    "Descripcion" : "Aumenta la defensa de todos los miembros del equipo.",
    "Costo" : 5,
    "Defensa Aumentada" : 30,
    "Precisión" : 100
}

habilidad2_mago = {
    "Nombre" : "Aumentar defensa",
    "Descripcion" : "Aumenta la defensa de todos los miembros del equipo.",
    "Costo" : 5,
    "Defensa Aumentada" : 30,
    "Precisión" : 100
}

habilidades_guerrero = [habilidad1_guerrero, habilidad2_guerrero]
habilidades_sanador = [habilidad1_sanador, habilidad2_sanador]
habilidades_mago = [habilidad1_mago, habilidad2_mago]

print(habilidades_guerrero[habilidad1_sanador["Sanacion"]])

clase_guerrero = {
    "Clase" : "Guerrero",
    "Vida" : 150,
    "Mana" : 15,
    "Velocidad" : 20,
    "Habilidades" : habilidades_guerrero
}

clase_sanador = {
    "Clase" : "Sanador",
    "Vida" : 70,
    "Mana" : 30,
    "Velocidad" : 30,
    "Habilidades" : habilidades_sanador
}

clase_mago = {
    "Clase" : "Mago",
    "Vida" : 50,
    "Mana" : 60,
    "Velocidad" : 30,
    "Habilidades" : habilidades_mago
}




enemigo = {
    "Habilidades" : ["Ataque en área", "Ataque directo", "Stun", "Ataque fuerte"]
}

jugador1 = ""
jugador2 = ""

jugadores = []

contador_personajes_creados = 0

while contador_personajes_creados < 2 :
    jugador_nuevo = clase_guerrero
    
    print("Escoja su clase: ")

    print("1) Guerrero")
    print("2) Sanador")
    print("3) Tanque")
    print("4) Mago")
    print("5) Asesino")

    index_clase = int (input())

    index_clase -= 1   # Esta resta es para que coincida el input con el index de la lista.

    match index_clase :
        case 0 :
            if jugador1 == clase_guerrero :
                print("Ya se ha escogido la clase Guerrero. Escoja otra.")
                continue

            jugador_nuevo = clase_guerrero
            contador_personajes_creados += 1
        case 1 :
            if jugador1 == clase_sanador :
                print("Ya se ha escogido la clase Sanador. Escoja otra.")
                continue

            jugador_nuevo = clase_sanador
            contador_personajes_creados += 1
        case 2 : 
            if jugador1 == clase_mago :
                print("Ya se ha escogido la clase Mago. Escoja otra.")
                continue

            jugador_nuevo = clase_mago
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
            print("Escoja una opción correcta.")

    
    if contador_personajes_creados == 1 :
        jugador1 = jugador_nuevo
        jugadores.append(jugador1)
    elif contador_personajes_creados == 2 :
        jugador2 = jugador_nuevo
        jugadores.append(jugador2)

for jugador in jugadores :
    print(jugador)
#numero_aleatorio = random.randint(int (velocidad_asesino * 0.8), int (velocidad_asesino * 1.2))

#print(numero_aleatorio)

