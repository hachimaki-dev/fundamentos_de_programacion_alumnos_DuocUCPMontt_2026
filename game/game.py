import time
def imprimir(texto, velocidad=0.03):
    for letra in texto:
        print(letra, end="", flush=True)
        time.sleep(velocidad)
    print()
import sys
imprimir("=== BIENVENIDO AL JUEGO, VE  COMIENZA TU AVENTURA ===")
entrar = 1
nombre_jugador = input("POR FAVOR INGRESE SU NOMBRE DE AVENTURERO: ")
entrada_aljuego = int(input("1. ENTRAR  2. SALIR \n"))
if entrada_aljuego == 1:
    print("//// ESCOGE TU CLASE ////")
    clase = int(input("[[[1. MAGO]]] \n[[[2.CABALLERO]]] \n[[[3.ASESINO]]] \n"))
    if clase == 1:
        hpmago = 75
        atkmago = 5
        apmago = 35
        manamago = 50
    elif clase == 2:
        hpcaballero = 150
        atkcaballero = 40
        apcaballero = 0
        manacaballero = 0
    elif clase == 3:
        hpasesino = 90
        atkasesino = 55
        apasesino = 5
        manaasesino = 20
    else:
        print("Aún no tenemos disponible más clases lo sentimos :( .)")
    time.sleep(1)
    imprimir(f"°|||=> {nombre_jugador} para empezar su aventura se dirige al gremio para reclamar su primera misión <=|||°", 0.05)
    time.sleep(1.5)
    mision = int(input(f"Maestra del Gremio: Bienvenido {nombre_jugador}, aqui tenemos las distintas misiones para tu aventura. \n--- 1. Derrotar al jefe de la mazmorra oculta entre las montañas --- \n--- 2. Pelear contra Cerbero, el perro del inframundo --- \n ---> "))
    if mision == 1:
        if clase == 1:
            imprimir("Te diriges en busca de la mazmorra con tu equipamiento principiante y con tu magia iluminas tu camino.")
            imprimir("Dentro de la mazmorra sientes como un escalofrio recorre tu columna desde abajo hacia arriba, sabes que se acerca algo peligroso por tu maná.")
            time.sleep(1)
            imprimir(".")
            time.sleep(1.5)
            imprimir("..")
            time.sleep(1.8)
            imprimir("...")
            imprimir("¡¡¡¡HAZ ENTRADO EN COMBATE CON EL JEFE DIRECTAMENTE!!!!",0.03)
            bosshp = 500
            bossatk = 20
            while bosshp > 0 and hpmago > 0:
                if bosshp <= 0:
                    print("Combate finalizado.\nHaz derrotado al jefe.")
                    break
                elif hpmago <= 0:
                    print("Haz sido derrotado por el jefe de la mazmorra, intentalo mejor la proxima vez.")
                    sys.exit()
                accion = int(input("\n1.Atacar\n2.Ver estadisticas\n3.Curarse\n4.Intentar huir. \n---> "))
                if accion == 1:
                    rayodeluz = 5
                    vendaval = 3
                    pelluco = 10
                    ataquesmago = int(input("\n1.|Rayo de luz|\n2.|Vendaval del sur|\n3.|Invocar a Pelluco|\n---> "))
                    if ataquesmago == 1:
                        bosshp = bosshp - (rayodeluz * apmago)
                        manamago = manamago - 10
                        print(f"Ataque efectivo, vida restante del enemigo : {bosshp}.")
                    elif ataquesmago ==2:
                        bosshp = bosshp - (vendaval * apmago)
                        manamago -= 5
                        print(f"Azotas con fuertes vientos a tu enemigo, su vida restante : {bosshp}.")
                    elif ataquesmago == 3:
                        print(f"¡Pelluco ha aparecido!\nEstá muy enojado por haberlo despertado de su sueño.")
                        bosshp = bosshp - (pelluco *apmago)
                        manamago -= 10
                        print(f"Le ha causado fatales heridas al enemigo, su hp es de {bosshp}.")
                    else:
                        print("Haz pérdido un turno y el enemigo aprovecha para atacarte")
                        hpmago -= bossatk
                        print(f"Tu vida restante es : {hpmago}.")
                elif accion == 2:
                    print(f"Vida total del enemigo : {bosshp}.\nAtaque del enemigo : {bossatk}.")
                elif accion == 3:
                    if manamago > 0:
                        hpmago += 15
                        manamago -= 5
                        print(f"Te haz curado 15 puntos vitales, tu HP restante : {hpmago}.\n Maná restante : {manamago}.")
                    else:
                        print("No tienes suficiente maná, no puedes curarte.")
                elif accion == 4:
                    print("No puedes huir en este combate, que lamentable.")
            imprimir("Al derrotar al jefe quedas exhausto del combate, decides tomar el botín que estaba a su lado y regresar al gremio para descansar.")
            print("==== AVENTURA FINALIZADA ====")
        elif clase == 2:
            imprimir("Has decidido ir a la mazmorra para derrotar al jefe y empezar bien tu aventura.")
            imprimir("Dentro de la mazmorra sientes un viento que te llena de energía, estas listo para cualquier combate.")
            time.sleep(1)
            imprimir(".")
            time.sleep(1.5)
            imprimir("..")
            time.sleep(1.8)
            imprimir("...")
            imprimir("Aparece el jefe delante tuyo, tiene un aspecto grotesco",0.03)
            bosshp = 500
            bossatk = 20
            while bosshp > 0 and hpcaballero > 0:
                if bosshp <= 0:
                    print("Combate finalizado.\nHaz derrotado al jefe.")
                    break
                elif hpcaballero <= 0:
                    print("Haz sido derrotado por el jefe de la mazmorra, intentalo mejor la proxima vez.")
                    sys.exit()
                accion = int(input("\n1.Atacar\n2.Ver estadisticas\n3.Intentar huir. \n---> "))
                if accion == 1:
                    empalamiento = 3
                    tajocelestial = 10
                    ataquecaballero = int(input("\n1.|Empalamiento|\n2.|Tajo Celestial|\n---> "))
                    if ataquecaballero == 1:
                        bosshp = bosshp - (empalamiento * atkcaballero)
                        print(f"Ataque efectivo, vida restante del enemigo : {bosshp}.")
                    elif ataquecaballero == 2:
                        bosshp = bosshp - (tajocelestial * atkcaballero)
                        print(f"Azotas con fuertes vientos a tu enemigo, su vida restante : {bosshp}.")
                    else:
                        print("Haz pérdido un turno y el enemigo aprovecha para atacarte")
                        hpcaballero -= bossatk
                        print(f"Tu vida restante es : {hpcaballero}.")
                elif accion == 2:
                    print(f"Vida total del enemigo : {bosshp}.\nAtaque del enemigo : {bossatk}.")
                elif accion == 3:
                    print("No puedes huir en este combate, que lamentable.")
            imprimir("Al derrotar al jefe quedas exhausto del combate, decides tomar el botín que estaba a su lado y regresar al gremio para descansar.")
            print("==== AVENTURA FINALIZADA ====")

        elif clase == 3:
            print("")

    elif mision == 2:
        if clase == 1:
            imprimir("Te armas de valor, sabes que probablemente no regreses con vida...")
            time.sleep(2)
            imprimir("Pero debes intentarlo.")
            imprimir("En los pasillos del infierno vez como hay muchos cuerpos devorados con la carne destazada o incinerada, el olor es fuerte y no puedes aguantar taparte la nariz.")
            imprimir("Sabes que Cerbero esta cerca tuyo, tu maná lo detecta cerca asi que te pones en guardia.")
            print("Haz entrado en combate contra el perro del infierno, Cerbero.")
            bosshp = 1500
            bossatk = 15
            while bosshp > 0 and hpmago > 0:
                if bosshp <= 0:
                    print("Combate finalizado.\nHaz derrotado a Cerbero.")
                    break
                elif hpmago <= 0:
                    print("Haz sido devorado por Cerbero, intentalo mejor la proxima vez.")
                    sys.exit()
                accion = int(input("\n1.Atacar\n2.Ver estadisticas\n3.Curarse\n4.Intentar huir. \n---> "))
                if accion == 1:
                    rayodeluz = 5
                    vendaval = 3
                    pelluco = 10
                    ataquesmago = int(input("\n1.|Rayo de luz|\n2.|Vendaval del sur|\n3.|Invocar a Pelluco|\n---> "))
                    if ataquesmago == 1:
                        bosshp = bosshp - (rayodeluz * apmago)
                        manamago = manamago - 10
                        print(f"Ataque efectivo, vida restante del enemigo : {bosshp}.")
                    elif ataquesmago ==2:
                        bosshp = bosshp - (vendaval * apmago)
                        manamago -= 5
                        print(f"Azotas con fuertes vientos a tu enemigo, su vida restante : {bosshp}.")
                    elif ataquesmago == 3:
                        print(f"¡Pelluco ha aparecido!\nEstá muy enojado por haberlo despertado de su sueño.")
                        bosshp = bosshp - (pelluco *apmago)
                        manamago -= 10
                        print(f"Le ha causado fatales heridas al enemigo, su hp es de {bosshp}.")
                    else:
                        print("Haz pérdido un turno y el enemigo aprovecha para atacarte")
                        hpmago -= bossatk
                        print(f"Tu vida restante es : {hpmago}.")
                elif accion == 2:
                    print(f"Vida total del enemigo : {bosshp}.\nAtaque del enemigo : {bossatk}.")
                elif accion == 3:
                    if manamago > 0:
                        hpmago += 15
                        manamago -= 5
                        print(f"Te haz curado 15 puntos vitales, tu HP restante : {hpmago}.\n Maná restante : {manamago}.")
                    else:
                        print("No tienes suficiente maná, no puedes curarte.")
                elif accion == 4:
                    print("No puedes huir en este combate, que lamentable.")
            imprimir("Cerbero ha muerto en tus manos, puedes regresar al gremio para descansar y reclamar tu botín.")
            print("==== AVENTURA FINALIZADA ====")
        elif clase == 2:
            imprimir("Como caballero, tienes confianza en ti y te preparas para bajar al infierno.")
            time.sleep(2)
            imprimir("Escuchas a Cerbero acercarse, sostienes tu espada con fuerza y te preparas para pelear.")
            print("Haz entrado en combate contra el perro del infierno, Cerbero.")
            bosshp = 1500
            bossatk = 15
            while bosshp > 0 and hpcaballero > 0:
                if bosshp <= 0:
                    print("Combate finalizado.\nHaz derrotado a Cerbero.")
                    break
                elif hpcaballero <= 0:
                    print("Haz sido devorado por Cerbero, intentalo mejor la proxima vez.")
                    sys.exit()
                accion = int(input("\n1.Atacar\n2.Ver estadisticas\n3.Intentar huir. \n---> "))
                if accion == 1:
                    empalamiento = 3
                    tajocelestial = 10
                    ataquecaballero = int(input("\n1.|Empalamiento|\n2.|Tajo Celestial|\n---> "))
                    if ataquecaballero == 1:
                        bosshp = bosshp - (empalamiento * atkcaballero)
                        print(f"Ataque efectivo, vida restante del enemigo : {bosshp}.")
                    elif ataquecaballero == 2:
                        bosshp = bosshp - (tajocelestial * atkcaballero)
                        print(f"Azotas con fuertes vientos a tu enemigo, su vida restante : {bosshp}.")
                    else:
                        print("Haz pérdido un turno y el enemigo aprovecha para atacarte")
                        hpcaballero -= bossatk
                        print(f"Tu vida restante es : {hpcaballero}.")
                elif accion == 2:
                    print(f"Vida total del enemigo : {bosshp}.\nAtaque del enemigo : {bossatk}.")
                elif accion == 3:
                    print("No puedes huir en este combate, que lamentable.")
            imprimir("Cerbero ha muerto, tu espada y escudo merecen un descanso despúes de esta hazaña, te vas de regreso al gremio.")
            print("==== AVENTURA FINALIZADA ====")

        elif clase == 3:    #Aqui va la actividad de asesino
            nombre = input("ingrese tu nombre aventurero:")

            print("...DESPERTASTE")
            print(f"{nombre}:¿donde estoy? ¿que es este lugar?")
            print("(vez a tu alrededor y solo ves oscuridad)")
            print("a lo lejos vez una ventana y estas en una especie de pieza")

        while True:
         print(" 1.ver afuera de la ventana\n 2.buscar la puerta")
         opciones = int(input("que haras ahora :"))
         opcion_1 = 1
         opcion_2 = 2

         if opciones == 1:
            print("ves afuera de la ventana.... solo vez niebla")
        
         else :
            opciones == 2
            print("encuentras una puerta y intentas abrirla")
            break

         print("sales de una especie de celda")
         print(f"{nombre}: ¿como llegue hasta aca? porque hay un pasillo tan largo?")
         print(f"{nombre}: no veo el final")
         print("ves muchas puertas y cada una tiene un texto diferente")
         print("llegas a la primera puerta a mano derecha, tiene una fecha ")
         print(" 23/08/1960")
         print("te entra una jaqueca enorme")

         while True:
            print("1.entrar en la puerta?\n2.seguir a la siguiente")
            print(" (si sigues tu camino no habra regreso atras) ")
            opciones = int(input("que haras ahora?:"))
            opcion_1 = 1
            opcion_2 = 2
            if opcion_1 == 1:
                print(" regresas a la fecha exacta.. 23/08/1960")
            else:
                opcion_2 == 2
                print("llegas a la siguiente puerta a mano izquierda")
                break
            print("al abrir la puerta ves un salón enorme")
            print("las paredes están cubiertas de relojes, todos marcando horas distintas")
            print(f"{nombre}: ¿qué significa todo esto?")
            print("en el centro hay un espejo antiguo, con tu reflejo mirándote fijamente")
            print("pero tu reflejo sonríe... y te habla")
            print(f"{nombre}: ¡¿qué está pasando?!")
            print("reflejo: 'Has cruzado el pasillo del tiempo. Cada puerta era un destino posible.'")
            print("reflejo: 'Ahora debes elegir: quedarte atrapado en un recuerdo... o seguir adelante.'")
            while True:
                print("1. Romper el espejo\n2. Aceptar tu reflejo y entrar en él")
                decision = int(input("¿Qué harás ahora?:"))
                if decision == 1:
                    print("rompes el espejo... la oscuridad te envuelve")
                    print("cuando abres los ojos, despiertas en tu cama. ¿Fue todo un sueño?")
                    break
                elif decision == 2:
                    print("tocas el espejo y tu reflejo te absorbe")
                    print("te conviertes en parte del pasillo eterno, guardián de las puertas del tiempo")
                    print("tu historia termina... pero el pasillo sigue esperando nuevos aventureros")
                    break
    else:
        print("Escoja una misión disponible porfavor.")
else:
    print("Hasta la próxima jugador(a). )")