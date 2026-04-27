import random

CANTIDAD_MINIMA_DE_JUGADORES = 2
CANTIDAD_MAXIMA_DE_JUGADORES = 3

FUNCION_HABILIDAD_ATACAR = "Atacar"
FUNCION_HABILIDAD_SANAR = "Sanar"
FUNCION_HABILIDAD_ATURDIR = "Aturdir"
FUNCION_HABILIDAD_BENDECIR_ARMA_PROPIA = "Bendecir Arma Propia"

OBJETIVO_HABILIDAD_OPONENTE = "Oponente"
OBJETIVO_HABILIDAD_OPONENTES = "Oponentes"
OBJETIVO_HABILIDAD_MIEMBROS = "Miembros"

PRECISION_ATAQUE = 95
CRITICO_ATAQUE = 95

########################
# HABILIDADES GUERRERO #
########################

habilidad_barbaro_1 = {
    "Nombre" : "Golpe contundente",
    "Descripcion" : "Inflige daño a un enemigo.",
    "Costo" : 3,
    "Daño" : 65,
    "Precision" : 95,
    "Critico" : 5,
    "Ignora_Defensa" : False,
    "Funcion" : FUNCION_HABILIDAD_ATACAR,
    "Objetivo" : OBJETIVO_HABILIDAD_OPONENTE
}

habilidad_barbaro_2 = {
    "Nombre" : "Ataque con frenesí",
    "Descripcion" : "Inflige mucho daño, pero es más propenso a fallar.",
    "Costo" : 5,
    "Daño" : 115,
    "Precision" : 75,
    "Critico" : 5,
    "Ignora_Defensa" : False,
    "Funcion" : FUNCION_HABILIDAD_ATACAR,
    "Objetivo" : OBJETIVO_HABILIDAD_OPONENTE
}

#########################
# HABILIDADES SACERDOTE #
#########################

habilidad_paladin_1 = {
    "Nombre" : "Sanación masiva",
    "Descripcion" : "Sana a todos los miembros del equipo.",
    "Costo" : 8,
    "Sanacion" : 38,
    "Precision" : 100,
    "Critico" : 5,
    "Funcion" : FUNCION_HABILIDAD_SANAR,
    "Objetivo" : OBJETIVO_HABILIDAD_MIEMBROS
}

habilidad_paladin_2 = {
    "Nombre" : "Bendición vengadora",
    "Descripcion" : "Bendice tu arma con luz sagrada, aumentando el daño de tu siguiente ataque.",
    "Costo" : 1,
    "Daño_Aumentado" : 60,
    "Precision" : 100,
    "Critico" : 0,
    "Funcion" : FUNCION_HABILIDAD_BENDECIR_ARMA_PROPIA,
    "Objetivo" : OBJETIVO_HABILIDAD_MIEMBROS
}

####################
# HABILIDADES MAGO #
####################

habilidad_mago_1 = {
    "Nombre" : "Bola de fuego",
    "Descripcion" : "Inflige mucho daño mágico a un enemigo. Ignora la defensa del enemigo.",
    "Costo" : 10,
    "Daño" : 100,
    "Precision" : 95,
    "Critico" : 5,
    "Ignora_Defensa" : True,
    "Funcion" : FUNCION_HABILIDAD_ATACAR,
    "Objetivo" : OBJETIVO_HABILIDAD_OPONENTE
}

habilidad_mago_2 = {
    "Nombre" : "Rayo",
    "Descripcion" : "Inflige daño mágico a un enemigo y casi siempre es crítico. Ignora la defensa del enemigo.",
    "Costo" : 7,
    "Daño" : 65,
    "Precision" : 95,
    "Critico" : 70,
    "Ignora_Defensa" : True,
    "Funcion" : FUNCION_HABILIDAD_ATACAR,
    "Objetivo" : OBJETIVO_HABILIDAD_OPONENTE
}

habilidades_barbaro = [habilidad_barbaro_1, habilidad_barbaro_2]
habilidades_paladin = [habilidad_paladin_1, habilidad_paladin_2]
habilidades_mago = [habilidad_mago_1, habilidad_mago_2]

##################
# CLASE GUERRERO #
##################

clase_barbaro = {
    "Clase" : "Bárbaro",
    "Vida_Maxima" : 135,
    "Vida_Actual" : 135,
    "Mana_Maximo" : 16,
    "Mana_Actual" : 16,
    "Ataque" : 35,
    "Defensa" : 12,
    "Velocidad_Base" : 30,
    "Velocidad_Turno" : 30,
    "Esta_Aturdido" : False,
    "Ha_Sido_Aturdido_Este_Turno" : False,
    "Habilidades" : habilidades_barbaro,
    "Index_Habilidad_Seleccionada" : 0,
    "Daño_Aumentado_Arma" : 0,
    "Arma_Bendecida" : False,
    "Se_Ha_Escogido" : False,
    "Ataca" : False,
    "Usa_Habilidad" : False
}

#################
# CLASE PALADIN #
#################

clase_paladin = {
    "Clase" : "Paladín",
    "Vida_Maxima" : 110,
    "Vida_Actual" : 110,
    "Mana_Maximo" : 28,
    "Mana_Actual" : 28,
    "Ataque" : 23,
    "Defensa" : 15,
    "Velocidad_Base" : 20,
    "Velocidad_Turno" : 20,
    "Esta_Aturdido" : False,
    "Ha_Sido_Aturdido_Este_Turno" : False,
    "Habilidades" : habilidades_paladin,
    "Index_Habilidad_Seleccionada" : 0,
    "Daño_Aumentado_Arma" : 0,
    "Arma_Bendecida" : False,
    "Se_Ha_Escogido" : False,
    "Ataca" : False,
    "Usa_Habilidad" : False
}

##############
# CLASE MAGO #
##############

clase_mago = {
    "Clase" : "Mago",
    "Vida_Maxima" : 90,
    "Vida_Actual" : 90,
    "Mana_Maximo" : 60,
    "Mana_Actual" : 60,
    "Ataque" : 7,
    "Defensa" : 8,
    "Velocidad_Base" : 25,
    "Velocidad_Turno" : 25,
    "Esta_Aturdido" : False,
    "Ha_Sido_Aturdido_Este_Turno" : False,
    "Habilidades" : habilidades_mago,
    "Index_Habilidad_Seleccionada" : 0,
    "Daño_Aumentado_Arma" : 0,
    "Arma_Bendecida" : False,
    "Se_Ha_Escogido" : False,
    "Ataca" : False,
    "Usa_Habilidad" : False
}

clases = [clase_barbaro, clase_paladin, clase_mago]

###########
# ENEMIGO #
###########

habilidad_enemigo_1 = {
    "Nombre" : "Embestida colosal",
    "Costo" : 0,
    "Daño" : 25,
    "Precision" : 95,
    "Critico" : 5,
    "Ignora_Defensa" : False,
    "Ataca a todos" : True,
    "Aturde" : False,
    "Funcion" : FUNCION_HABILIDAD_ATACAR,
    "Objetivo" : OBJETIVO_HABILIDAD_OPONENTES
}

habilidad_enemigo_2 = {
    "Nombre" : "Apretón",
    "Costo" : 0,
    "Daño" : 45,
    "Precision" : 100,
    "Critico" : 5,
    "Ignora_Defensa" : False,
    "Ataca a todos" : False,
    "Aturde" : False,
    "Funcion" : FUNCION_HABILIDAD_ATACAR,
    "Objetivo" : OBJETIVO_HABILIDAD_OPONENTE
}

habilidad_enemigo_3 = {
    "Nombre" : "Pisotón",
    "Costo" : 0,
    "Daño" : 0,
    "Precision" : 35,
    "Critico" : 0,
    "Ataca a todos" : True,
    "Aturde" : True,
    "Funcion" : FUNCION_HABILIDAD_ATURDIR,
    "Objetivo" : OBJETIVO_HABILIDAD_OPONENTES
}

habilidades_enemigo = [habilidad_enemigo_1, habilidad_enemigo_1, habilidad_enemigo_2, habilidad_enemigo_3]

enemigo = {
    "Clase" : "Gigante",
    "Vida_Maxima" : 350,
    "Vida_Actual" : 350,
    "Mana_Maximo" : 60,
    "Mana_Actual" : 60,
    "Ataque" : 4,
    "Defensa" : 10,
    "Velocidad_Base" : 25,
    "Velocidad_Turno" : 25,
    "Esta_Aturdido" : False,
    "Ha_Sido_Aturdido_Este_Turno" : False,
    "Habilidades" : habilidades_enemigo,
    "Index_Habilidad_Seleccionada" : 0,
    "Ataca" : False,
    "Usa_Habilidad" : True
}

jugadores = []

while True :
    cantidad_jugadores = int (input(f"¿Cuántas clases quiere jugar? (Mínimo {CANTIDAD_MINIMA_DE_JUGADORES}, máximo {CANTIDAD_MAXIMA_DE_JUGADORES}) "))

    if cantidad_jugadores == CANTIDAD_MINIMA_DE_JUGADORES or cantidad_jugadores == CANTIDAD_MAXIMA_DE_JUGADORES :
        break
    else :
        print("\nError. Escoja entre 2 a 3 clases.\n")

while len(jugadores) < cantidad_jugadores :
    match len(jugadores) :
        case 0 :
            print("\nEscoja la primera clase: ")
        case 1 :
            print("\nEscoja la segunda clase: ")
        case 2 :
            print("\nEscoja la tercera clase: ")

    print("1) Bárbaro")
    print("2) Paladín")
    print("3) Mago")
   # print("0) Ver descripción de las clases.")
   # print("4) Tanque")
    #print("5) Asesino")

    index_clase = int (input())

    index_clase -= 1   # Esta resta es para que coincida el input con el index de la lista.

    match index_clase :
        case 0 :
            if clase_barbaro["Se_Ha_Escogido"] :
                print("\nYa se ha escogido la clase Bárbaro. Escoja otra.")
                continue

            clase_barbaro["Se_Ha_Escogido"] = True
            jugadores.append(clase_barbaro)
        case 1 :
            if clase_paladin["Se_Ha_Escogido"] :
                print("\nYa se ha escogido la clase paladín. Escoja otra.")
                continue

            clase_paladin["Se_Ha_Escogido"] = True
            jugadores.append(clase_paladin)
        case 2 : 
            if clase_mago["Se_Ha_Escogido"] :
                print("\nYa se ha escogido la clase Mago. Escoja otra.")
                continue

            clase_mago["Se_Ha_Escogido"] = True
            jugadores.append(clase_mago)
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
            print(f"\nError. Escoja una opción entre 1 y {len(clases)}.")
            continue

enemigo["Vida_Maxima"]

has_ganado = False
has_perdido = False
ha_terminado_el_combate = False

print("\n*******************************")
print("*** HA COMENZADO EL COMBATE ***")
print("*******************************")

while not ha_terminado_el_combate:
    print("")

    # Se resetean algunos booleanos.
    for i in range(len(jugadores)) :
        jugadores[i]["Ataca"] = False
        jugadores[i]["Usa_Habilidad"] = False
        jugadores[i]["Ha_Sido_Aturdido_Este_Turno"] = False

        if jugadores[i]["Vida_Actual"] <= 0 :
            jugadores[i]["Esta_Aturdido"] = False

    # Se muestra la info de cada jugador.
    for i in range(len(jugadores)) :
        print(f"-+- {jugadores[i]["Clase"]} -+-")
        print(f"Vida: {jugadores[i]["Vida_Actual"]}/{jugadores[i]["Vida_Maxima"]}")
        print(f"Maná: {jugadores[i]["Mana_Actual"]}/{jugadores[i]["Mana_Maximo"]}")
        if jugadores[i]["Vida_Actual"] <= 0 :
            print("[MUERTO]")
        else :
            if jugadores[i]["Arma_Bendecida"] :
                print("+ Arma bendecida +")
            if jugadores[i]["Esta_Aturdido"] :
                print("* Aturdido *")
        print("")
        
    print(f"*** {enemigo["Clase"]} ***")
    print(f"Vida: {enemigo["Vida_Actual"]}/{enemigo["Vida_Maxima"]}")

    index_jugador_actual = 0

    while index_jugador_actual < len(jugadores) :
        jugador_actual = jugadores[index_jugador_actual]
        jugador_actual["Ataca"] = False
        jugador_actual["Usa_Habilidad"] = False

        termina_turno = False

        while not termina_turno :
            if jugador_actual["Vida_Actual"] <= 0 :
                index_jugador_actual += 1
                break

            print(f"\n--- Turno de {jugador_actual["Clase"]} ---")
            print(f"Vida: {jugador_actual["Vida_Actual"]}/{jugador_actual["Vida_Maxima"]}")
            print(f"Maná: {jugador_actual["Mana_Actual"]}/{jugador_actual["Mana_Maximo"]}")
            if jugador_actual["Arma_Bendecida"] :
                print("+ Arma bendecida +")
            if jugador_actual["Esta_Aturdido"] :
                print("* Aturdido *")
                
            if jugador_actual["Esta_Aturdido"] :
                print("")
                print("1) Pasar turno.")
            else :
                print("")
                print("1) Atacar.")
                print("2) Ver habilidades.")

            if index_jugador_actual > 0 :
                print("0) Volver al jugador anterior.")
            
            opcion_jugador = int (input(""))

            if jugador_actual["Esta_Aturdido"] :
                match opcion_jugador :
                    case 1 :
                        index_jugador_actual += 1
                        termina_turno = True
                    case 0 :
                        if index_jugador_actual > 0 :
                            index_jugador_actual -= 1
                            termina_turno = True
                            break
                        else :
                            print("\nError. Seleccione una opción correcta.")
                    case _ :
                        print("\nError. Seleccione una opción correcta.")
            else :  
                match opcion_jugador :
                    case 1 :
                        print(f"\n{jugador_actual["Clase"]} se prepara para atacar...")
                        jugador_actual["Ataca"] = True
                        index_jugador_actual += 1
                        termina_turno = True
                    case 2 : # Escogiendo una habilidad
                        if jugador_actual["Esta_Aturdido"] :
                            index_jugador_actual += 1
                            termina_turno = True
                        while True :
                            print("\nHabilidades:")

                            for j in range(len(jugador_actual["Habilidades"])) :
                                print(f"{j+1}) {jugador_actual["Habilidades"][j]["Nombre"]} (Costo -> {jugador_actual["Habilidades"][j]["Costo"]})")
                                print(f"{jugador_actual["Habilidades"][j]["Descripcion"]}")
                                print("")
                            
                            print("0) Volver.")

                            opcion_habilidad = int (input(""))
                            opcion_habilidad -= 1

                            if opcion_habilidad >= 0 and opcion_habilidad < len(jugador_actual["Habilidades"]) :
                                if jugador_actual["Habilidades"][opcion_habilidad]["Costo"] > jugador_actual["Mana_Actual"] :
                                    print("\nNo tienes maná suficiente.")
                                else :
                                    print(f"\n{jugador_actual["Clase"]} se prepara para usar '{jugador_actual["Habilidades"][opcion_habilidad]["Nombre"]}'...")
                                    jugador_actual["Usa_Habilidad"] = True
                                    jugador_actual["Index_Habilidad_Seleccionada"] = opcion_habilidad

                                    index_jugador_actual += 1
                                    termina_turno = True
                                    break
                            elif opcion_habilidad == -1 :
                                break
                            else :
                                print("\nError. Seleccione una habilidad.")
                    case 0 :
                        if index_jugador_actual > 0 :
                            index_jugador_actual -= 1
                            termina_turno = True
                            break
                        else :
                            print("\nError. Seleccione una opción correcta.")
                    case _ :
                        print("\nError. Seleccione una opción correcta.")

    print("\nX ============== X")
    print("X    Preparando  X")
    print("X      orden     X")
    print("X       de       X")
    print("X     turnos     X")
    print("X ============== X")
    print("")
    input("---> ENTER ")

    #
    # Aquí ya están listos los turnos. Ahora el enemigo escoge una habilidad aleatoria.
    #

    index_habilidad_aleatoria = random.randint(0, len(habilidades_enemigo) - 1)
    enemigo["Index_Habilidad_Seleccionada"] = index_habilidad_aleatoria

    #
    # Creando las prioridades de turno en base a la velocidad de cada personaje.
    #

    personajes = []

    for i in range(len(jugadores)) :
        personajes.append(jugadores[i])

    personajes.append(enemigo)

    for i in range(len(personajes)) :
        velocidad_turno = random.randint(int (personajes[i]["Velocidad_Base"] * 0.75), int (personajes[i]["Velocidad_Base"] * 1.25)) 
        personajes[i]["Velocidad_Turno"] = velocidad_turno

    personajes_ordenados = sorted(personajes, key=lambda x: x["Velocidad_Turno"], reverse=True)
    
    #
    # Cada personaje hace su acción (atacar o usar habilidad).
    #

    for i in range(len(personajes_ordenados)) : 
        personaje = personajes_ordenados[i]

        if personaje["Ha_Sido_Aturdido_Este_Turno"] :
            print(f"\n{personaje["Clase"]} está aturdido. No puede usar su turno.")
            input("---> ENTER ")
            continue

        if personaje["Vida_Actual"] <= 0 :
            continue
        
        if personaje["Ataca"] : ### AQUÍ ATACA ###
            if personaje != enemigo :
                print(f"\n{personaje["Clase"]} ataca a {enemigo["Clase"]}...")
                input("---> ENTER ")

                falla_ataque = PRECISION_ATAQUE <= random.randint(0, 100) 

                if falla_ataque :
                    print(f"Pero {enemigo["Clase"]} ha esquivado el ataque.")
                    input("---> ENTER ")
                else :
                    danio_total = personaje["Ataque"]

                    if personaje["Arma_Bendecida"] == True :
                        print(f"¡El arma de {personaje["Clase"]} empieza a brillar con una luz cegadora!")
                        input("---> ENTER ")

                        danio_aumentado_por_bendicion = personaje["Daño_Aumentado_Arma"]
                        danio_total += personaje["Daño_Aumentado_Arma"]

                    es_critico = CRITICO_ATAQUE <= random.randint(0, 100)

                    if es_critico :
                        danio_total = (int) (danio_total * 1.5)
                        print(f"¡Es un ataque crítico!")
                        input("---> ENTER ")

                    danio_total = (int) (danio_total * random.uniform(0.9, 1.1))

                    danio_total -= enemigo["Defensa"]

                    if danio_total < 0 :
                        danio_total = 0

                    enemigo["Vida_Actual"] -= danio_total

                    print(f"{enemigo["Clase"]} ha recibido {danio_total} de daño.")
                    input("---> ENTER ")

                    if personaje["Arma_Bendecida"] == True :
                        personaje["Arma_Bendecida"] = False
                        personaje["Daño_Aumentado_Arma"] -= danio_aumentado_por_bendicion
                        print("La luz del arma se apagó tras el ataque.")
                        input("---> ENTER ")

                    if enemigo["Vida_Actual"] <= 0 :
                        print(f"{enemigo["Clase"]} ha muerto.")
                        input("---> ENTER ")

                        enemigo["Vida_Actual"] = 0
                        has_ganado = True
                        ha_terminado_el_combate = True
                        break
                
        elif personaje["Usa_Habilidad"] : ### AQUÍ SE USA UNA HABILIDAD ###
            habilidad_usada = personaje["Habilidades"][personaje["Index_Habilidad_Seleccionada"]]

            personaje["Mana_Actual"] -= habilidad_usada["Costo"]

            miembros = []
            oponentes = []

            if personaje == enemigo :
                miembros.append(enemigo)
                
                for jugador in jugadores :
                    if jugador["Vida_Actual"] <= 0 :
                        continue

                    oponentes.append(jugador)
            else :
                oponentes.append(enemigo)
                
                for jugador in jugadores :
                    if jugador["Vida_Actual"] <= 0 :
                        continue

                    miembros.append(jugador)

            if habilidad_usada["Funcion"] == FUNCION_HABILIDAD_ATACAR :
                if habilidad_usada["Objetivo"] == OBJETIVO_HABILIDAD_OPONENTE :
                    oponente_aleatorio = oponentes[random.randint(0, len(oponentes) - 1)]

                    print(f"\n{personaje["Clase"]} ha usado '{habilidad_usada["Nombre"]}' contra {oponente_aleatorio["Clase"]}...")
                    input("---> ENTER ")
                    
                    falla_habilidad = habilidad_usada["Precision"] <= random.randint(0, 100) and habilidad_usada["Precision"] != 0

                    if falla_habilidad :
                        print(f"Pero {oponente_aleatorio["Clase"]} lo ha esquivado.")
                        input("---> ENTER ")

                    else :
                        danio_total = habilidad_usada["Daño"]

                        es_critico = random.randint(0, 100) <= habilidad_usada["Critico"] and habilidad_usada["Critico"] != 0

                        if es_critico :
                            danio_total = (int) (danio_total * 1.5)
                            print(f"¡{habilidad_usada["Nombre"]} es crítico!")
                            input("---> ENTER ")

                        danio_total = (int) (danio_total * random.uniform(0.9, 1.1))

                        if not habilidad_usada["Ignora_Defensa"] :
                            danio_total -= oponente_aleatorio["Defensa"]
                        
                        if danio_total < 0 :
                            danio_total = 0

                        oponente_aleatorio["Vida_Actual"] -= danio_total
                        print(f"{oponente_aleatorio["Clase"]} ha recibido {danio_total} de daño.")
                        input("---> ENTER ")

                        if oponente_aleatorio["Vida_Actual"] <= 0 :
                            print(f"{oponente_aleatorio["Clase"]} ha muerto.")
                            input("---> ENTER ")
                            
                            oponente_aleatorio["Vida_Actual"] = 0

                            if oponente_aleatorio == enemigo :
                                has_ganado = True
                                ha_terminado_el_combate = True
                                break
                            else :
                                contador_jugadores_muertos = 0

                                for jugador in jugadores :
                                    if jugador["Vida_Actual"] > 0 :
                                        break
                                    else :
                                        contador_jugadores_muertos += 1

                                if contador_jugadores_muertos == len(jugadores) :
                                    has_perdido = True
                                    ha_terminado_el_combate = True
                                    break

                elif habilidad_usada["Objetivo"] == OBJETIVO_HABILIDAD_OPONENTES :
                    print(f"\n{personaje["Clase"]} ha usado '{habilidad_usada["Nombre"]}' contra todo el equipo rival...")
                    input("---> ENTER ")

                    for i in range(len(oponentes)) :
                        oponente = oponentes[i]
                        falla_habilidad = habilidad_usada["Precision"] <= random.randint(0, 100) and habilidad_usada["Precision"] != 0

                        if falla_habilidad :
                            print(f"Pero {oponente["Clase"]} lo ha esquivado.")
                            input("---> ENTER ")
                        else :
                            danio_total = habilidad_usada["Daño"]

                            es_critico = random.randint(0, 100) <= habilidad_usada["Critico"] and habilidad_usada["Critico"] != 0

                            if es_critico :
                                danio_total = (int) (danio_total * 1.5)
                                print(f"¡{habilidad_usada["Nombre"]} es crítico!")
                                input("---> ENTER ")

                            danio_total = (int) (danio_total * random.uniform(0.9, 1.1))

                            if not habilidad_usada["Ignora_Defensa"] :
                                danio_total -= oponente["Defensa"]
                                
                            if danio_total < 0 :
                                danio_total = 0

                            oponente["Vida_Actual"] -= danio_total
                            print(f"{oponente["Clase"]} ha recibido {danio_total} de daño.")
                            input("---> ENTER ")

                            if oponente["Vida_Actual"] <= 0 :
                                print(f"{oponente["Clase"]} ha muerto.")
                                input("---> ENTER ")
                                
                                oponente["Vida_Actual"] = 0

                                if oponente == enemigo :
                                    has_ganado = True
                                    ha_terminado_el_combate = True
                                    break
                                else :
                                    contador_jugadores_muertos = 0

                                    for jugador in jugadores :
                                        if jugador["Vida_Actual"] > 0 :
                                            break
                                        else :
                                            contador_jugadores_muertos += 1

                                    if contador_jugadores_muertos == len(jugadores) :
                                        has_perdido = True
                                        ha_terminado_el_combate = True
                                        break
                    
            elif habilidad_usada["Funcion"] == FUNCION_HABILIDAD_SANAR :
                if habilidad_usada["Objetivo"] == OBJETIVO_HABILIDAD_MIEMBROS :
                    print(f"\n{personaje["Clase"]} ha usado '{habilidad_usada["Nombre"]}' hacia todo su equipo...")
                    input("---> ENTER ")

                    for i in range(len(miembros)) :
                        miembro = miembros[i]

                        if miembro["Vida_Actual"] <= 0 :
                            continue

                        sanacion_total = habilidad_usada["Sanacion"]

                        es_critico = random.randint(0, 100) <= habilidad_usada["Critico"] and habilidad_usada["Critico"] != 0

                        if es_critico :
                            sanacion_total = (int) (sanacion_total * 1.5)
                            print(f"¡{habilidad_usada["Nombre"]} es crítico!")
                            input("---> ENTER ")

                        sanacion_total = (int) (sanacion_total * random.uniform(0.9, 1.1))

                        miembro["Vida_Actual"] += sanacion_total
                        print(f"{miembro["Clase"]} ha recuperado {sanacion_total} de vida.")
                        input("---> ENTER ")

                        if miembro["Vida_Actual"] > miembro["Vida_Maxima"] :
                            miembro["Vida_Actual"] = miembro["Vida_Maxima"]

            elif habilidad_usada["Funcion"] == FUNCION_HABILIDAD_BENDECIR_ARMA_PROPIA :
                if personaje["Arma_Bendecida"] == False :
                    personaje["Arma_Bendecida"] = True
                    personaje["Daño_Aumentado_Arma"] += habilidad_usada["Daño_Aumentado"]

                    print(f"\n{personaje["Clase"]} ha bendecido su arma.")
                    input("---> ENTER")
                else :
                    print(f"\n{personaje["Clase"]} ya tiene su arma bendecida.")
                    input("---> ENTER")

            elif habilidad_usada["Funcion"] == FUNCION_HABILIDAD_ATURDIR :
                if habilidad_usada["Objetivo"] == OBJETIVO_HABILIDAD_OPONENTES :
                    print(f"\n{personaje["Clase"]} ha usado '{habilidad_usada["Nombre"]}' contra todo el equipo rival...")
                    input("---> ENTER ")

                    for i in range(len(oponentes)) :
                        oponente = oponentes[i]
                        falla_habilidad = habilidad_usada["Precision"] <= random.randint(0, 100) and habilidad_usada["Precision"] != 0

                        if falla_habilidad :
                            print(f"Pero {oponente["Clase"]} lo ha esquivado.")
                            input("---> ENTER ")
                        else :
                            oponente["Esta_Aturdido"] = True
                            oponente["Ha_Sido_Aturdido_Este_Turno"] = True

                            print(f"{oponente["Clase"]} ha sido aturdido.")
                            input("---> ENTER ")

    for personaje in personajes_ordenados :
        if personaje["Esta_Aturdido"] and not personaje["Ha_Sido_Aturdido_Este_Turno"] :
            personaje["Esta_Aturdido"] = False
            print(f"\n{personaje["Clase"]} ya no está aturdido.")
            input("---> ENTER ")

print("")

if has_ganado :
    print("¡¡¡FELICIDADES, HAS GANADO EL COMBATE!!!")
elif has_perdido :
    print("Has perdido :c ¡Más suerte para la próxima vez!")