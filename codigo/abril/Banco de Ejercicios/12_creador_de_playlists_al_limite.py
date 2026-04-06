limite_duracion = 60
duracion_total = 0

while duracion_total <= 60:
    duracion_cancion = int(input("Minutos de la siguiente canción: "))
    if (duracion_total + duracion_cancion) <= 60:
        duracion_total += duracion_cancion
        print(f"¡Canción agregada! Duración actual de la playlist: {duracion_total} minutos.")
        if duracion_total == 60:
            print("¡Espacio lleno al 100%!")
            break
    else:
        print(f"La canción de {duracion_cancion} minutos no cabe. Duración actual de la playlist: {duracion_total} minutos.")
