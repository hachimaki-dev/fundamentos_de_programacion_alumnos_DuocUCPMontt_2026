print("██╗      ██████╗ ███████╗      ██╗")
print("██║     ██╔═══██╗██╔════╝      ██║")
print("██║     ██║   ██║███████╗      ██║")
print("██║     ██║   ██║╚════██║      ╚═╝")
print("███████╗╚██████╔╝███████║      ██╗")
print("╚══════╝ ╚═════╝ ╚══════╝      ╚═╝")

print("")
print("     ██╗██╗   ██╗███╗   ██╗ █████╗ ██████╗  ██████╗ ██╗   ██╗███████╗")
print("     ██║██║   ██║████╗  ██║██╔══██╗██╔══██╗██╔═══██╗╚██╗ ██╔╝██╔════╝")
print("     ██║██║   ██║██╔██╗ ██║███████║██████╔╝██║   ██║ ╚████╔╝ ███████╗")
print("██   ██║██║   ██║██║╚██╗██║██╔══██║██╔══██╗██║   ██║  ╚██╔╝  ╚════██║")
print("╚█████╔╝╚██████╔╝██║ ╚████║██║  ██║██████╔╝╚██████╔╝   ██║   ███████║")
print(" ╚════╝  ╚═════╝ ╚═╝  ╚═══╝╚═╝  ╚═╝╚═════╝  ╚═════╝    ╚═╝   ╚══════╝")

print("\n" + "░" * 20 + "DEMO" + "░" * 20)


input("Presione enter para continuar...")

personajes = ["Franco", "Matias", "Brayan"]

while True: 
    print("\n" + "░" * 20 + "MENU" + "░" * 20)
    print("1. escoger personaje")
    print("2. crear personaje")
    print("3. salir")

    eleccion_usuario = input("Elige una opcion (1/2/3): ")

    if eleccion_usuario == "3":

        print("hasta pronto")
        break 

    if eleccion_usuario == "1":

        print(f"{personajes}")
        personaje_elegido = input("escoger personaje: ")

    elif eleccion_usuario == "2":
        personaje_elegido = input("Ingrese el nombre de su personaje: ")

    else:
        print("opcion invalida")
        continue 

    print("\n===== REGLAS =====")
    print("1. tienes 5 vidas")
    print("2. Se amable con el abogado del diablo")
    print("3. no lastimes a sus animales")
    print("4. si tienes que escapar HAZLO")
    print("5. En caso de escapar, protegete hasta el amanecer (7 AM)")
    print("Ahora que sabes esto, estas listo para empezar")
    
    input("\nPresiona enter para comenzar... ")
    
    print("\nDespués de una semana eterna de pruebas, tareas y profes enojados (aun somos la seccion favorita del profe carlos), los Junaboys tomaron una decisión: escapar al campo, —“Necesitamos desconectarnos— dijo Brayan, mientras tiraba su mochila al suelo —“Sí, pero ojalá haya señal…”— respondió Matías, más preocupado por el WiFi que por la naturaleza.")

    input("\nPresiona cualquier tecla para continuar: ")

    print("\nEl plan era simple, pasar el fin de semana en casa de Franco, donde se supone solo estaba su padre... Llegando la noche decidieron salir a caminar, camino al bosque, llegaron a una casa abandonada, en medio del bosque")

    desicion1 = input("\n1. Pasar la noche en la casa abandonada\n2. Seguir caminando\n¿Que deben hacer?: ")
    
    if desicion1 == "1" or desicion1 == "2":

        if desicion1 == "2":
            print("\nIntentaron seguir caminando, pero la oscuridad era total y el frío insoportable. Sin darse cuenta, terminaron regresando a la casa abandonada. No tienen otra opción que entrar.")
            input("Presiona enter para entrar a la casa...")

        print("\nDeciden pasar la noche en la casa abandonada, comienzan a buscar cosas para dormir, entre ellas, hojas grades de arbol, leña para el fuego y cosas para abrigarse durante la noche, despues de un largo rato divirtiendose dentro de la casa, les da sueño y se duermen")
        print("\nA las 02:00 AM escuchan ruidos extraños dentro de la casa, un poco asustados, deben decidir que hacer, y RAPIDO!")

        desicion2 = input("\n(1. Alumbrar y ver que es | 2. Salir rapido de la casa y correr) Que decides hacer?: ")

        if desicion2 == "1":

            print(f"\n{personaje_elegido} toma la linterna, la enciende y apunta hacia una extraña silueta... ")
           
            print("██╗  ██╗ █████╗ ███████╗")
            print("██║  ██║██╔══██╗╚══███╔╝")
            print("███████║███████║  ███╔╝ ")
            print("██╔══██║██╔══██║ ███╔╝  ")
            print("██║  ██║██║  ██║███████╗")
            print("╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝")
            print("███╗   ███╗██╗   ██╗███████╗██████╗ ████████╗ ██████╗ ")
            print("████╗ ████║██║   ██║██╔════╝██╔══██╗╚══██╔══╝██╔═══██╗")
            print("██╔████╔██║██║   ██║█████╗  ██████╔╝   ██║   ██║   ██║")
            print("██║╚██╔╝██║██║   ██║██╔══╝  ██╔══██╗   ██║   ██║   ██║")
            print("██║ ╚═╝ ██║╚██████╔╝███████╗██║  ██║   ██║   ╚██████╔╝")
            print("╚═╝     ╚═╝ ╚═════╝ ╚══════╝╚═╝  ╚═╝   ╚═╝    ╚═════╝ ")
           
            print("Te ha matado EL ABOGADO DEL DIABLO")

        elif desicion2 == "2":

            print(f"\n{personaje_elegido} y el resto salen corriendo por donde pueden, corren en direccion hacia la cascada, mientras corren por el bosque, benja resbala con una roca humeda y cae por el barranco.... y muere ensartado")
            print("\nun poco shockeados, no queda otra que seguir avanzando, de todas maneras tenian que escapar de lo que sea que los perseguia y benja no importaba mucho, ya que, ya estaba muerto")
            input("\nPresiona cualquier tecla para continuar: ")

            print(f"\nAgotados, llegan a la cascada, uno de los chicos dice: '{personaje_elegido} tenemos que encontrar un lugar donde pasar la noche, estamos muy lejos de la casa para volver ahora, podemos ir a una cueva mas abajo o buscar algo subiendo por la cascada'")
            desicion3 = input("(1. Subir por la cascada y buscar algo | 2. Bajar a la cueva) Que haras?: ")

            if desicion3 == "1":
                print("Han tratado de subir por la cascada pero pierden el equilibrio y caen")
                
                print("██╗  ██╗ █████╗ ███████╗")
                print("██║  ██║██╔══██╗╚══███╔╝")
                print("███████║███████║  ███╔╝ ")
                print("██╔══██║██╔══██║ ███╔╝  ")
                print("██║  ██║██║  ██║███████╗")
                print("╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝")
                print("███╗   ███╗██╗   ██╗███████╗██████╗ ████████╗ ██████╗ ")
                print("████╗ ████║██║   ██║██╔════╝██╔══██╗╚══██╔══╝██╔═══██╗")
                print("██╔████╔██║██║   ██║█████╗  ██████╔╝   ██║   ██║   ██║")
                print("██║╚██╔╝██║██║   ██║██╔══╝  ██╔══██╗   ██║   ██║   ██║")
                print("██║ ╚═╝ ██║╚██████╔╝███████╗██║  ██║   ██║   ╚██████╔╝")
                print("╚═╝     ╚═╝ ╚═════╝ ╚══════╝╚═╝  ╚═╝   ╚═╝    ╚═════╝ ")

                print("error: Como escalas una cascada? jajaja")
                print("Pd: No se enoje profe carlos esto es una comedia terrorifica >:3")
            
            elif desicion3 == "2":
                print("\nBajan a la cueva y logran refugiarse, la cueva parece ser una buena opcion")
                input("Presiona cualquier tecla para continuar: ")

                print("Un par de horas despues, los Junaboys escuchan ruidos afuera de la cueva, deben decidir si salir a investigar o quedarse en la cueva")
                desicion4 = input("(1. salir a investigar | 2. quedarse en la cueva) Que quieres hacer?: ")

                if desicion4 == "1":

                    print("██╗  ██╗ █████╗ ███████╗")
                    print("██║  ██║██╔══██╗╚══███╔╝")
                    print("███████║███████║  ███╔╝ ")
                    print("██╔══██║██╔══██║ ███╔╝  ")
                    print("██║  ██║██║  ██║███████╗")
                    print("╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝")
                    print("███╗   ███╗██╗   ██╗███████╗██████╗ ████████╗ ██████╗ ")
                    print("████╗ ████║██║   ██║██╔════╝██╔══██╗╚══██╔══╝██╔═══██╗")
                    print("██╔████╔██║██║   ██║█████╗  ██████╔╝   ██║   ██║   ██║")
                    print("██║╚██╔╝██║██║   ██║██╔══╝  ██╔══██╗   ██║   ██║   ██║")
                    print("██║ ╚═╝ ██║╚██████╔╝███████╗██║  ██║   ██║   ╚██████╔╝")
                    print("╚═╝     ╚═╝ ╚═════╝ ╚══════╝╚═╝  ╚═╝   ╚═╝    ╚═════╝ ")

                    print("HAS SIDO ASESINADO POR EL ABOGADO DEL DIABLO")
                elif desicion4 == "2":
                    print("\nlogran observar al abogado del diablo rondando por la zona, resguardarse fue una buena desicion")
                    print("\nSon las 3:33 AM, ahora comienza la verdadera pesadilla... ")
                    input("\nPresiona enter para continuar: ")
                    print("Los chicos deciden avanzar,ya que la zona parece no ser segura, deben reubicarse")
                    print("observan un rio, aunque la corriente es violenta creen que existe la posibilidad de cruzar")
                    
                    desicion5 = input("(1. cruzar el rio | 2. rodear el bosque) que haras?: ")

                    if desicion5 == "1":

                        print("la corriente los arrastra, los Junaboys no lograron salvarse")

                        print("██╗  ██╗ █████╗ ███████╗")
                        print("██║  ██║██╔══██╗╚══███╔╝")
                        print("███████║███████║  ███╔╝ ")
                        print("██╔══██║██╔══██║ ███╔╝  ")
                        print("██║  ██║██║  ██║███████╗")
                        print("╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝")
                        print("███╗   ███╗██╗   ██╗███████╗██████╗ ████████╗ ██████╗ ")
                        print("████╗ ████║██║   ██║██╔════╝██╔══██╗╚══██╔══╝██╔═══██╗")
                        print("██╔████╔██║██║   ██║█████╗  ██████╔╝   ██║   ██║   ██║")
                        print("██║╚██╔╝██║██║   ██║██╔══╝  ██╔══██╗   ██║   ██║   ██║")
                        print("██║ ╚═╝ ██║╚██████╔╝███████╗██║  ██║   ██║   ╚██████╔╝")
                        print("╚═╝     ╚═╝ ╚═════╝ ╚══════╝╚═╝  ╚═╝   ╚═╝    ╚═════╝ ")
                    
                    elif desicion5 == "2":

                        print("\nLos chicos deciden que la corriente del rio es muy peligrosa, rodearan el bosque")
                        print("\nlos Junaboys escuchan pasos a lo lejos que se acercan, quizas los perros puedan asustar al ABOGADO DEL DIABLO.... o no?")
                        
                        desicion6 = input("\n(1. Chiflar | 2. No chiflar) Decide si delatas tu posicion al chiflar: ")

                        if desicion6 == "1":
                            print("\nAl chiflar delatas tu posicion, y el ABOGADO DEL DIABLO corre rapidamente hacia los Junaboys, sera el fin?...")
                            input("Presiona enter para continuar...")
                            print("\nEl ABOGADO DEL DIABLO se frena en seco al escuchar... UN LADRIDO, los Junaboys ven como vienen corriendo tres perros a su rescate, el ABOGADO DEL DIABLO, al escuchar los ladridos sale corriendo, no es el fin, pero estaban a salvo por ahora..")
                            
                        
                        elif desicion6 == "2":
                            print(f"\ndeciden ser cautelozos y mantenerse en silencio, no es momento de correr riesgos, 'Que debemos hacer {personaje_elegido}, el ABOGADO DEL DIABLO esta cerca', susurra alguien")
                            desicion7 = input("\n(1. Esconderse entre las ramas y rocas | 2. Seguir caminando en la dirección opuesta): ")

                            if desicion7 == "1":
                                print("\nAl esconderse, logran ver pasar al ABOGADO DEL DIABLO, todo queda en extremo silencio, el ABOGADO DEL DIABLO se voltea hacia donde estan ustedes, todos sienten un escalofrio por la espalda")
                                input("Presiona enter para continuar: ")
                                print("\nAl no ver ni escuchar nada, el ABOGADO DEL DIABLO sigue su camino, intentando encontrar a los Junaboys,")
                                print(f"\n{personaje_elegido} dice: 'Necesitamos encontrar una forma de vencerlo', 'O escapar' dice otro de los chicos")
                                
                                desicion8 = input("(1. luchar contra EL ABOGADO DEL DIABLO | 2. Escapar) cual sera tu desicion?: ")

                                if desicion8 == "1":

                                    print("\nEntre todos comienzan planear como vencerlo, sin embargo no llegan a ninguna conclusion, están perdiendo tiempo y el Diablo los acorrala.")
                                    
                                    print("██╗  ██╗ █████╗ ███████╗")
                                    print("██║  ██║██╔══██╗╚══███╔╝")
                                    print("███████║███████║  ███╔╝ ")
                                    print("██╔══██║██╔══██║ ███╔╝  ")
                                    print("██║  ██║██║  ██║███████╗")
                                    print("╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝")
                                    print("███╗   ███╗██╗   ██╗███████╗██████╗ ████████╗ ██████╗ ")
                                    print("████╗ ████║██║   ██║██╔════╝██╔══██╗╚══██╔══╝██╔═══██╗")
                                    print("██╔████╔██║██║   ██║█████╗  ██████╔╝   ██║   ██║   ██║")
                                    print("██║╚██╔╝██║██║   ██║██╔══╝  ██╔══██╗   ██║   ██║   ██║")
                                    print("██║ ╚═╝ ██║╚██████╔╝███████╗██║  ██║   ██║   ╚██████╔╝")
                                    print("╚═╝     ╚═╝ ╚═════╝ ╚══════╝╚═╝  ╚═╝   ╚═╝    ╚═════╝ ")

                                elif desicion8 == "2":
                                    print("deciden que escapar hasta el amanecer es la mejor opcion, pero sera dificil. el ABOGADO DEL DIABLO debe estar cerca...")

                                    desicion9 = input("1. tratar de regresar a casa | 2. mantenerse en la zona: ")

                                    if desicion9 == "1":

                                        print("todos estan de acuerdo en que es buena idea regresar a casa con cautela, quizas en casa encuentren algun arma") 
                                        print("Despues de muchas circunstancias desafortunadas, los chicos logran llegar a casa, pero se percatan de algo")
                                        print("El padre de franco no esta en casa...")
                                        input("presiona enter para continuar...")
                                        print("Despues de revisar un poco, los Junaboys logran encontrar objetos para defenderse")

                                        armas = ["Escopeta", "Rifle", "Glock"]
                                        print("los Junaboys logran observar al ABOGADO DEL DIABLO corriendo hacia la casa, deben decidir que hacer Rapido")
                                        desicion10 = input("1. Elegir arma / 2. Escapar de la casa: ")

                                        if desicion10 == "1":

                                            print(f"{armas}")
                                            elegir_arma = input("Que arma escogen los junaboys?: ")
                                            print(f"Has escogido {elegir_arma}")
                                            print("ahora deben decidir....")
                                            
                                            disparar = input("Disparar al ABOGADO DEL DIABLO... o no? (SI/NO): ").strip().lower()
                                            if disparar == "si":
                                                print("Han disparado, el ABOGADO DEL DIABLO ha caido muerto en el cesped...")
                                                print("Es hora de descubrir quien es")
                                                input("Si desea descubrir quien es el ABOGADO DEL DIABLO, presione enter...")
                                                print("los Junaboys se acercan para descubrir que el horroroso rostro del ABOGADO DEL DIABLO no era mas que una mascara")
                                                print("Una vez que quitan la mascara, el rostro del padre de Franco fue revelado")
                                                input()
                                                print("Los Junaboys lloraron con cierta calma al saber que la pesadilla habia acabado, eran las 5:30 AM ")
                                                print("horas mas tarde la policia llegaria a la escena, el ABOGADO DEL DIABLO un asesino serial conocido habia fallecido, quien parecia ser un simple granjero retirado, habia matado a mas de 25 personas")
                                                print("Afortunadamente todo acabo, verdad?")
                                                input()
                                                print("¿Verdad?")
                                                print(" ██████╗ ██████╗ ███╗   ██╗████████╗██╗███╗   ██╗██╗   ██╗ █████╗ ██████╗  █████╗ ")
                                                print("██╔════╝██╔═══██╗████╗  ██║╚══██╔══╝██║████╗  ██║██║   ██║██╔══██╗██╔══██╗██╔══██╗")
                                                print("██║     ██║   ██║██╔██╗ ██║   ██║   ██║██╔██╗ ██║██║   ██║███████║██████╔╝███████║")
                                                print("██║     ██║   ██║██║╚██╗██║   ██║   ██║██║╚██╗██║██║   ██║██╔══██║██╔══██╗██╔══██║")
                                                print("╚██████╗╚██████╔╝██║ ╚████║   ██║   ██║██║ ╚████║╚██████╔╝██║  ██║██║  ██║██║  ██║")
                                                print(" ╚═════╝ ╚═════╝ ╚═╝  ╚═══╝   ╚═╝   ╚═╝╚═╝  ╚═══╝ ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝")
                                            else:
                                                print("Dudaste... El Abogado del Diablo entró a la casa. Nadie sobrevivió.")
                                        else:
                                            print("Intentaron escapar por la puerta trasera, pero el Diablo fue más rápido. Los alcanzó en el patio.")
                                            
                                            print("██╗  ██╗ █████╗ ███████╗")
                                            print("██║  ██║██╔══██╗╚══███╔╝")
                                            print("███████║███████║  ███╔╝ ")
                                            print("██╔══██║██╔══██║ ███╔╝  ")
                                            print("██║  ██║██║  ██║███████╗")
                                            print("╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝")
                                            print("███╗   ███╗██╗   ██╗███████╗██████╗ ████████╗ ██████╗ ")
                                            print("████╗ ████║██║   ██║██╔════╝██╔══██╗╚══██╔══╝██╔═══██╗")
                                            print("██╔████╔██║██║   ██║█████╗  ██████╔╝   ██║   ██║   ██║")
                                            print("██║╚██╔╝██║██║   ██║██╔══╝  ██╔══██╗   ██║   ██║   ██║")
                                            print("██║ ╚═╝ ██║╚██████╔╝███████╗██║  ██║   ██║   ╚██████╔╝")
                                            print("╚═╝     ╚═╝ ╚═════╝ ╚══════╝╚═╝  ╚═╝   ╚═╝    ╚═════╝ ")

                                    elif desicion9 == "2":
                                        
                                        print("Los Junaboys, muertos de cansancio deciden resistir.... pero no fue una buena desicion")
                                        input("")
                                        print("Despues de horas escapando, los chicos no pueden evitar preguntarse, el padre de franco, era un granjero amigable ex abogado que dejo de ejercer en circunstancias desconocidas")
                                        print("y lo mas extraño de todo, ¿porque no lo hemos visto desde que llegamos?....")
                                        input("")
                                        print("de repente de entre los arbustos, una voz familiar parece escucharse...")
                                       
                                        print("HOLA CHICOS...")

                                        print("██╗  ██╗ █████╗ ███████╗")
                                        print("██║  ██║██╔══██╗╚══███╔╝")
                                        print("███████║███████║  ███╔╝ ")
                                        print("██╔══██║██╔══██║ ███╔╝  ")
                                        print("██║  ██║██║  ██║███████╗")
                                        print("╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝")
                                        print("███╗   ███╗██╗   ██╗███████╗██████╗ ████████╗ ██████╗ ")
                                        print("████╗ ████║██║   ██║██╔════╝██╔══██╗╚══██╔══╝██╔═══██╗")
                                        print("██╔████╔██║██║   ██║█████╗  ██████╔╝   ██║   ██║   ██║")
                                        print("██║╚██╔╝██║██║   ██║██╔══╝  ██╔══██╗   ██║   ██║   ██║")
                                        print("██║ ╚═╝ ██║╚██████╔╝███████╗██║  ██║   ██║   ╚██████╔╝")
                                        print("╚═╝     ╚═╝ ╚═════╝ ╚══════╝╚═╝  ╚═╝   ╚═╝    ╚═════╝ ")
                                       
                                        print("los Junaboys nunca fueron encontrados, fueron reportados como desaparecidos y quedaron en el olvido mientras el ABOGADO DEL DIABLO sigue fingiendo ser nada mas que... un amigable granjero")
                            else: 
                                print("\nAl intentar seguir caminando, el Abogado del Diablo los escucha y los alcanza.")
                                
                                print("██╗  ██╗ █████╗ ███████╗")
                                print("██║  ██║██╔══██╗╚══███╔╝")
                                print("███████║███████║  ███╔╝ ")
                                print("██╔══██║██╔══██║ ███╔╝  ")
                                print("██║  ██║██║  ██║███████╗")
                                print("╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝")
                                print("███╗   ███╗██╗   ██╗███████╗██████╗ ████████╗ ██████╗ ")
                                print("████╗ ████║██║   ██║██╔════╝██╔══██╗╚══██╔══╝██╔═══██╗")
                                print("██╔████╔██║██║   ██║█████╗  ██████╔╝   ██║   ██║   ██║")
                                print("██║╚██╔╝██║██║   ██║██╔══╝  ██╔══██╗   ██║   ██║   ██║")
                                print("██║ ╚═╝ ██║╚██████╔╝███████╗██║  ██║   ██║   ╚██████╔╝")
                                print("╚═╝     ╚═╝ ╚═════╝ ╚══════╝╚═╝  ╚═╝   ╚═╝    ╚═════╝ ")

    else:
        print("\nOpción no válida. Te has perdido en el bosque oscuro.")

    print("\n--- FIN DE LA PARTIDA ---")
    input("Presiona Enter para volver al menú principal...")
