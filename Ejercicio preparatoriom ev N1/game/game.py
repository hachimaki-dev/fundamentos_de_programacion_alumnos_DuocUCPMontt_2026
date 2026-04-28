print("Bienvenido a la nueva experiencia Four A")



while True:

    print("Escoge el elemento de tu mascota:\n 1.Fuego\n 2.Agua\n 3.Hierbita\n 4.Aire\n 5.Tierra\n 6.Electricidad ")

    respuesta_de_elemento = int(input("Ingrese el numero de opcion que desee: "))

    if respuesta_de_elemento == 1:

        print("Perfecto el elemento de tu mascota es Fuego")

        nombre_de_mascota = input("Elige el nombre de tu mascota: ")

        print(f"¡¡Se han desordenado las opciones de los elementos!!\nDeberas elegir una opcion para saber el\ncontrincante de {nombre_de_mascota}\n¡¡Cuidado, sera al azar!!")

        contrincante_al_azar = int(input("Ingrese un numero de el 1 al 6: "))

        if contrincante_al_azar == 1:

            print(f"A {nombre_de_mascota} le ha tocado contra el elemento de Electricidad")

            print(f"Luego de una larga batalla de {nombre_de_mascota}\nHubo un empate debido a que\nambos son igual de poderosos.\n \nFin de la batalla.")

        elif contrincante_al_azar == 2:

            print(f"A {nombre_de_mascota} le ha tocado contra elemento de Tierra")

            print(f"Luego de una larga batalla de {nombre_de_mascota}\nha perdido ya que\ntierra lo ha derrotado\nArriba, a la proxima ven mas fuerte\nFin de la batalla.")

        elif contrincante_al_azar == 3:

            print(f"A {nombre_de_mascota} le ha tocado contra elemento de Aire")

            print(f"Luego de una larga batalla de {nombre_de_mascota}\n{nombre_de_mascota} ha ganado la batalla\ncontra el elemento de aire.\n \nFin de la batalla.")

        elif contrincante_al_azar == 4:

            print(f"A {nombre_de_mascota} le ha tocado contra elemento de Agua")

            print(f"Luego de una larga batalla de {nombre_de_mascota}\nHa perdido ya que el agua a apagado\nla llama de {nombre_de_mascota}.\n \nFin de la batalla.")

        elif contrincante_al_azar == 5:

            print(f"A {nombre_de_mascota} le ha tocado contra elemento de Fuego")

            print(f"Luego de una larga batalla de {nombre_de_mascota}\nHubo un empate debido a que\nambos son igual de poderosos.\n \nFin de la batalla.")

        elif contrincante_al_azar == 6:

            print(f"A {nombre_de_mascota} le ha tocado contra elemento de Hierbita")

            print(f"Luego de una larga batalla de {nombre_de_mascota}\nA incendiado a Hierbita\nhasta dejarlo en cenizas.\n \nFin de la batalla.")

        else:

            print("Ingrese una opcion valida.")

            

        break



    elif respuesta_de_elemento == 2:

        print("Perfecto el elemento de tu mascota es Agua")

        nombre_de_mascota = input("Elige el nombre de tu mascota: ")

        print(f"¡¡Se han desordenado las opciones de los elementos!!\nDeberas elegir una opcion para saber el\ncontrincante de {nombre_de_mascota}\n¡¡Cuidado, sera al azar!!")

        contrincante_al_azar = int(input("Ingrese un numero de el 1 al 6: "))

        if contrincante_al_azar == 1:

            print(f"A {nombre_de_mascota} le ha tocado contra el elemento de Electricidad")

            print(f"Luego de una larga batalla de {nombre_de_mascota}\nHa sido derrotado por\nuna descarga electrica.\nNos vemos en la proxima batalla. \nFin de la batalla.")

        elif contrincante_al_azar == 2:

            print(f"A {nombre_de_mascota} le ha tocado contra elemento de Tierra")

            print(f"Luego de una larga batalla de {nombre_de_mascota}\nHa salido victorioso y\nha ahogado a la tierra\nFelicidades.\nFin de la batalla.")

        elif contrincante_al_azar == 3:

            print(f"A {nombre_de_mascota} le ha tocado contra elemento de Aire")

            print(f"Luego de una larga batalla de {nombre_de_mascota}\nHan empatado ya que\nambos tienen fuerzas iguales.\n \nFin de la batalla.")

        elif contrincante_al_azar == 4:

            print(f"A {nombre_de_mascota} le ha tocado contra elemento de Agua")

            print(f"Luego de una larga batalla de {nombre_de_mascota}\nHan empatado ya que\nambos tienen fuerzas iguales.\n \nFin de la batalla.")

        elif contrincante_al_azar == 5:

            print(f"A {nombre_de_mascota} le ha tocado contra elemento de Fuego")

            print(f"Luego de una larga batalla de {nombre_de_mascota}\nHa desaparecido la llama del fuego\n{nombre_de_mascota} ha demostrado ser fuerte.\n \nFin de la batalla.")

        elif contrincante_al_azar == 6:

            print(f"A {nombre_de_mascota} le ha tocado contra elemento de Hierbita")

            print(f"Luego de una larga batalla de {nombre_de_mascota}\nLa hierba a absorbido la energia de {nombre_de_mascota}\nhasta dejarlo sin energia.\n \nFin de la batalla.")

        else:

            print("Ingrese una opcion valida.")

            

        break

    elif respuesta_de_elemento == 3:

        print("Perfecto el elemento de tu mascota es Hierbita")

        nombre_de_mascota = input("Elige el nombre de tu mascota: ")

        print(f"¡¡Se han desordenado las opciones de los elementos!!\nDeberas elegir una opcion para saber el\ncontrincante de {nombre_de_mascota}\n¡¡Cuidado, sera al azar!!")

        contrincante_al_azar = int(input("Ingrese un numero de el 1 al 6: "))

        if contrincante_al_azar == 1:

            print(f"A {nombre_de_mascota} le ha tocado contra el elemento de Electricidad")

            print(f"Luego de una larga batalla de {nombre_de_mascota}\nHubo un empate debido a que\nambos son igual de poderosos.\n \nFin de la batalla.")

        elif contrincante_al_azar == 2:

            print(f"A {nombre_de_mascota} le ha tocado contra elemento de Tierra")

            print(f"Luego de una larga batalla de {nombre_de_mascota}\nha ganado {nombre_de_mascota}\ny ha atado a la tierra\nfelicidades has ganado esta batalla\nFin de la batalla.")

        elif contrincante_al_azar == 3:

            print(f"A {nombre_de_mascota} le ha tocado contra elemento de Aire")

            print(f"Luego de una larga batalla de {nombre_de_mascota}\n{nombre_de_mascota} ha perdido y a volado por los cielos\ncontra el elemento de aire.\n \nFin de la batalla.")

        elif contrincante_al_azar == 4:

            print(f"A {nombre_de_mascota} le ha tocado contra elemento de Agua")

            print(f"Luego de una larga batalla de {nombre_de_mascota}\nHa ganado y a absorbido\na su contrincante.\n \nFin de la batalla.")

        elif contrincante_al_azar == 5:

            print(f"A {nombre_de_mascota} le ha tocado contra elemento de Fuego")

            print(f"Luego de una larga batalla de {nombre_de_mascota}\nHa sido incinerada\ncontra el elemento de fuego \nFin de la batalla.")

        elif contrincante_al_azar == 6:

            print(f"A {nombre_de_mascota} le ha tocado contra elemento de Hierbita")

            print(f"Luego de una larga batalla de {nombre_de_mascota}\nHubo un empate debido a que\nambos son igual de poderosos.\n \nFin de la batalla.")

        else:

            print("Ingrese una opcion valida.")

            

        break

    elif respuesta_de_elemento == 4:    

        print("Perfecto el elemento de tu mascota es Aire")

        nombre_de_mascota = input("Elige el nombre de tu mascota: ")

        print(f"¡¡Se han desordenado las opciones de los elementos!!\nDeberas elegir una opcion para saber el\ncontrincante de {nombre_de_mascota}\n¡¡Cuidado, sera al azar!!")

        contrincante_al_azar = int(input("Ingrese un numero de el 1 al 6: "))

        if contrincante_al_azar == 1:

            print(f"A {nombre_de_mascota} le ha tocado contra el elemento de Electricidad")

            print(f"Luego de una larga batalla de {nombre_de_mascota}\nHubo una derrota\nambos son poderosos pero electricidad te paralizo.\n \nFin de la batalla.")

        elif contrincante_al_azar == 2:

            print(f"A {nombre_de_mascota} le ha tocado contra elemento de Tierra")

            print(f"Luego de una larga batalla de {nombre_de_mascota}\nha perdido {nombre_de_mascota}\ncontra tierra \nya que tierra ocupo un poder exepcional\nFin de la batalla.")

        elif contrincante_al_azar == 3:

            print(f"A {nombre_de_mascota} le ha tocado contra elemento de Aire")

            print(f"Luego de una larga batalla de {nombre_de_mascota}\n{nombre_de_mascota} ha perdido y a volado por los cielos\ncontra el elemento de aire.\n \nFin de la batalla.")

        elif contrincante_al_azar == 4:

            print(f"A {nombre_de_mascota} le ha tocado contra elemento de Agua")

            print(f"Luego de una larga batalla de {nombre_de_mascota}\nHubo un empate debido a que\nambos son igual de poderosos.\n \nFin de la batalla.")

        elif contrincante_al_azar == 5:

            print(f"A {nombre_de_mascota} le ha tocado contra elemento de Fuego")

            print(f"Luego de una larga batalla de {nombre_de_mascota}\nHa sido derrotada\nya que avivo el elemento de fuego \nFin de la batalla.")

        elif contrincante_al_azar == 6:

            print(f"A {nombre_de_mascota} le ha tocado contra elemento de Hierbita")

            print(f"Luego de una larga batalla de {nombre_de_mascota}\ngano ya que hizo volar\nhirbita a los cielos.\n \nFin de la batalla.")

        else:

            print("Ingrese una opcion valida.")

            

        break

    elif respuesta_de_elemento == 5:    

        print("Perfecto el elemento de tu mascota es Tierra")

        nombre_de_mascota = input("Elige el nombre de tu mascota: ")

        print(f"¡¡Se han desordenado las opciones de los elementos!!\nDeberas elegir una opcion para saber el\ncontrincante de {nombre_de_mascota}\n¡¡Cuidado, sera al azar!!")

        contrincante_al_azar = int(input("Ingrese un numero de el 1 al 6: "))

        if contrincante_al_azar == 1:

            print(f"A {nombre_de_mascota} le ha tocado contra el elemento de Electricidad")

            print(f"Luego de una larga batalla de {nombre_de_mascota}\nHubo una victoria\neres repelente contra los ataques de tu contrincante\nfue una pelea digna y... has ganado.\n\nFin de la batalla.")

        elif contrincante_al_azar == 2:

            print(f"A {nombre_de_mascota} le ha tocado contra elemento de Tierra")

            print(f"Luego de una larga batalla de {nombre_de_mascota}\nHubo un empate debido a que\nambos son igual de poderosos\ny sus fuerzas son similares.\n\nFin de la batalla.")

        elif contrincante_al_azar == 3:

            print(f"A {nombre_de_mascota} le ha tocado contra elemento de Aire")

            print(f"Luego de una larga batalla de {nombre_de_mascota}\n{nombre_de_mascota} has ganado y as repelido todos los ataques\nen contra el elemento de aire\ny a podido derrotarlo\n\nFin de la batalla.")

        elif contrincante_al_azar == 4:

            print(f"A {nombre_de_mascota} le ha tocado contra elemento de Agua")

            print(f"Luego de una larga batalla de {nombre_de_mascota}\nah sido derrotado por agua\nambos son igual de poderosos\npero agua te ha arrastrado hasta su trampa\ny te vencio\n\nFin de la batalla.")

        elif contrincante_al_azar == 5:

            print(f"A {nombre_de_mascota} le ha tocado contra elemento de Fuego")

            print(f"Luego de una larga batalla de {nombre_de_mascota}\nHas ganado\nhas sofocado al elemento de fuego\ny conseguiste derrotarlo\n\nFin de la batalla.")

        elif contrincante_al_azar == 6:

            print(f"A {nombre_de_mascota} le ha tocado contra elemento de Hierbita")

            print(f"Luego de una larga batalla de {nombre_de_mascota}\nhas sido derrotado por hierbita\nah ocupado tu poder en contra tuya\ny a podido derrotarte\n\nFin de la batalla.")

        else:

            print("Ingrese una opcion valida.")

            

        break

    elif respuesta_de_elemento == 6:

        print("Perfecto el elemento de tu mascota es Electricidad")

        nombre_de_mascota = input("Elige el nombre de tu mascota: ")

        print(f"¡¡Se han desordenado las opciones de los elementos!!\nDeberas elegir una opcion para saber el\ncontrincante de {nombre_de_mascota}\n¡¡Cuidado, sera al azar!!")

        contrincante_al_azar = int(input("Ingrese un numero de el 1 al 6: "))

        if contrincante_al_azar == 1:

            print(f"A {nombre_de_mascota} le ha tocado contra el elemento de Electricidad")

            print(f"Luego de una larga batalla de {nombre_de_mascota}\nHubo un empate debido a que\nambos son igual de poderosos.\n \nFin de la batalla.")

        elif contrincante_al_azar == 2:

            print(f"A {nombre_de_mascota} le ha tocado contra elemento de Tierra")

            print(f"Luego de una larga batalla de {nombre_de_mascota}\nha perdido {nombre_de_mascota}\ncontra tierra \nya que tierra ocupo un poder exepcional\nFin de la batalla.")

        elif contrincante_al_azar == 3:

            print(f"A {nombre_de_mascota} le ha tocado contra elemento de Aire")

            print(f"Luego de una larga batalla de {nombre_de_mascota}\n{nombre_de_mascota} has ganado y volado por los cielos\ncontra el elemento de aire\npara darle un ataque fulminante\n\nFin de la batalla.")

        elif contrincante_al_azar == 4:

            print(f"A {nombre_de_mascota} le ha tocado contra elemento de Agua")

            print(f"Luego de una larga batalla de {nombre_de_mascota}\nhas ganado en contra de aire\nya que tu poder se incrementa con el agua.\n\nfin de la batalla")

        elif contrincante_al_azar == 5:

            print(f"A {nombre_de_mascota} le ha tocado contra elemento de Fuego")

            print(f"Luego de una larga batalla de {nombre_de_mascota}\nHa sido derrotada\nya que avivo el elemento de fuego\ny un ataque imposible de detener\nte fulmino tus fuerzas\n\nFin de la batalla.")

        elif contrincante_al_azar == 6:

            print(f"A {nombre_de_mascota} le ha tocado contra elemento de Hierbita")

            print(f"Luego de una larga batalla de {nombre_de_mascota}\nhas perdido ya que hierbita\nrepeleto todos tus ataques\ny te a dejado sin fuerzas\n\nfin de la batalla")

        else:

            print("Ingrese una opcion valida.")

            

        break

    else:

        print("Escoga un elemento valido")











