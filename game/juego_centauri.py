print("==========================================")
print("                 CENTAURI                 ")
print("==========================================")

jugador = {"nombre": "",
        "vida": 100,
        "ataque": 10,
        "inventario": [],
        "creditos": 0
}
enemigos = [
    {"nombre": "Androide", "vida": 30, "daño": 10},
    {"nombre": "Night Walker", "vida": 10, "daño": 25},
    {"nombre": "Slasher", "vida": 50, "daño": 30},
    {"nombre": "Blind Whale", "vida": 150, "daño": 40}
]
eliminados = 0
print("\n---- BIENVENIDO A LA ESTACIÓN APHEX 004 ----\n")
jugador["nombre"] = input("Ingrese su nombre: ")

rol_elegido = 0

while rol_elegido < 1 or rol_elegido > 3:

    print(f"\n{jugador['nombre']} | Vida: {jugador['vida']} | Creditos: {jugador['creditos']}")
    print("\n-- Selecciona tu rol en la estación --")
    print("1. Ingeniero")
    print("2. Marin")
    print("3. Médico")

    print("\n---------------------------")
    rol_elegido = int(input("Selecciona (1-2-3): "))
    print("---------------------------")
    if rol_elegido < 1 or rol_elegido > 3:
        print("\n<<<< Opción no válida. Intentalo de nuevo. >>>>\n")

if rol_elegido == 1:
    jugador["clase"] = "Ingeniero"
    jugador["vida"] = 110
    jugador["ataque"] = 25
    jugador["nanobots"] = 3
    jugador["tipo_curacion"] = "Kit de Reparacion"
elif rol_elegido == 2:
    jugador["clase"] = "Marin"
    jugador["vida"] = 150
    jugador["ataque"] = 40
    jugador["nanobots"] = 2
    jugador["tipo_curacion"] = "Adrenalina"
else:
    jugador["clase"] = "Médico"
    jugador["vida"] = 80
    jugador["ataque"] = 20
    jugador["nanobots"] = 5
    jugador["tipo_curacion"] = "Nanobots Medicos"

jugando = True

while jugando and jugador["vida"] > 0:
    print(f"\nHas sido reclutado para que inicies tu primera mision espacial como {jugador['clase']} en la estacion Aphex 004.\n")
    print("Te entregan un equipamiento incial. La misión es catolagada como extracción de emergencia al personal de la estacion...\n")
    print("Pero al llegar a la cabina de mando de la nave, encuentras a todo la tripulación principal muerta, algunos carcomidos desde sus entrañas, otros sin cabezas y demas...\n")
    print("Aterrorizados, tu grupo le reporta a la estación de origen Orión 189 de lo ocurrido en la nave...\n")
    print("Al poco tiempo les dieron la orden estricta a tu grupo de activar el sistema de emergencias si no encontraban al capitán de la nave, esto haria explotar la nave en un lapso de 5 minutos, por lo que solo se activaba si corria el riesgo de que una posible amenaza pueda matar a la raza humana restante...\n")
    print("Pero por el momento se deciden separar para encontrar al capitán, ya que la nave era bastante grande y al conocerla se sentieron en confianza de investigar cada uno por su cuenta y reportar inmediatamente la ubicación de cada uno si tenian problemas, aunque la señal de comunicación de la estación estaba bastante dañada, era muy probable que algo malo pasara...\n")
    accion = 0

    while accion != 1 and accion != 2:
        print("// Al quedar solo, decides entre dos opciones //")
        print("1. Abrir la compuerta de la habitación cercana")
        print("2. Revisar los cuerpos en el suelo\n")

        print("\n-----------------------------")
        accion = int(input("¿Que decides hacer? (1-2): "))
        print("-----------------------------")

        if accion != 1 and accion != 2:
            print("\n<<<< Opción invalida. Elige 1 o 2. >>>>\n")

    if accion == 1:
        print("\n // Te acercas a la compuerta... Hay tres pasillos: A) Sector Médico | B) Motores | C) Laboratorio. //")

        camino = ""

        while camino != "a" and camino != "b" and camino != "c":

            print("\n------------------------")
            camino = input("¿Que camino eliges?: ").lower()
            print("------------------------")

            if camino != "a" and camino != "b" and camino != "c":
                print("\n<<<< Opción invalida. Escriba solo las opciones disponibles (A-B-C) >>>>\n")

        if camino == "a":
            enemigo_actual = enemigos[1]
        elif camino == "b":
            enemigo_actual = enemigos[0]
        else:
            enemigo_actual = enemigos[2]

        print(f"\n¡Desde las sombras emerge un {enemigo_actual['nombre']}!\n")
        
        while enemigo_actual["vida"] > 0 and jugador["vida"] > 0:
            accion_combate = ""
            while accion_combate != "a" and accion_combate != "b":

                print(f"Enemigo: {enemigo_actual['nombre']} | Vida: {enemigo_actual['vida']}\n")
                print(f"Tu vida: {jugador['vida']}")
                
                print("\n---------------------------------")
                accion_combate = input("¿Deseas Atacar o Esquivar (A-B): ").lower()
                print("---------------------------------")

                if accion_combate != "a" and accion_combate != "b":
                    print("\n<< ¡Elige una opcion válida, A o B! >>\n")

            if accion_combate == "a":
                enemigo_actual["vida"] = enemigo_actual["vida"] - jugador["ataque"]
                print(f"\nLe diste! El {enemigo_actual['nombre']} pierde vida.\n")
            elif accion_combate == "b":
                print("\nEsquivaste el golpe, pero no hiciste daño.\n")
            
            if enemigo_actual["vida"] > 0:
                jugador["vida"] = jugador["vida"] - enemigo_actual["daño"]
                print(f"El monstruo te golpea! Pierdes {enemigo_actual['daño']} de vida.")

            curarse = ""

            while curarse != "s" and curarse != "n":
                print(f"Disponibles: {jugador['nanobots']} de {jugador['tipo_curacion']}\n")
                print("\n---------------------------------------------")
                curarse = input("Deseas curarte si (S) o no (N): ").lower()
                print("---------------------------------------------")
                
                if curarse != "s" and curarse != "n":
                    print("\n<<<< Opción invalida. Intente de nuevo. >>>>\n")
                    
            if curarse == "s":
                if jugador["nanobots"] > 0:
                    jugador["vida"] = jugador["vida"] + 40
                    jugador["nanobots"] = jugador["nanobots"] - 1
                    print("\nInyectando nanobots en torrente sanguíneo...")
                    print("Reparando tejidos dañados\n")
                    print(f"Usaste {jugador['tipo_curacion']}. +40 de vida.\n")
                else:
                    print("¡No te quedan suministros médicos!\n")
            if jugador["vida"] <= 0:
                print("Has sido eliminado por el " + enemigo_actual["nombre"])
                print("Tu cuerpo quedara vagando en la Aphex 004...")
                print("--------------------------------------------\n")
                jugando = False

            elif curarse == "n":
                print("¡Sigues en combate!\n")

            elif jugador["vida"] > 0:
                print("Victoria. Recoges suministros del suelo.")
                print("--------------------------------------------\n")
                eliminados = eliminados + 1
                jugador["creditos"] = jugador["creditos"] + 200
                jugador["inventario"].append("Celda de Energia")

    elif accion == 2:
        print("Encuentras una grabacion de voz clave para la misión... 'No debimos abrir la compuerta...' dice una voz temblorosa\n")
        jugador["inventario"].append("Grabadora de voz - 01")

    if jugador["vida"] > 0:
        print("Despues de lo sucedido le reportas a tu grupo, pero al parecer la señal es muy inestable, no puedes comprender lo que dicen tus compañeros y tampoco sabes si te escucharon...\n")
        print("Tras investigar la zona, llegas al hangar de carga\n")
        print("La señal se pierde por completo, no puedes contactarte con tu grupo ni con la estación Orión 189...\n")

        decision_final = 0

        while decision_final != 1 and decision_final != 2:
            print("// En el centro del hangar, algo gigante bloquea el paso a la salida del lugar. //")
            print("1. Intentas rodear a la criatura en silencio")
            print("2. Atacar con todo!\n")
            pelea_jefe = False

            print("\n---------------------------")
            decision_final = int(input("¿Que vas a realizar? (1-2): "))
            print("---------------------------")

            if decision_final != 1 and decision_final != 2:
                print("\n<<<< Opción Invalida. ELige 1 o 2 >>>>\n")

        if decision_final == 1:
            print("Caminas cuidadosamente sobre el frio metal de la nave, pero tropiezas con un casco")
            print("El monstruo se da cuenta... ¡Es el Blind Whale!\n")
            pelea_jefe = True
        else:
            print("¡Disparas al aire! La Blind Whale ruge y se abalanza con todo sobre ti.\n")
            pelea_jefe = True
        
        if pelea_jefe:
            jefe = enemigos[3]
            while jefe["vida"] > 0 and jugador["vida"] > 0:
                print(f"Jefe: {jefe['nombre']} | Vida: {jefe['vida']}\n")
                print(f"Tu vida: {jugador['vida']}\n")

                ataque_final = ""
                while ataque_final != "a" and ataque_final != "b":
                    print("\n------------------------------------------------------")
                    ataque_final = input("¿Usar arma de Plasma o Porra electrica (A-B): ").lower()
                    print("------------------------------------------------------")

                    if ataque_final != "a" and ataque_final != "b":
                        print("\n<<<< Opción invalida. Elige uno de las dos armas (A-B) >>>>\n")
                if ataque_final == "a":
                    daño_jefe = jugador["ataque"] + 5
                    jefe["vida"] = jefe["vida"] - daño_jefe
                    print(f"\n¡Impacto directo! Quitas {daño_jefe} de vida.\n")

                else:
                    jefe["vida"] = jefe ["vida"] -5
                    print("\nLa porra electrica apenas hace daño...\n")
                
                if jefe["vida"] > 0:
                    jugador["vida"] = jugador["vida"] - jefe["daño"]
                    print(f"La Blind Whale te embiste! Pierdes {jefe['daño']} de vida.")

                    curarse = ""

                    while curarse != "s" and curarse != "n":

                        print(f"Disponibles: {jugador['nanobots']} de {jugador['tipo_curacion']}\n")
                        print("\n---------------------------------------------")
                        curarse = input("Deseas curarte si (S) o no (N): ").lower()
                        print("---------------------------------------------")
                        if curarse != "s" and curarse != "n":
                            print("\n<<<< Opción invalida. Elige (s) o (n) >>>>\n")
                    if curarse == "s":
                        if jugador["nanobots"] > 0:
                            jugador["vida"] = jugador["vida"] + 40
                            jugador["nanobots"] = jugador["nanobots"] - 1
                            print("\nInyectando nanobots en torrente sanguíneo...")
                            print("Reparando tejidos dañados\n")
                            print(f"Usaste {jugador['tipo_curacion']}. +40 de vida.\n")
                        else:
                            print("¡No te quedan suministros médicos!\n")

                    if jugador["vida"] <= 0:
                        jugando = False

                    elif curarse == "n":
                        print("¡Sigues en combate!\n")
                        
            if jugador["vida"] <= 0:
                print("\n>>>> Has caido en combate... <<<<")
                print(f"La {jefe['nombre']} ha terminado con tu misión.\n")
                jugando = False

            elif jefe["vida"] <= 0:
                print(">>>> ¡INCREIBLE! Has derrotado a la Blind Whale. <<<<\n")
                eliminados = eliminados + 1
                jugador["creditos"] = jugador["creditos"] + 500
                jugador["inventario"].append("Nucleo de la Estación")
                print("Encuentras la tarjeta de acceso del Capitán en el suelo.")
                jugador["inventario"].append("Tarjeta del Capitán")

    if jugador["vida"] > 0:

        escape = ""

        while escape != "s" and escape != "n":
            print("\nDe repente, suena algo que te alerta enseguida")
            print("El sistema de autodestrucción se ha activado: 5 minutos y contando...\n")
            print("\n-----------------------------------------------------")
            escape = input("¿Correr hacia la capsula de escape? (S/N): ").lower()
            print("-----------------------------------------------------")
            if escape != "s" and escape != "n":
                print(">> Opción no válida. El pánico te invade el cuerpo, ¡responde S o N! <<\n")

        if escape == "s" and "Tarjeta del Capitán" in jugador["inventario"]:
            print("!Lograste escapar de la Aphex 004 antes de la explosión!\n")
            jugando = False
        else:
            print("No pudiste salir a tiempo o no tenias la tarjeta...\n")
            jugador["vida"] = 0
            jugando = False

print("\n------- RESUMEN FINAL DE LA EXPEDICIÓN -------\n")
for objeto in jugador["inventario"]:
    print("- " + objeto)

if jugador["vida"] <= 0:
    print("¡Mision fracasada!")
else:
    if eliminados >= 2:
        print("Felicidades, has purgado la amenaza de la Aphex 004.\n")
    elif eliminados == 1:
        print("Sobreviviste, pero la infección sigue ahí afuera...\n")

print(f"Créditos totales en la partida: {jugador['creditos']}\n")

if "Grabadora de voz - 01" in jugador["inventario"]:
    print("Has recuperado evidencia clave de lo ocurrido en la Aphex 004, esto ayudara a exterminar las amenazas restantes a corto plazo.\n")