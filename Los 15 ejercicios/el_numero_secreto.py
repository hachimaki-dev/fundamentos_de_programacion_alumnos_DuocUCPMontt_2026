print("****************BIENVENIDOS AL JUEGO DEL NUMERO SECRETO*****************")

numero_secreto = 20
respuesta_del_usuario = ""

intentos = 0


while  respuesta_del_usuario != numero_secreto :
    respuesta_del_usuario = int(input("ingresa un numero el cual tu creas que es el numero secreto "))

    intentos += 1

    if respuesta_del_usuario < numero_secreto :
        print("El número secreto es más ALTO")
    elif respuesta_del_usuario > numero_secreto :
        print("El número secreto es más BAJO")
    else:
        print(f"adivinaste que el numero secreto era {numero_secreto}")


print(f"Ganaste en {intentos} intentos")