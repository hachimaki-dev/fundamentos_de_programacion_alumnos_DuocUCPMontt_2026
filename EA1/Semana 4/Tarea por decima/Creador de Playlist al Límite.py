# Creador de Playlists al Límite
# Objetivo: No llenar la memoria de un reproductor que soporta máximo 60 minutos.

# 1. Tienes un reproductor MP3 minúsculo que solo permite guardar canciones mientras el tiempo total sea EXACTO o MENOR a 60 minutos.
# 2. Usa un acumulador "duracion_total" partido en 0.
# 3. El while se ejecuta MIENTRAS la duracion_total <= 60.
# 4. Pide: "Minutos de la siguiente canción: ".
# 5. ATENCIÓN: Solo suma la canción al acumulador SI (condición) la canción cabe en el tiempo restante.
# - Si no cabe (ej, quedan 2 mins libres y la canción dura 4), muestra "La canción de X minutos no cabe". (Y la canción NO se agrega).
# - Como no se agregó, la suma no cambia. El ciclo volverá a pedir otra pista.
# 6. Si suma_total llega justo a 60, el ciclo terminará solo. Muestra "¡Espacio lleno al 100%!".
    

duracion_total = 0
MAXIMO = 60

while duracion_total <= MAXIMO:
    tiempo_restante = MAXIMO - duracion_total

    if tiempo_restante == 0:
        print("¡Espacio lleno al 100%!")
        break

    minutos_cancion = int(input(f"Faltan {tiempo_restante} min. Minutos de la siguiente canción: "))

    if minutos_cancion <= tiempo_restante:
        duracion_total += minutos_cancion
        print(f"Canción agregada. Total: {duracion_total} de {MAXIMO} min.")
    else:
        print(f"La canción de {minutos_cancion} min no cabe. Solo quedan {tiempo_restante} min.")
print(f"Canción finalizada con {duracion_total} minutos.")


