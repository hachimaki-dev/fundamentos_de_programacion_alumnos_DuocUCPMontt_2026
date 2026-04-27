duracion_total = 0
contador = 0

while duracion_total < 60:
    entrada = input("Minutos de la siguiente canción (o escribe 0 para salir): ")

    if entrada == "0":
        print("Saliendo...")
        break

    cancion = int(entrada)

    if duracion_total + cancion <= 60:
        duracion_total += cancion
        contador += 1
        print("Canción agregada. Total:", duracion_total)
    else:
        print("La canción de", cancion, "minutos no cabe")

if duracion_total == 60:
    print("¡Espacio lleno al 100%!")

print("Canciones guardadas:", contador)