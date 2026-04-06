duracion_total = 0
while duracion_total < 60:
    minutos_de_cancion = int(input("Minutos de la siguiente canción: "))
    if minutos_de_cancion + duracion_total <= 60:
        duracion_total = duracion_total + minutos_de_cancion
    else:
        print(f"La cancion de {minutos_de_cancion} no cabe")

if duracion_total == 60:
    print("¡Espacio lleno al 100%!")