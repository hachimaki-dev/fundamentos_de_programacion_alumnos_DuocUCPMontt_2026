duracion_total = 0
capacidad_max = 60

while duracion_total < capacidad_max:
    min_cancion = int(input("Minutos de la siguiente canción: "))

    if duracion_total + min_cancion > capacidad_max:
        print(f"La cancion de {min_cancion} minuto(s) no cabe")
    else:
        duracion_total += min_cancion
        print(f"Llevas {duracion_total} minuto(s) en la playlist")

print("¡Espacio lleno al 100%!")