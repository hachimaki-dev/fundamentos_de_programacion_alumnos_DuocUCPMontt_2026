palabras_correctas = ["PYTHON", "CODIGO", "LOGICA", "BUCLE", "LISTA", "VARIABLE", "CADENA", "ENTERO", "FUNCION", "CONSOLA", "OBJETO", "RECURSO", "PROCESO", "TECLADO", "PANTALLA"]
palabras_desordenadas = ["YPHTNO", "GIDOCO", "CIALGO", "ELUBC", "STILA", "BAVALRIE", "NEDACA", "REETNO", "COINFUN", "OLSACON", "TEJOBO", "SRUOCRE", "SCEOPRO", "DALOTEC", "TALLAPAN"]

print("Bienvenido al juego") #
print("Instrucciones: Palabra desordenada , debes ordenarla , dependiendo de la dificultad tendras mas o menos vidas! ") #
print("\n") #salto de linea para que se vea mas estetico
nombre_jugador = input("Ingrese su nombre: ")
#declaramos nuestras variables , empezamos con dos variables con un string vacio para rellenarlos mas tarde , y opcion_dificultad y vidas en 0 
palabra_seleccionada = ""
palabra_correcta = ""
opcion_dificultad = 0
vidas = 0
# Se empieza con un while ya que debe de ser un ciclo hasta que se cumpla cierta condicion , se da un input para que jugador escoja la dificultad y dependiendo de la dificultad escogida se entrega una cierta cantidad de vidas disponibles , desde el 
while True:
    modo_de_juego = int(input("Elija su modo de juego:\n1. Modo Libre (Una palabra)\n2. Modo Clásico (Todas las palabras)\n3. Salir del juego\n"))
    if modo_de_juego == 1 or modo_de_juego == 2:
        while True:
            opcion_dificultad = int(input("Dificultad: \n1. Fácil\n2. Medio\n3. Difícil\n4. Extremo\n"))
            if opcion_dificultad == 1:
                dificultad = "Fácil"
                vidas = 10
                break
            elif opcion_dificultad == 2:
                dificultad = "Medio"
                vidas = 5
                break
            elif opcion_dificultad == 3:
                dificultad = "Difícil"
                vidas = 3
                break
            elif opcion_dificultad == 4:
                dificultad = "Extremo"
                vidas = 1
                break
            else:
                print("Por favor ingrese una opción válida")
        if modo_de_juego == 1:
            print("----------------------------------------")
            print("Modo de Juego: Modo Libre (Una palabra)")
            print(f"Dificultad: {dificultad}")
            print(f"Vidas: {vidas}")
            print("----------------------------------------")
            print("Presione ENTER para comenzar")
            input()

            # incompleto
            indice_palabra = int(input(f"Ingrese un numero del 1 al {len(palabras_desordenadas)}: "))
            palabra_seleccionada = palabras_desordenadas[indice_palabra-1] # Restamos 1 porque la lista comienza desde el 0 y ahora empieza desde 1 al 15
            palabra_correcta = palabras_correctas[indice_palabra-1]
            while vidas > 0:
                respuesta_usuario = input(f"Ordena la palabra {palabra_seleccionada}: ").upper()
                if respuesta_usuario == palabra_correcta:
                    print(f"¡Correcto! ¡Felicidades {nombre_jugador}!")
                    # seguir jugando?
                    break
                else:
                    vidas -= 1
                    print("¡Incorrecto!")
                    print(f"Vidas restantes: {vidas}")
                    pista = "" # Inicializado aqui para que no se concatene cada vez que se pierde una vida
                    for letra in range(len(palabra_correcta)):
                        if letra % 2 == 0: # Para mostrar solo letra por medio
                            pista = pista + palabra_correcta[letra]
                        else:
                            pista = pista + "_"
                    if dificultad == "Fácil": # Si elige dificultad fácil, se ve la pista cada vez que el usuario se equivoque
                        print(f"Pista: {pista}")
                    elif dificultad == "Medio": # Se ve una pista fome cuando queden 2 vidas y pista buena cuando quede 1 vida
                        if vidas == 2: # Posicion de la palabra de la lista de palabra_correcta empieza desde el 0
                            print(f"Pista: La palabra comienza con {palabra_correcta[0]}")
                        elif vidas == 1:
                            print(f"Pista: {pista}")
                    elif dificultad == "Difícil" and vidas == 1: # Solo se ve la pista fome cuando queda 1 vida
                        print(f"Pista: La palabra comienza con {palabra_correcta[0]}")
                    #no se que pasa que no muestra la pista
                    # vidas == 0??
            break # jugar otra vez o salir

        elif modo_de_juego == 2:
            print("----------------------------------------")
            print("Modo de Juego: Modo Clásico (Todas las palabras)")
            print(f"Dificultad: {dificultad}")
            print(f"Vidas: {vidas}")
            # puntaje
            print("----------------------------------------")
            print("Presione ENTER para comenzar")
            input()

            print(f"Total de palabras :{len(palabras_desordenadas)}: ")
            palabra_seleccionada = palabras_desordenadas[indice_palabra-1] # Restamos 1 porque la lista comienza desde el 0 y ahora empieza desde 1 al 15
            palabra_correcta = palabras_correctas[indice_palabra-1]
            while vidas > 0:
                respuesta_usuario = input(f"Ordena la palabra {palabra_seleccionada}: ").upper()
                if respuesta_usuario == palabra_correcta:
                    print(f"¡Correcto! ¡Felicidades {nombre_jugador}!")
                    # seguir jugando?
                    break
                else:
                    vidas -= 1
                    print("¡Incorrecto!")
                    print(f"Vidas restantes: {vidas}")
                    pista = "" # Inicializado aqui para que no se concatene cada vez que se pierde una vida
                    for letra in range(len(palabra_correcta)):
                        if letra % 2 == 0: # Para mostrar solo letra por medio
                            pista = pista + palabra_correcta[letra]
                        else:
                            pista = pista + "_"
                    if dificultad == "Fácil": # Si elige dificultad fácil, se ve la pista cada vez que el usuario se equivoque
                        print(f"Pista: {pista}")
                    elif dificultad == "Medio": # Se ve una pista fome cuando queden 2 vidas y pista buena cuando quede 1 vida
                        if vidas == 2: # Posicion de la palabra de la lista de palabra_correcta empieza desde el 0
                            print(f"Pista: La palabra comienza con {palabra_correcta[0]}")
                        elif vidas == 1:
                            print(f"Pista: {pista}")
                    elif dificultad == "Difícil" : # Solo se ve la pista fome cuando queda 1 vida
                        print(f"Pista: La palabra comienza con {palabra_correcta[0]}")
                    #QUE NO SE ME OLVIDA COLOCAR LA AND
                    # vidas == 0??
            break # jugar otra vez o salir

            # incompleto

    elif modo_de_juego == 3:
        break
    else:
        print("Ingrese una opcion válida")
