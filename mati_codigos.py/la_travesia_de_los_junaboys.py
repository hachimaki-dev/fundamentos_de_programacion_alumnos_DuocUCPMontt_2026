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

print("")
print("            ☠ LOS JUNABOYS ☠")
print("         nadie debió entrar...")
print("       y ahora... no pueden salir")
print("░░░░░░░░░░░░░░░░░░░░MENU░░░░░░░░░░░░░░░░░░░░░░")

personajes = ["Franco", "Matias", "Brayan"]
vidas_utilizadas= 0
vidas_maximas = 5


print("1. escoger personaje")
print("2. crear personaje")
print("3. salir")

eleccion_usuario= input("Elige una opcion (1/2/3): ")

while vidas_utilizadas < vidas_maximas:
    
    if eleccion_usuario == "1":
        print(f"{personajes}")
        
        personaje_elegido = input("escoger personaje: ").upper()
    
    elif eleccion_usuario == "2":
        
        personaje_elegido= input("Ingrese el nombre de su personaje: ").upper()

    elif eleccion_usuario == "3":
        print("hasta pronto")
        break

    else:
        print("opcion invalida")
        

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

    desicion1= int(input("\n1. Pasar la noche en la casa abandonada|2. seguir caminando)Que deben hacer?: "))
    if desicion1 == 1:

        print("\nDeciden pasar la noche en la casa abandonada, comienzan a buscar cosas para dormir, entre ellas, hojas grades de arbol, leña para el fuego y cosas para abrigarse durante la noche, despues de un largo rato divirtiendose dentro de la casa, les da sueño y se duermen")

        print("\nA las 2am escuchan ruidos extraños dentro de la casa, un poco asustados, deben decidir que hacer, y RAPIDO!")

        desicion2= int(input("\n(1. Alumbrar y ver que es|2. Salir rapido de la casa y correr) Que decides hacer?: "))

        if desicion2 == 1:
            print(f"\n{personaje_elegido} toma la linterna, la enciende y apunta hacia una extraña silueta... ")

            vidas_utilizadas += 1

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

            print("Te ha matado EL DIABLO")
            
            break
        
        elif desicion2 == 2:
            print(f"\n{personaje_elegido} y el resto salen corriendo por donde pueden, corren en direccion hacia la cascada, mientras corren por el bosque, benja resbala con una roca humeda y cae por el barranco y muere ensartado")

            print("\nun poco shockeados, no queda otra que seguir avanzando, de todas maneras tenian que escapar de lo que sea que los perseguia y benja no importaba mucho, ya que, ya estaba muerto")

            input("\nPresiona cualquier tecla para continuar: ")

            print(f"\nAgotados, llegan a la cascada, uno de los chicos dice: '{personaje_elegido} tenemos que encontrar un lugar donde pasar la noche, estamos muy lejos de la casa para volver ahora, podemos ir a una cueva mas abajo o buscar algo subiendo por la cascada'")

            desicion3= int(input("(1. Subir por la cascada y buscar algo|2. Bajar a la cueva) Que haras?: "))

            if desicion3 == 1:
                print("Han tratado de subir por la cascada pero pierden el equilibrio y caen")
            
                vidas_utilizadas += 1
                
            elif desicion3 == 2:
                print("\nBajan a la cueva y logran refugiarse, la cueva parece ser una buena opcion")
                
                input("Presiona cualquier tecla para continuar: ")

                print("Un par de horas despues, los Junaboys escuchan ruidos afuera de la cueva, deben decidir si salir a investigar o quedarse en la cueva")

                desicion4 = int(input("(1. salir a investigar |2. quedarse en la cueva) Que quieres hacer?: "))

                if desicion4 == 1:
                    print("HAS SIDO ATACADO POR EL DIABLO")
                    vidas_utilizadas += 1
                elif desicion4 == 2:
                    print("\nlogran observar al diablo rondando por la zona, resguardarse fue una buena desicion")

                    print("\nSon las 3:33 AM, ahora comienza la verdadera pesadilla... ")

                    input("\nPresiona enter para continuar: ")

                    print("Los chicos deciden avanzar,ya que la zona parece no ser segura, deben reubicarse")

                    print("los chicos observan un rio, aunque la corriente es violenta creen que existe la posibilidad de cruzar")

                    desicion5= int(input("(1. cruzar el rio 2. rodear el bosque) que haras?: "))

                    if desicion5 == 1:
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

                        break

                    elif desicion5 == 2:
                        print("\nLos chicos deciden que la corriente del rio es muy peligrosa, rodearan el bosque")

                        print("\nlos Junaboys escuchan pasos a lo lejos que se acercan, quizas los perros puedan asustar al diablo.... o no?")

                        desicion6= int(input("\n(1. Chiflar|2. No chiflar) Decide si delatas tu posicion al chiflar: "))

                        if desicion6 == 1:
                            print("\nAl chiflar delatas tu posicion, y el DIABLO corre rapidamente hacia los Junaboys, sera el fin?...")

                            input("Presiona enter para continuar...")

                            print("\nEl DIABLO se frena en seco al escuchar... un ladrido, los Junaboys ven como vienen corriendo los tres perros a su rescate, el DIABLO, al escuchar los ladridos sale corriendo, no es el fin, pero estaban a salvo por ahora..")
                            
                        elif desicion6 == 2:
                            print(f"\ndeciden ser cautelozos y mantenerse en silencio, no es momento de correr riesgos, 'Que debemos hacer {personaje_elegido}, el DIABLO esta cerca', susurra alguien")

                            desicion7= int(input("\n(1. Esconderse entre las ramas y rocas|2. Seguir caminando en la direccion opuesta) debes decidir que hacer, y RAPIDO, el tiempo no espera a nadie... "))

                            if desicion7 == 1:
                                print("\nAl esconderse, logran ver pasar al DIABLO, todo queda en extremo silencio, el DIABLO se voltea hacia donde estan ustedes, todos sienten un escalofrio por la espalda")

                                input("Presiona enter para continuar: ")

                                print("\nAl no ver ni escuchar nada, el DIABLO sigue su camino, intentando encontrar a los Junaboys,")

                                print(f"\n{personaje_elegido} dice: 'Necesitamos encontrar una forma de vencerlo', 'O escapar' dice otro de los chicos")

                                desicion8= int(input("(1. Vencer al DIABLO|2. Escapar) cual sera tu desicion?: "))

                                if desicion8 == 1:
                                    print("\nEntre todos comienzan planear como vencerlo")