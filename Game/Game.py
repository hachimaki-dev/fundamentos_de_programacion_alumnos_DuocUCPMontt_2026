#"Pokebola Normal", "Pokebola Normal", "Pokebola Normal", "Pokebola Normal", "Pokebola Normal", "Pocion De Vida Para Pokemon"
opcion= 0

logo_pokemon = """
██████╗  ██████╗ ██╗  ██╗███████╗███╗   ███╗ ██████╗ ███╗   ██╗
██╔══██╗██╔═══██╗██║ ██╔╝██╔════╝████╗ ████║██╔═══██╗████╗  ██║
██████╔╝██║   ██║█████╔╝ █████╗  ██╔████╔██║██║   ██║██╔██╗ ██║
██╔═══╝ ██║   ██║██╔═██╗ ██╔══╝  ██║╚██╔╝██║██║   ██║██║╚██╗██║
██║     ╚██████╔╝██║  ██╗███████╗██║ ╚═╝ ██║╚██████╔╝██║ ╚████║
╚═╝      ╚═════╝ ╚═╝  ╚═╝╚══════╝╚═╝     ╚═╝ ╚═════╝ ╚═╝  ╚═══╝
"""

Tu_Pokemon_Inicial = ""

Pokemon_inicial_escogido_Charmander = False #Sistema de banderas que activa caminos segun el pokemon que uno escogio

Pokemon_inicial_escogido_Bulbasaur = False #Dependiendo del Pokemon escogido se volvera True la variable correspondiente

Pokemon_inicial_escogido_Squirtle = False #Esto permitira que los dialogos y acciones cambien, sin tener que crear muchas subramas dentro de una misma subrama

Tipo_de_elemento_de_tu_pokemon_inicial = ""

Dinero_del_Jugador = 10 #Dolares

Indicador_del_numero_de_item_en_la_mochila = 1

Mensaje_por_activacion_seguida_de_mochila_vacia = False

Contador_de_veces_que_abre_la_mochila_vacia = 2

Indicador_numero_de_turno_batalla = 1 #Se puede reutilizar en cualquier batalla

Pidgey_ataque_de_arena = False

Escapar_de_la_batalla = False

Cantidad_de_usos_Refugio_de_Squirtle = 0

Refugio_de_Squirtle_activado_por_dos_turnos = False

print(logo_pokemon)

print("-----Bienvenido a Pokemon Masters RPG-----")

input("Para continuar despues de que aparezca un texto, deberas presionar cualquier ENTER.")

Nombre_del_Jugador = input("Introduce tu nombre: ")

Nombre_de_tu_Rival = input("Introduce el nombre de tu rival: ")

Mochila_del_jugador = []


print(f"Hola, {Nombre_del_Jugador}, bienvenido a este maravilloso mundo, donde criaturas mágicas caminan junto a nosotros los humanos.")

input()

print("Te levantas temprano por la mañana, emocionado por que sera el dia en que te convertiras en un entrenador Pokemon, Tu madre te dice que vayas a hablar con el profesor Oák, para que te de instrucciones sobre como iniciar tu aventura.")

input()

print("Te diriges hacia el laboratorio del profesor Oák y al llegar el te recibe con una sonrisa y un apreton de manos.")

input()

print("A continuacion, el profesor Oák te indica que debes elegir a tu Pokemon inicial, miras la mesa con atencion, y te das cuenta de que hay 3 Pokebolas las cuales contienen 1 Pokemon cada una, el profesor Oák las lanza al suelo y tu puedes obvservar los diferentes Pokemon que salieron de alli.")

input()

while True:
  print("-----Elige tu Pokemon inicial-----")
  print("1. Charmander")
  print("2. Bulbasaur")
  print("3. Squirtle")
  
  Eleccion_De_Pokemon= input("Introduce alguna opcion: ")
  
  if Eleccion_De_Pokemon == "1":
    
    Tu_Pokemon_Inicial = "Charmander"
    
    Tipo_de_elemento_de_tu_pokemon_inicial = "Fuego"
    
    #Estadisticas de Charmander
    
    Charmander_PS = 26
    
    Charmander_Daño = 9
    
    Charmander_Agilidad = 45
    
    Charmander_Defensa = 18
    
    Pokemon_inicial_escogido_Charmander = True
    
    print(f"Interesante, has elegido a {Tu_Pokemon_Inicial} como tu compañero de aventuras.")
    input()
    print("Estadisticas de tu pokemon:")
    print(f"PS de tu {Tu_Pokemon_Inicial}: {Charmander_PS}")
    print(f"Ataque de tu {Tu_Pokemon_Inicial}: {Charmander_Daño}")
    print(f"Agilidad de tu {Tu_Pokemon_Inicial}: {Charmander_Agilidad}")
    print(f"Defensa de tu {Tu_Pokemon_Inicial}: {Charmander_Defensa}")
    print()
    print(f"Tu {Tu_Pokemon_Inicial} es del tipo {Tipo_de_elemento_de_tu_pokemon_inicial}.")
    input()
    break
    
  elif Eleccion_De_Pokemon == "2":
    
    Tu_Pokemon_Inicial = "Bulbasaur"
    
    Tipo_de_elemento_de_tu_pokemon_inicial = "Planta"
    
    #Estadisticas de Bulbasaur
    
    Bulbasaur_PS = 30
    
    Bulbasaur_Daño = 7
    
    Bulbasaur_Agilidad = 37
    
    Bulbasaur_Defensa = 17
    
    Pokemon_inicial_escogido_Bulbasaur = True
    
    print(f"Perfecto, has elegido a {Tu_Pokemon_Inicial} como tu compañero de aventuras.")
    input()
    print("Estadisticas de tu pokemon:")
    print()
    print(f"PS de tu {Tu_Pokemon_Inicial}: {Bulbasaur_PS}")
    print(f"Ataque de tu {Tu_Pokemon_Inicial}: {Bulbasaur_Daño}")
    print(f"Agilidad de tu {Tu_Pokemon_Inicial}: {Bulbasaur_Agilidad}")
    print(f"Defensa de tu {Tu_Pokemon_Inicial}: {Bulbasaur_Defensa}")
    print()
    print(f"Tu {Tu_Pokemon_Inicial} es del tipo {Tipo_de_elemento_de_tu_pokemon_inicial}.")
    input()
    break
    
  elif Eleccion_De_Pokemon == "3":
    
    Tu_Pokemon_Inicial = "Squirtle"
    
    Tipo_de_elemento_de_tu_pokemon_inicial = "Agua"
    
    #Estadisticas de Squirtle
    
    Squirtle_PS = 33    
    
    Squirtle_Daño = 22
    
    Squirtle_Agilidad = 35
    
    Squirtle_Defensa = 13
    
    Pokemon_inicial_escogido_Squirtle = True
    
    print(f"Perfecto, has elegido a {Tu_Pokemon_Inicial} como tu compañero de aventuras.")
    input()
    print("Estadisticas de tu pokemon:")
    print()
    print(f"PS de tu {Tu_Pokemon_Inicial}: {Squirtle_PS}")
    print(f"Ataque de tu {Tu_Pokemon_Inicial}: {Squirtle_Daño}")
    print(f"Agilidad de tu {Tu_Pokemon_Inicial}: {Squirtle_Agilidad}")
    print(f"Defensa de tu {Tu_Pokemon_Inicial}: {Squirtle_Defensa}")
    print()
    print(f"Tu {Tu_Pokemon_Inicial} es del tipo {Tipo_de_elemento_de_tu_pokemon_inicial}.")
    input()
    break
    
  else:
    print("La opcion que escogiste no es un Pokemon.")
    print("Intentalo otra vez.")
    
input()

print("El profesor Oák te mira, sonrie y te felicita debido a que al fin te has convertido en un Entrenador Pokemon.")

input()

print("El profesor Oák te pide que le vayas a comprar algo a la tienda, tu aceptas y le dices que volveras pronto.")

input()

while True:

  print("-----Que quieres hacer ahora?-----")

  print("1. Ir a comprar lo que necesita el Profesor Oák.")

  print("2. Abrir tu mochila")
  
  Primera_Accion_del_Jugador = input("Selecciona alguna opcion: ")
  
  if Primera_Accion_del_Jugador == "1":

    print("Excelente, a continuacion te diriges hacia la tienda a comprar lo que necesita el profesor Oák.")

    break
    
  elif Primera_Accion_del_Jugador == "2":

    if len(Mochila_del_jugador) <= 0: # Registra la cantidad de elementos en el inventario. En este caso es siempre 0. Por ende solo se va a imprimir el suguiente codigo.

        print("Por el momento, no tienes nada en tu mochila")

        Mensaje_por_activacion_seguida_de_mochila_vacia = True # Activacion personalizada de dialogo a futuro.

        continue

    for items in Mochila_del_jugador:
        
        # Sistema completo de inventario funcional. Por el momento en esta accion no se puede activar.

        print(f"{Indicador_del_numero_de_item_en_la_mochila} - {items}")

        Indicador_del_numero_de_item_en_la_mochila += 1

    input()

  else:

    print("Escoge una opcion válida.")
    
input()

print("Vas caminando por la Ruta hasta que te das cuenta de que algo se mueve entre la densa hierba.")

input()

print("Decides acercarte para ver que es lo que se mueve...")

input()

print("Wow! un Pokemon se arroja encima tuyo y entras en combate")

input()

print(f"Vas a depender de {Tu_Pokemon_Inicial} en esta ocasion")

print()

#Estadisticas del pokemon que se va a enfrentar (Pidgey)

Pidgey_PS = 26   
    
Pidgey_Daño = 6
    
Pidgey_Agilidad = 40
    
Pidgey_Defensa = 20

if Pokemon_inicial_escogido_Charmander == True: # Dependiendo del pokemon basico escogido. Cambiara las interacciones en el combate. En este caso es Charmander.

    Gruñido_de_charmander_activado_por_un_turno = False

    while Charmander_PS > 0 and Pidgey_PS > 0:
        input()
        print(f"Numero de Turno: {Indicador_numero_de_turno_batalla}")
        print("-----Elige que hacer:-----")
        print("1. Lucha")
        print("2. Revisar tu Mochila")
        print("3. Huir")
        print()

        Opciones_del_primer_combate_contra_Pidgey = input("Elige alguna opcion: ")
        
        if Opciones_del_primer_combate_contra_Pidgey == "1":   # Sistema de ataque

            print("1- Arañazo")

            print("2- Gruñido")

            Tipos_de_Ataque = int(input(f"Como va a atacar tu {Tu_Pokemon_Inicial}? (1/2) "))

            if Tipos_de_Ataque == 1:    # Tipo de ataque. Arañazo

                if Gruñido_de_charmander_activado_por_un_turno == False: # En caso de que al usar Arañazo NO se haya usado Gruñido antes. El siguiente codigo aparecera.

                    print(f"Tu {Tu_Pokemon_Inicial} usa Arañazo intentado quitar {Charmander_Daño}")

                    input()

                    if Pidgey_ataque_de_arena == True: # Si en el turno anterior Pidgey utilizo ataque de arena, el siguiente codigo aparecera.

                        print(f"Pero la precision de tu {Tu_Pokemon_Inicial} se ve afectada")

                        Azar_de_Precision = int(input(f"Escoge un numero del 1 al 6 (Determinara si el ataque de tu {Tu_Pokemon_Inicial} es efectivo)"))

                        # Intento de azar, segun la respuesta del usuario, el ataque fallara o acertara.

                        if Azar_de_Precision % 2 == 0:

                            print("Ataque fallido")

                            Pidgey_ataque_de_arena = False # El uso de ataque de arena de Pidgey se acabo.

                            continue
                        print("Ataque efectivo")
                      
                        input()
                    print("Pero el Pidgey tiene defensa alta resultando en 4 de Daño")

                    input()

                    Pidgey_PS = Pidgey_PS - 4

                    print(f"Vida restante del Pidgey: {Pidgey_PS}")

                    if Pidgey_PS <= 0:
                        break
                    input()

                    Pidgey_ataque_de_arena = False # Se desactiva naturalmente si se encontraba activo. En caso de lo contrario no cambia el resultado.

                if Gruñido_de_charmander_activado_por_un_turno == True: # En caso de que al usar Arañazo SI se haya usado Gruñido antes. El siguiente codigo aparecera.

                    print(f"Tu {Tu_Pokemon_Inicial} usa Arañazo intentado quitar {Charmander_Daño}")

                    input()

                    if Pidgey_ataque_de_arena == True: # Si en el turno anterior Pidgey utilizo ataque de arena, el siguiente codigo aparecera.

                        print(f"Pero la precision de tu {Tu_Pokemon_Inicial} se ve afectada")

                        # Intento de azar, segun la respuesta del usuario, el ataque fallara o acertara.

                        Azar_de_Precision = int(input(f"Escoge un numero del 1 al 6 (Determinara si el ataque de tu {Tu_Pokemon_Inicial} es efectivo)"))

                        if Azar_de_Precision % 2 == 0:

                            print("Ataque fallido")

                            Pidgey_ataque_de_arena = False # El uso de ataque de arena de Pidgey se acabo.

                            Gruñido_de_charmander_activado_por_un_turno = False # Al fracasar al acertar, el Gruñido de Charmander se desactiva.

                            continue

                        print("Ataque efectivo")
                      
                        # Si el ataque es efectivo, el codigo se imprimira naturalmente.

                        input()

                    print("El Pidgey se encuentra intimidado asi que el ataque es mas efectivo")
                    
                    input()

                    print(f"{Tu_Pokemon_Inicial} hara su daño natural")

                    input()

                    Pidgey_PS = Pidgey_PS - Charmander_Daño

                    print(f"Vida restante del Pidgey: {Pidgey_PS}")

                    if Pidgey_PS <= 0:
                        break
                    input()

                    Gruñido_de_charmander_activado_por_un_turno = False # Al hacer uso del gruñido de Charmander. se desactivara naturalmente.

                    Pidgey_ataque_de_arena = False # Se desactiva naturalmente si se encontraba activo. En caso de lo contrario no cambia el resultado.

            elif Tipos_de_Ataque == 2:  # Tipo de ataque. Gruñido

                print(f"Tu {Tu_Pokemon_Inicial} usa Gruñido, reduciendo la defensa del Pidgey a {Pidgey_Defensa/2} temporalmente")

                Gruñido_de_charmander_activado_por_un_turno = True

                # Esto causara que en el siguiente turno del usuario, si escoge Arañazo, el daño sera el original. Considera que igualmente el Pidgey si atacara a Charmander.

            else:   # En caso de una respuesta invalida. Se saltara el turno del usuario. Pidgey atacara igualmente.
                print("Opcion no aceptada")
                
                input()

                print("Perdiste tu turno")

                input()

        elif Opciones_del_primer_combate_contra_Pidgey == "2": # Mochila

            if Mensaje_por_activacion_seguida_de_mochila_vacia == True and Contador_de_veces_que_abre_la_mochila_vacia > 4:

                 # Cambio de dialogo en caso de que se abra la mochila muchas veces. No cambia ningun tipo de variable. El objetivo es darle mas vida al juego.

                print("Confirmas completamente que en tu mochila no hay nada")

            elif Mensaje_por_activacion_seguida_de_mochila_vacia == True:
                
                # Cambio de dialogo en caso de que se abra la mochila 2 o mas veces. El objetivo es darle mas vida al juego.

                print(f"Al parecer abrir tu mochila {Contador_de_veces_que_abre_la_mochila_vacia} veces seguidas no hace que aparezca algo")

                input()

                Contador_de_veces_que_abre_la_mochila_vacia += 1
            
            if Mensaje_por_activacion_seguida_de_mochila_vacia == False:
                
                # Dialogo que se activa al abrir tu mochila por primera vez. Considera que en el camino no la hayas abierto antes.

                print("Al revisar en tu mochila no encuentras nada")

                Mensaje_por_activacion_seguida_de_mochila_vacia = True

                input()
            
        elif Opciones_del_primer_combate_contra_Pidgey == "3": # Escapar
            
            # Sistema de escape el cual solo requiere un intento. Sera la unica batalla en la cual tome un solo intento.

            print("Has escapado de la batalla sin problemas")

            input()

            print("Puede que en un futuro no sea tan facil")

            Escapar_de_la_batalla = True

            break
         
        if Indicador_numero_de_turno_batalla == 3: # Turno especial de Pidgey. Siempre hara un ataque critico garantizado, para dificultar la batalla.

            print()

            print(f"Pidgey usa: Placaje")

            input() 
            
            print("El ataque de Pidgey fue critico")

            input()

            print("El daño se multiplico X2")

            Charmander_PS = Charmander_PS - 10

            if Charmander_PS <= 0:

                Charmander_PS = 0

                print(f"Vida restante de tu {Tu_Pokemon_Inicial}: {Charmander_PS}")

                break
            print(f"Vida restante de tu {Tu_Pokemon_Inicial}: {Charmander_PS}")

            Indicador_numero_de_turno_batalla += 1

            continue

        if Indicador_numero_de_turno_batalla % 2 != 0: # Indicador de tipo de ataque de Pidgey dependiendo del turno. Si es impar, Pidgey usara Placaje
            print()

            print(f"Pidgey usa: Placaje")

            input() 
            
            Charmander_PS = Charmander_PS - 5

            if Charmander_PS <= 0:

                Charmander_PS = 0

                print(f"Vida restante de tu {Tu_Pokemon_Inicial}: {Charmander_PS}")

                break
            print(f"Vida restante de tu {Tu_Pokemon_Inicial}: {Charmander_PS}")

        if Indicador_numero_de_turno_batalla % 2 == 0: # Indicador de tipo de ataque de Pidgey dependiendo del turno. Si es par, Pidgey usara Ataque de arena

            print()

            print(f"Pidgey usa: Ataque de arena")

            input()

            print(f"La precision de {Tu_Pokemon_Inicial} se ve afectada")

            Pidgey_ataque_de_arena = True #Indicador de si Pidgey uso ataque de arena, el cual va a afectar el siguiente ataque del pokemon escogido

        Indicador_numero_de_turno_batalla += 1 # Cambio de turno

if Pokemon_inicial_escogido_Bulbasaur == True: # Dependiendo del pokemon basico escogido. Cambiara las interacciones en el combate. En este caso es Bulbasaur.

    Gruñido_de_Bulbasaur_activado_por_un_turno = False

    while Bulbasaur_PS > 0 and Pidgey_PS > 0:
        input()
        print(f"Numero de Turno: {Indicador_numero_de_turno_batalla}")
        print("-----Elige que hacer:-----")
        print("1. Lucha")
        print("2. Revisar tu Mochila")
        print("3. Huir")
        print()

        Opciones_del_primer_combate_contra_Pidgey = input("Elige alguna opcion: ")
        
        if Opciones_del_primer_combate_contra_Pidgey == "1":   # Sistema de ataque

            print("1- Placaje")

            print("2- Gruñido")

            Tipos_de_Ataque = int(input(f"Como va a atacar tu {Tu_Pokemon_Inicial}? (1/2) "))

            if Tipos_de_Ataque == 1:    # Tipo de ataque. Placaje

                if Gruñido_de_Bulbasaur_activado_por_un_turno == False: # En caso de que al usar Placaje NO se haya usado Gruñido antes. El siguiente codigo aparecera.

                    print(f"Tu {Tu_Pokemon_Inicial} usa Placaje intentado quitar {Bulbasaur_Daño}")

                    input()

                    if Pidgey_ataque_de_arena == True: # Si en el turno anterior Pidgey utilizo ataque de arena, el siguiente codigo aparecera.

                        print(f"Pero la precision de tu {Tu_Pokemon_Inicial} se ve afectada")

                        Azar_de_Precision = int(input(f"Escoge un numero del 1 al 6 (Determinara si el ataque de tu {Tu_Pokemon_Inicial} es efectivo)"))

                        # Intento de azar, segun la respuesta del usuario, el ataque fallara o acertara.

                        if Azar_de_Precision % 2 == 0:

                            print("Ataque fallido")

                            Pidgey_ataque_de_arena = False # El uso de ataque de arena de Pidgey se acabo.

                            continue

                        print("Ataque efectivo")
                      
                        input()

                    print("Pero el Pidgey tiene defensa alta resultando en 3 de Daño")

                    input()

                    Pidgey_PS = Pidgey_PS - 3

                    if Pidgey_PS <= 0: # En caso de derrotar a Pidgey, la vida se pondra automaticamente en 0. Evitando que aparezcan los numeros en negativo
                        
                        Pidgey_PS = 0

                        print(f"Vida restante del Pidgey: {Pidgey_PS}")

                        break

                    print(f"Vida restante del Pidgey: {Pidgey_PS}")

                    input()

                    Pidgey_ataque_de_arena = False # Se desactiva naturalmente si se encontraba activo. En caso de lo contrario no cambia el resultado.

                if Gruñido_de_Bulbasaur_activado_por_un_turno == True: # En caso de que al usar Placaje SI se haya usado Gruñido antes. El siguiente codigo aparecera.

                    print(f"Tu {Tu_Pokemon_Inicial} usa Placaje intentado quitar {Bulbasaur_Daño}")

                    input()

                    if Pidgey_ataque_de_arena == True: # Si en el turno anterior Pidgey utilizo ataque de arena, el siguiente codigo aparecera.

                        print(f"Pero la precision de tu {Tu_Pokemon_Inicial} se ve afectada")

                        # Intento de azar, segun la respuesta del usuario, el ataque fallara o acertara.

                        Azar_de_Precision = int(input(f"Escoge un numero del 1 al 6 (Determinara si el ataque de tu {Tu_Pokemon_Inicial} es efectivo)"))

                        if Azar_de_Precision % 2 != 0:

                            print("Ataque fallido")

                            Pidgey_ataque_de_arena = False # El uso de ataque de arena de Pidgey se acabo.

                            Gruñido_de_charmander_activado_por_un_turno = False # Al fracasar al acertar, el Gruñido de Bulbasaur se desactiva.

                            continue

                        print("Ataque efectivo")
                      
                        # Si el ataque es efectivo, el codigo se imprimira naturalmente.

                        input()

                    print("El Pidgey se encuentra intimidado asi que Placaje sera mucho mas efectivo")
                    
                    input()

                    print(f"{Tu_Pokemon_Inicial} hara su daño natural")

                    input()

                    Pidgey_PS = Pidgey_PS - Bulbasaur_Daño_Daño

                    if Pidgey_PS <= 0: # En caso de derrotar a Pidgey, la vida se pondra automaticamente en 0. Evitando que aparezcan los numeros en negativo
                        
                        Pidgey_PS = 0

                        print(f"Vida restante del Pidgey: {Pidgey_PS}")

                        break

                    print(f"Vida restante del Pidgey: {Pidgey_PS}")

                    input()

                    Gruñido_de_Bulbasaur_activado_por_un_turno = False # Al hacer uso del gruñido de Bulbasaur. se desactivara naturalmente.

                    Pidgey_ataque_de_arena = False # Se desactiva naturalmente si se encontraba activo. En caso de lo contrario no cambia el resultado.

            elif Tipos_de_Ataque == 2:  # Tipo de ataque. Gruñido

                print(f"Tu {Tu_Pokemon_Inicial} usa Gruñido, reduciendo la defensa del Pidgey a {Pidgey_Defensa/2} temporalmente")

                Gruñido_de_Bulbasaur_activado_por_un_turno = True

                # Esto causara que en el siguiente turno del usuario, si escoge Arañazo, el daño sera el original. Considera que igualmente el Pidgey si atacara a Bulbasaur

            else:   # En caso de una respuesta invalida. Se saltara el turno del usuario. Pidgey atacara igualmente.
                print("Opcion no aceptada")
                
                input()

                print("Perdiste tu turno")

                input()

        elif Opciones_del_primer_combate_contra_Pidgey == "2": # Mochila

            if Mensaje_por_activacion_seguida_de_mochila_vacia == True and Contador_de_veces_que_abre_la_mochila_vacia > 4:

                 # Cambio de dialogo en caso de que se abra la mochila muchas veces. No cambia ningun tipo de variable. El objetivo es darle mas vida al juego.

                print("Confirmas completamente que en tu mochila no hay nada")

            elif Mensaje_por_activacion_seguida_de_mochila_vacia == True:
                
                # Cambio de dialogo en caso de que se abra la mochila 2 o mas veces. El objetivo es darle mas vida al juego.

                print(f"Al parecer abrir tu mochila {Contador_de_veces_que_abre_la_mochila_vacia} veces seguidas no hace que aparezca algo")

                input()

                Contador_de_veces_que_abre_la_mochila_vacia += 1
            
            if Mensaje_por_activacion_seguida_de_mochila_vacia == False:
                
                # Dialogo que se activa al abrir tu mochila por primera vez. Considera que en el camino no la hayas abierto antes.

                print("Al revisar en tu mochila no encuentras nada")

                Mensaje_por_activacion_seguida_de_mochila_vacia = True

                input()
            
        elif Opciones_del_primer_combate_contra_Pidgey == "3": # Escapar
            
            # Sistema de escape el cual solo requiere un intento. Sera la unica batalla en la cual tome un solo intento.

            print("Has escapado de la batalla sin problemas.")

            input()

            print("Puede que en un futuro no sea tan facil.")

            Escapar_de_la_batalla = True

            break
         
        if Indicador_numero_de_turno_batalla == 3: # Turno especial de Pidgey. Siempre hara un ataque critico garantizado, para dificultar la batalla.

            print()

            print(f"Pidgey usa: Placaje")

            input() 
            
            print("El ataque de Pidgey fue critico")

            input()

            print("El daño se multiplico X2")

            Bulbasaur_PS = Bulbasaur_PS - 10

            if Bulbasaur_PS <= 0:

                Bulbasaur_PS = 0

                print(f"Vida restante de tu {Tu_Pokemon_Inicial}: {Bulbasaur_PS}")

                break
            print(f"Vida restante de tu {Tu_Pokemon_Inicial}: {Bulbasaur_PS}")

            Indicador_numero_de_turno_batalla += 1

            continue

        if Indicador_numero_de_turno_batalla % 2 != 0: # Indicador de tipo de ataque de Pidgey dependiendo del turno. Si es impar, Pidgey usara Placaje
            print()

            print(f"Pidgey usa: Placaje")

            input() 
            
            Bulbasaur_PS = Bulbasaur_PS - 5

            if Bulbasaur_PS <= 0:

                Bulbasaur_PS = 0

                print(f"Vida restante de tu {Tu_Pokemon_Inicial}: {Bulbasaur_PS}")

                break
            print(f"Vida restante de tu {Tu_Pokemon_Inicial}: {Bulbasaur_PS}")

        if Indicador_numero_de_turno_batalla % 2 == 0: # Indicador de tipo de ataque de Pidgey dependiendo del turno. Si es par, Pidgey usara Ataque de arena

            print()

            print(f"Pidgey usa: Ataque de arena")

            input()

            print(f"La precision de {Tu_Pokemon_Inicial} se ve afectada")

            Pidgey_ataque_de_arena = True # Indicador de si Pidgey uso ataque de arena, el cual va a afectar el siguiente ataque del pokemon escogido

        Indicador_numero_de_turno_batalla += 1 # Cambio de turno

if Pokemon_inicial_escogido_Squirtle == True: # Dependiendo del pokemon basico escogido. Cambiara las interacciones en el combate. En este caso es Squirtle.

    while Squirtle_PS > 0 and Pidgey_PS > 0:

        input()
        print(f"Numero de Turno: {Indicador_numero_de_turno_batalla}")
        print("-----Elige que hacer:-----")
        print("1. Lucha")
        print("2. Revisar tu Mochila")
        print("3. Huir")
        print()

        Opciones_del_primer_combate_contra_Pidgey = input("Elige alguna opcion: ")
        
        if Opciones_del_primer_combate_contra_Pidgey == "1":   # Sistema de ataque

            print("1- Placaje")

            print("2- Refugio")

            Tipos_de_Ataque = int(input(f"Como va a atacar tu {Tu_Pokemon_Inicial}? (1/2) "))

            if Tipos_de_Ataque == 1:    # Tipo de ataque. Placaje

                    print(f"Tu {Tu_Pokemon_Inicial} usa Placaje intentado quitar {Squirtle_Daño}")

                    input()

                    if Pidgey_ataque_de_arena == True: # Si en el turno anterior Pidgey utilizo ataque de arena, el siguiente codigo aparecera.

                        print(f"Pero la precision de tu {Tu_Pokemon_Inicial} se ve afectada")

                        Azar_de_Precision = int(input(f"Escoge un numero del 1 al 6 (Determinara si el ataque de tu {Tu_Pokemon_Inicial} es efectivo)"))

                        # Intento de azar, segun la respuesta del usuario, el ataque fallara o acertara.

                        if Azar_de_Precision % 2 == 0:

                            print("Ataque fallido")

                            Pidgey_ataque_de_arena = False # El uso de ataque de arena de Pidgey se acabo.

                            continue

                        print("Ataque efectivo")
                      
                        input()

                    print("Pero el Pidgey tiene defensa alta resultando en 5 de Daño")

                    input()

                    Pidgey_PS = Pidgey_PS - 5

                    print(f"Vida restante del Pidgey: {Pidgey_PS}")

                    if Pidgey_PS <= 0: # En caso de derrotar a Pidgey, la vida se pondra automaticamente en 0. Evitando que aparezcan los numeros en negativo
                        
                        Pidgey_PS = 0

                        print(f"Vida restante del Pidgey: {Pidgey_PS}")

                        break

                    print(f"Vida restante del Pidgey: {Pidgey_PS}")

                    input()

                    Pidgey_ataque_de_arena = False # Se desactiva naturalmente si se encontraba activo. En caso de lo contrario no cambia el resultado.

            elif Tipos_de_Ataque == 2:  # Tipo de ataque. Refugio

                print(f"Tu {Tu_Pokemon_Inicial} usa Refugio, Aumentando la defensa de {Tu_Pokemon_Inicial} temporalmente!!!")

                Refugio_de_Squirtle_activado_por_dos_turnos = True # El refugio de Squirtle durara dos turnos seguidos.

                Cantidad_de_usos_Refugio_de_Squirtle = 2 # Variable para determinar cuantos usos quedan

                # Esto causara que en el siguiente turno del usuario, el daño de Pidgey haya reducido.

            else:   # En caso de una respuesta invalida. Se saltara el turno del usuario. Pidgey atacara igualmente.
                print("Opcion no aceptada")
                
                input()

                print("Perdiste tu turno")

                input()

        elif Opciones_del_primer_combate_contra_Pidgey == "2": # Mochila

            if Mensaje_por_activacion_seguida_de_mochila_vacia == True and Contador_de_veces_que_abre_la_mochila_vacia > 4:

                 # Cambio de dialogo en caso de que se abra la mochila muchas veces. No cambia ningun tipo de variable. El objetivo es darle mas vida al juego.

                print("Confirmas completamente que en tu mochila no hay nada")

            elif Mensaje_por_activacion_seguida_de_mochila_vacia == True:
                
                # Cambio de dialogo en caso de que se abra la mochila 2 o mas veces. El objetivo es darle mas vida al juego.

                print(f"Al parecer abrir tu mochila {Contador_de_veces_que_abre_la_mochila_vacia} veces seguidas no hace que aparezca algo")

                input()

                Contador_de_veces_que_abre_la_mochila_vacia += 1
            
            if Mensaje_por_activacion_seguida_de_mochila_vacia == False:
                
                # Dialogo que se activa al abrir tu mochila por primera vez. Considera que en el camino no la hayas abierto antes.

                print("Al revisar en tu mochila no encuentras nada")

                Mensaje_por_activacion_seguida_de_mochila_vacia = True

                input()
            
        elif Opciones_del_primer_combate_contra_Pidgey == "3": # Escapar
            
            # Sistema de escape el cual solo requiere un intento. Sera la unica batalla en la cual tome un solo intento.

            print("Has escapado de la batalla sin problemas")

            input()

            print("Puede que en un futuro no sea tan facil")

            Escapar_de_la_batalla = True

            break
         
        if Indicador_numero_de_turno_batalla == 3: # Turno especial de Pidgey. Siempre hara un ataque critico garantizado, para dificultar la batalla.
            if Cantidad_de_usos_Refugio_de_Squirtle == 0:

                Refugio_de_Squirtle_activado_por_dos_turnos = False

            if Refugio_de_Squirtle_activado_por_dos_turnos == False: # En caso de que el refugio de Squirtle se encuentre desactivado, se imprimira el suguiente codigo.

                print()

                print(f"Pidgey usa: Placaje")

                input() 
                
                print("El ataque de Pidgey fue critico")

                input()

                print("El daño se multiplico X2")

                Squirtle_PS = Squirtle_PS - 10

                if Squirtle_PS <= 0: # En caso de que Squirtle sea derrotado, la vida se pondra automaticamente en 0. Evitando que aparezcan los numeros en negativo

                    Squirtle_PS = 0

                    print(f"Vida restante de tu {Tu_Pokemon_Inicial}: {Squirtle_PS}")

                    break

                print(f"Vida restante de tu {Tu_Pokemon_Inicial}: {Squirtle_PS}")

                Indicador_numero_de_turno_batalla += 1

                continue
           
            if Refugio_de_Squirtle_activado_por_dos_turnos == True: # En caso de que el refugio de Squirtle se encuentre activado, se imprimira el suguiente codigo.

                print()

                print(f"Pidgey usa: Placaje")

                input() 
                
                print("El ataque de Pidgey fue critico")

                input()

                print("El daño se multiplico X2")

                input()

                print(f"Pero tu {Tu_Pokemon_Inicial} activo Refugio")

                input()

                print("El ataque se neutralizo")

                Squirtle_PS = Squirtle_PS - 5

                if Squirtle_PS <= 0: # En caso de que Squirtle sea derrotado, la vida se pondra automaticamente en 0. Evitando que aparezcan los numeros en negativo

                    Squirtle_PS = 0

                    print(f"Vida restante de tu {Tu_Pokemon_Inicial}: {Squirtle_PS}")

                    break

                print(f"Vida restante de tu {Tu_Pokemon_Inicial}: {Squirtle_PS}")

                Indicador_numero_de_turno_batalla += 1

                Cantidad_de_usos_Refugio_de_Squirtle -= 1

        if Indicador_numero_de_turno_batalla % 2 != 0: # Indicador de tipo de ataque de Pidgey dependiendo del turno. Si es impar, Pidgey usara Placaje

            if Cantidad_de_usos_Refugio_de_Squirtle == 0:

                Refugio_de_Squirtle_activado_por_dos_turnos = False

            if Refugio_de_Squirtle_activado_por_dos_turnos == False:
                print()

                print(f"Pidgey usa: Placaje")

                input() 
                
                Squirtle_PS = Squirtle_PS - 5

                if Squirtle_PS <= 0:

                    Squirtle_PS = 0

                    print(f"Vida restante de tu {Tu_Pokemon_Inicial}: {Squirtle_PS}")

                    break
                print(f"Vida restante de tu {Tu_Pokemon_Inicial}: {Squirtle_PS}")

            if Refugio_de_Squirtle_activado_por_dos_turnos == True:
                print()

                print(f"Pidgey usa: Placaje")

                input() 
                
                print(f"Pero tu {Tu_Pokemon_Inicial} tiene Refugio activado")

                input()

                print(f"El ataque de Pidgey se a reducido considerablemente!!!")

                Squirtle_PS = Squirtle_PS - 2

                if Squirtle_PS <= 0:

                    Squirtle_PS = 0

                    print(f"Vida restante de tu {Tu_Pokemon_Inicial}: {Squirtle_PS}")

                    break
                print(f"Vida restante de tu {Tu_Pokemon_Inicial}: {Squirtle_PS}")

                Cantidad_de_usos_Refugio_de_Squirtle -= 1

        if Indicador_numero_de_turno_batalla % 2 == 0: # Indicador de tipo de ataque de Pidgey dependiendo del turno. Si es par, Pidgey usara Ataque de arena

            print()

            print(f"Pidgey usa: Ataque de arena")

            input()

            print(f"La precision de {Tu_Pokemon_Inicial} se ve afectada")

            Pidgey_ataque_de_arena = True #Indicador de si Pidgey uso ataque de arena, el cual va a afectar el siguiente ataque del pokemon escogido

        Indicador_numero_de_turno_batalla += 1 # Cambio de turno

if Escapar_de_la_batalla == True: # Si se logra escapar de la batalla, se saltara cualquier tipo de recompensa.
    
    Escapar_de_la_batalla = False

elif Pidgey_PS <= 0 and Charmander_PS > 0 or Bulbasaur_PS > 0 or Squirtle_PS > 0:

    print("Has ganado la batalla, ganando 100 de EXP")

else:

    print("Perdiste la batalla")

    input()

    print(f"Tu {Tu_Pokemon_Inicial} se encuentra debilitado")

Indicador_numero_de_turno_batalla = 1 # El numero de turno se resetea. Esto permitira que se reutilize en cualquier batalla futura sin tener que crear una nueva variable

input()

print("Tras lidiar con aquel Pokemon que apareció en la hierba, continúas con la encomienda del profesor Oák dirigiéndote hacia la tienda.")

input()

print("Ya en la tienda, compras lo que el profesor te encargó")
input()

print("Viendo las vitrinas sientes que quizás deberías aprovechar la instancia para comprar algo... O quizás solo es el consumismo surgiendo dentro de tí")
input()

decision_tienda = input("¿Deseas ver los productos a la venta, o sólo te irás?  1. Comprar Objeto    2. Irte     ")
while True :
  if decision_tienda == "1" :
    print("Decides ver las opciones de objetos que tienen a la venta y te sorprendes por su repertorio")
    input()
    print("Con el dinero de la mensualidad que te daban tu madre y tu padre, y analizando los precios, tus 3 mejores opciones de compra son:")
    
    print("1. 3 Pociones Curativas (Capaces de curar 20PS's a tus Pokemon).")
    print("2. Comprar 1 Revivir.Máx (Puede revivir a 1 pokemon con todos sus PS).")
    print(f"3. Un medallón con la cara de {Tu_Pokemon_Inicial} (Completamente cosmético).")
    print("4. Te arrepientes y solo te vas.")
    
    compra_tienda = input("Que vas a hacer?")
      
      
    if compra_tienda == "1" :
        print("Decides comprar 3 pociones curativas, ocupando todo tu dinero, pero sientes que pueden cumplir un rol importante en tu aventura.")
        # Agregar un contador con variable de objeto_curativo para contar estos objetos en la mochila.
        break
    elif compra_tienda == "2" :
        print("Prefieres comprar un Revivir Máx, que luego de la explicación que te dió el dueño de la tienda, sientes que podría cumplir un gran propósito dada tu casi nula experiencia en combates pokémon")
        break
    elif compra_tienda == "3" :
        print(f"Te dejas llevar por tu corazón y compras este lindo medallón de {Tu_Pokemon_Inicial}, para conmemorar su primer día juntos.")
        break
    elif compra_tienda == "4" :
        print("Realmente sientes que no necesitarás nada de esto así que simplemente te vas")
        break
    else :
        print("Ingresa una opción válida porfavor.")
    
  elif decision_tienda == "2" :
        print("Solo quieres ahorrarte tu dinero para ti mismo como la persona egoísta que eres y te largas.")
        break
      
    
print("Hey! Tu aventura debera parar aqui por ahora, debido a que no tenemos mas tiempo para continuar con el codigo XD.")