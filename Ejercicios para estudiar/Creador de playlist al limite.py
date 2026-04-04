#Tienes un reproductor MP3 minúsculo que solo permite guardar canciones mientras el tiempo total sea EXACTO o MENOR a 60 minutos.
# Usa un acumulador "duracion_total" partido en 0.
# El while se ejecuta MIENTRAS la duracion_total <= 60.
# Pide: "Minutos de la siguiente canción: ".
#ATENCIÓN: Solo suma la canción al acumulador SI (condición) la canción cabe en el tiempo restante.
#Si no cabe (ej, quedan 2 mins libres y la canción dura 4), muestra "La canción de X minutos no cabe". (Y la canción NO se agrega).
#Como no se agregó, la suma no cambia. El ciclo volverá a pedir otra pista.
# Si suma_total llega justo a 60, el ciclo terminará solo. Muestra "¡Espacio lleno al 100%!".

duracion_total = 0
suma_total = 60
while duracion_total < suma_total:
    cancion = int(input("Minutos de la siguiente canción: "))
    espacio_restante = suma_total - duracion_total
    if cancion <= espacio_restante:
        duracion_total = duracion_total + cancion
        print (f"Añadida. Haz usado {duracion_total}/60 minutos")
    else:
        print (f"La canción de {cancion} minutos no cabe")
    if duracion_total == suma_total:
        print ("¡Espacio lleno al 100%!")
