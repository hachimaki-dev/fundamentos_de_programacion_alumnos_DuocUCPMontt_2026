print("Bienvenido al creador de playlists al limite!!")
print("Ingresa canciones hasta el limite!")
acumulador_duracion_total = 0 
Minutos_siguiente_cancion = 0 
while acumulador_duracion_total <= 60:
    Minutos_siguiente_cancion = int(input("Ingresa los minutos de la siguiente cancion: "))
    espacio_MP3 = 60 - acumulador_duracion_total
    if Minutos_siguiente_cancion <= espacio_MP3:
        acumulador_duracion_total = acumulador_duracion_total + Minutos_siguiente_cancion
        print("La cancion ha sido agregada!!!")
        print(f"Espacio restante:{espacio_MP3}")
    else:
        print(f"La cancion de {Minutos_siguiente_cancion} no cabe :()")
    if acumulador_duracion_total == 60:
        print("ESPACIO LLENO AL 100%")
        break






#1. Tienes un reproductor MP3 minúsculo que solo permite guardar canciones mientras el tiempo total sea EXACTO o MENOR a 60 minutos.
#2. Usa un acumulador "duracion_total" partido en 0.
#3. El while se ejecuta MIENTRAS la duracion_total <= 60.
#4. Pide: "Minutos de la siguiente canción: ".
#5. ATENCIÓN: Solo suma la canción al acumulador SI (condición) la canción cabe en el tiempo restante.
#- Si no cabe (ej, quedan 2 mins libres y la canción dura 4), muestra "La canción de X minutos no cabe". (Y la canción NO se agrega).
#- Como no se agregó, la suma no cambia. El ciclo volverá a pedir otra pista.
#6. Si suma_total llega justo a 60, el ciclo terminará solo. Muestra "¡Espacio lleno al 100%!".