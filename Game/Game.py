print("") #Titulo
vidas = 5
puntaje = 0
print("------Bienvenido al sistema de Calculos matematicos------")
print("Porfavor usuario presentese")
nombre = input("Tu nombre es?: ")
print(f"¡¡¡¡¡¡Bienvenido {nombre}!!!!!! Preparate para subir de nivel en tus matematicas!")
print("")
print("Etapa 1 (Sumas Y Restas) ")
print("Nivel 1: Sumas")
print("Esta está facilita \n99 + 10")

while vidas > 0:
    
    while vidas > 0:
        respuesta_1 = int(input("Por favor ingresa la solución: "))
        if respuesta_1 == 109:
            print("Felicidades acertaste la primera pregunta (+1 punto)")
            puntaje = puntaje + 1
            print(f"Llevas un total de {puntaje} puntos")
            break
        
        else:
            print("Es en serio? En la primera? Pues no lo siento respuesta incorrecta (-1 vida)")
            vidas = vidas - 1
            print(f"vidas restantes {vidas}")
            continue
    if vidas <= 0:
        print(f"Lo siento {nombre} has perdido todas tus vidas, buena suerte la proxima")
        break
    
    print("")
    print("Nivel 2: Restas")
    print("A ver esta? \n188 - 55")
    while vidas > 0:
        respuesta_2 = int(input("Por favor ingresa la solución: "))
        if respuesta_2 == 133:
            print("Felicidades acercaste la segunda pregunta pregunta (+1 punto)")
            puntaje = puntaje + 1
            print(f"Llevas un total de {puntaje} puntos")
            break

        else:
            print("Bueno esta estaba un poco mas complicada, lo siento respuesta incorrecta (-1 vida)")
            vidas = vidas - 1
            print(f"Vidas restantes {vidas}")
            continue
    if vidas <= 0:
        print("Has perdido todas tus vidas, buena suerte la proxima")
        break
           
    #actividad 2
    print("")
    print("Etapa 2: (Multiplicación y División)")
    print("Nivel 1: Multiplicación")
    print("Veamos si te aprendiste las tablas en el colegio \n9x5")
    while vidas > 0:
        respuesta_4 = int(input("Ingresa la solución: "))
        if respuesta_4 == 45:
            print("Respuesta correcta haz ganado (+1 punto)")
            puntaje = puntaje + 1
            print(f"Llevas un total de {puntaje} puntos")
            break
        else:
            print("Vamos piensa esa no era, solamente tienes que sumar el numero 9, 5 veces (-1 vida)")
            vidas = vidas - 1
            print(f"Haz perdido una vida te quedan {vidas}")
    if vidas <= 0:
        print("Te has quedado sin vidas, perdiste.")
        break

    print("")
    print("Nivel 2: División")
    print("Estamos en la recta final, vamos tu puedes!! \n18 : 6")
    while vidas > 0:
        respuesta_5 = int(input("Ingresa la respuesta: "))
        if respuesta_5 == 3:
            print("Respuesta correcta haz ganado (+1 punto)")
            puntaje = puntaje + 1
            print(f"Llevas un total de {puntaje} puntos")
            break
        else:
            print("No te preocupes por fallar, yo tampoco se dividir :( (-1 vida)")
            vidas = vidas - 1
            print(f"haz perdido una vida te quedan {vidas} vidas")
    if vidas <= 0:
        print("Te haz quedado sin vidas, perdiste.")
        break

    print("")
    print("Etapa 3: Potencias")
    print("Nivel 1: Potencias")
    print("Vamos queda poco! \n2 elevado a 3")
    while vidas > 0:
        respuesta_7 = int(input("Ingresa tu solución: "))
        if respuesta_7 == 8:
            print("Respuesta correcta haz ganado (+1 punto)")
            puntaje = puntaje + 1
            print(f"Llevas un total de {puntaje} puntos")
            break
        else:
            print("Mmmmm no, esa no era, vamos solo tienes que multiplicar 2x2 y luego el resultado multiplicarlo x2 otra vez (-1 vida)")
            vidas = vidas - 1
            print(f"Te quedan un total de {vidas} vidas")
    if vidas <= 0:
        print("Te has quedado sin vidas, perdiste.")
        break
    
    print("")
    print("nivel 2: Potencias medias")
    print("Subimos el nivel un poco, pero es el mismo tipo de operacion \n8 elevado a 3")
    while vidas > 0:
        respuesta_8 = int(input("Ingresa tu solución: "))
        if respuesta_8 == 512:
            print("Excelente, respuesta correcta haz ganado (+1 punto)")
            print("Solo te falta un nivel, TU PUEDES!!!!")
            puntaje = puntaje + 1
            print(f"Llevas un total de {puntaje} puntos")
            break
        else:
            print("Nop, esa no era, respuesta equivocada intenta denuevo (-1 vida)")
            vidas = vidas - 1
            print(f"Te quedan un total de {vidas} vidas")
    if vidas <= 0:
        print("Te haz quedado sin vidas, Falto tan poco :(")
        break

    print("")
    print("Nivel 3: Potencias avanzadas")
    print("Esta es la ultima, probablemente necesitaras una calculadora \n10 elevado 6")
    while vidas > 0:
        respuesta_9 = int(input("Ingresa tu respuesta: "))
        if respuesta_9 == 1000000:
            print("")
            print("Respuesta correcta haz ganado (+1 punto)")
            puntaje = puntaje + 1
            print(f"Llevas un total de {puntaje} puntos")
            print("----------------------------------------------------------------------------------------------------------")
            print(f"Felicidades!!!!! Eres un crack para las matematicas")
            nombre = input("Disculpa, tantos numeros provocaron que se me haya olvido tu nombre, como te llamabas? ")
            print(f"Pues ahora pasaras a llamarte ¡¡¡¡{nombre} la Calculadora Humana!!!!")
            print("----------------------------------------------------------------------------------------------------------")
            break
        
        else:
            print("Respuesta incorrecta (Pista: son 6 ceros.)(-1 vida)")
            vidas = vidas - 1
            print(f"Te quedan un total de {vidas} vidas")
    if vidas <= 0:
        print("NOOOO, era la ultima, lo siento, pero deberias intentarlo otra vez")
        print("Hasta luego :(")
        break
        
    break