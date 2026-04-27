print("\n")
print("╔══════════════════════╗")
print("║    Después de ti     ║")
print("╚══════════════════════╝")
print("\n")

jugar = input("Deseas jugar? Si/No\nIngresa tu elección: ").strip().lower()
while jugar == "si":
    char = ["Alberto Magno", "Pilar Trinidad", "Brayan", "Matias"]
    eventos_dia1 = [f"Era un día lluvioso como de costumbre en Puerto Montt.", "Se podía ver el disgusto de varias personas, pero a pesar de todo había un chico sonriendo como nunca.", "???: Ahhh me encanta esto, es tan relajante.", "???: ALBERTOOO ¿Que haces afuera con está lluvia torrencial?, al menos lleva un paraguas.", "Alberto: Ahh si, me encanta la lluvia, no te preocupes matias.", "Matias: Pero te vas a enfermar amigo", "Ya me voy a mi casa así que no te preocupes."]

    for evento in eventos_dia1:
        print(evento)
        input("Presiona Enter...")
    weon = "amigo" 

    tiempo = ["Mañana", "Tarde", "Madrugada"]

    print("Demoraste 20 minutos en llegar a tu casa")
    cigarros_fumados = 0
    tristeza = 0
    felicidad = 0
    ejercicio = 0
    amor = 0
    cansancio = 0
    ansiedad = 0
    tiempo_diario = 0
    dia = 1
    dias_totales = 5
    ida_biblioteca = False

    print("Ya llegue a casa, que debería de hacer?")
    tiempo_diario += 15


    while tiempo_diario < 24:
            menu_diario = input("Opciones disponibles:\nA. Jugar en la computadora\nB. Hacer aseo\nC. Salir a fumar\nD. Ver la hora\nF. Ir a dormir (acaba el día)\nIngrese su elección: ").strip().lower()
            if menu_diario == "a":
                print("Fuiste a jugar en la computadora a valorant por 4 horas")
                felicidad += 5
                cansancio += 2
                tiempo_diario += 4

            elif menu_diario == "b":
                print("Hiciste el aseo por 2 horas, quedaste algo agotado.")
                cansancio += 1
                tiempo_diario += 2

            elif menu_diario == "c":
                print("Decidiste salir a fumar por una hora, te sientes más relajado.")
                cansancio += 1
                tiempo_diario += 1
                cigarros_fumados += 1
                continuar_fumando = input("Deseas fumar otro? Si/No\nIngrese su elección: ").strip().lower()
                if continuar_fumando == "si":
                    print("Saliste a fumar por una hora más, te sientes más relajado.")
                    cansancio += 1
                    tiempo_diario += 1
                    cigarros_fumados += 1
                elif continuar_fumando == "no":
                    print("Decidiste no fumar más, quizás esto a futuro sea la mejor opción.")
                else:
                    print("Ingresa una opción valida.")

            elif menu_diario == "d":
                print(f"Son las {tiempo_diario}:20 de la {tiempo[1]}.")

            elif menu_diario == "f":
                print("Decidiste ir a dormir.")
                cansancio -= 2
                break
            else:
                print("Ingresa una opción valida")
                continue

    tiempo_diario = 0
    tiempo_diario += 8

    print(f"Hoy es el día 2 y son las {tiempo_diario} de la {tiempo[0]}")
    eventos_dia2 = ["Te levantas de la cama y empiezas a vestirte", "Sales de la habitación y te diriges a la cocina.", "Decides prepararte un sandwich de huevo con queso y jamón.", "Ahora estás listo para ir a estudiar", "Llegas a la universidad a vivir un día monotono como ya estás acostumbrado.", "Alberto: Otro día más deprimente que el anterior."]

    for evento in eventos_dia2:
        print(evento)
        input("Presiona Enter...")
    while True:
            donde_ir = input("Que quieres hacer?\nA. Sala de clases\nB. Biblioteca\nC. Llamar a tus amigos\nIngresa tu elección: ").strip().lower()
            if donde_ir == "a":
                print("Te diriges hacia el salón de clases")
                print("La clase ha durado 2 horas.")
                tiempo_diario += 2
                cansancio += 1
                break

            elif donde_ir == "b":
                print("Te diriges hacia la biblioteca")
                print("Nunca lees ningún libro, pero está vez quizás podrías intentarlo.")
                ida_biblioteca = True
                leer = input("Deseas leer algún libro? Si/No\nIngresa tu elección: ").strip().lower()
                if leer == "si":
                    print("Hay muchos libros que leer, pero podría probar con alguno de filosofia o deporte.")
                    print("Ves a una chica de cabello rubio leeyendo un libro, nunca habías visto a una chica tan linda en toda tu vida.")
                    hablar_chica = input("Quieres acercarte a hablarle? Si/No\nIngresa tu elección: ")
                    if hablar_chica == "si":
                        print("Te acercas a hablarle, algo nervioso.")
                        print("Alberto: Oye cual es ese libro que estás leyendo?\n???: Este libro se llama Cumbres borrascosas\nAlberto: y de que trata?")
                    elif hablar_chica == "no":
                        print("No te atreviste a hablarle, te sientes algo triste.")
                        tristeza += 1
                        ansiedad += 1
                    break
                elif leer == "no":
                    print("Pues solo viniste a mirar y te vas.")
                    break

            elif donde_ir == "c":
                print("Decides llamar a tus amigos, ninguno contesta.")
                print("Así que vas al salón de clases.")
                print("La clase ha durado 2 horas, estás algo triste porque tus amigos no respondieron.")
                tiempo_diario += 2
                tristeza += 2
                cansancio += 1

                break

            else:
                print("Ingresa una opción valida.")
                continue
            
    print(f"En total fumaste {cigarros_fumados} veces")

    if cigarros_fumados > 5:
        print("Beto muere de cáncer pulmonar.")

    elif ansiedad > 5:
        print("Beto muere de ansiedad")

    elif tristeza > 10:
        print("Beto no pudo más, decidio acabar con todo.")

    elif tristeza > 5:
        print("Beto fue diagnosticado con depresión, aún así la vida sigue, pero es dificil.")

    elif amor > 5 and tristeza > 10:
        print("Tenían muchos planes a futuro, pero no pudiste más y acabaste con todo.")

    elif amor > 10:
        print("Decidiste casarte con pilar, y hacerla la mujer más feliz del mundo.")


    else:
        print("Ni fu ni fa, la vida sigue y ya.")

    if ida_biblioteca == True:
        print("Pilar: Jamás olvidare la primera vez que te vi, estabas ahí en la biblioteca como un corderito perdido.")
    else:
        print("Me hubiera gustado haberte conocido un poco antes...")
    #disculpe que el programa este tan vacio, sigo armando la estructura del juego, pero me gustaría terminarlo en un futuro.