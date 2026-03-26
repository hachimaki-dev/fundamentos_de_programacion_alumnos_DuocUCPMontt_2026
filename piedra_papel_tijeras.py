#Programa piedra, papel o tijeras entre dos usuarios, de maximo 3 puntos para ganar, vamos a ocupar el while para repetir el juego hasta que uno de los usuarios alcance los 3 puntos, vamos a ocupar el if para determinar quien gana cada ronda, y al final del juego vamos a mostrar el ganador.

#Iniciar del programa
print("Bienvenidos al juego de piedra, papel o tijeras")
print("El primer jugador en alcanzar 3 puntos gana el juego")
#Definir las opciones

opciones = ["piedra", "papel", "tijeras"]
#Definir las variables
eleccion_usuario1 = ""
eleccion_usuario2 = ""
#Definir el contador de puntos
puntos_usuario1 = 0
puntos_usuario2 = 0
#Definir meta de victorias
meta_puntos = 3
#Iniciar el juego

while eleccion_usuario1 == eleccion_usuario2:
    print("Es un empate en esta ronda, nadie gana puntos, vuelvan a elegir")
    eleccion_usuario1 = input("Usuario 1, elige piedra, papel o tijeras: ")
    eleccion_usuario2 = input("Usuario 2, elige piedra, papel o tijeras: ")

else:
    if (eleccion_usuario1 == "piedra" and eleccion_usuario2 == "tijeras") or (eleccion_usuario1 == "papel" and eleccion_usuario2 == "piedra") or (eleccion_usuario1 == "tijeras" and eleccion_usuario2 == "papel"):
        puntos_usuario1 += 1
        print("Usuario 1 gana esta ronda, puntos: ", puntos_usuario1)
    else:
        puntos_usuario2 += 1
        print("Usuario 2 gana esta ronda, puntos: ", puntos_usuario2)

while puntos_usuario1 < meta_puntos and puntos_usuario2 < meta_puntos:
        eleccion_usuario1 = input("Usuario 1, elige piedra, papel o tijeras: ")
        eleccion_usuario2 = input("Usuario 2, elige piedra, papel o tijeras: ")

        if eleccion_usuario1 == eleccion_usuario2:
            print("Es un empate en esta ronda, nadie gana puntos, vuelvan a elegir")

        elif (eleccion_usuario1 == "piedra" and eleccion_usuario2 == "tijeras") or (eleccion_usuario1 == "papel" and eleccion_usuario2 == "piedra") or (eleccion_usuario1 == "tijeras" and eleccion_usuario2 == "papel"):
            puntos_usuario1 += 1
            print("Usuario 1 gana esta ronda, puntos: ", puntos_usuario1)
        else:
            puntos_usuario2 += 1
            print("Usuario 2 gana esta ronda, puntos: ", puntos_usuario2)
#Mostrar el ganador
print("El ganador es: ", "Usuario 1" if puntos_usuario1 == meta_puntos else "Usuario 2")







    



