"""
Objetivo: No llenar la memoria de un reproductor que soporta máximo 60 minutos.

1. Tienes un reproductor MP3 minúsculo que solo permite guardar canciones mientras el tiempo total sea EXACTO o MENOR a 60 minutos.
2. Usa un acumulador "duracion_total" partido en 0.
3. El while se ejecuta MIENTRAS la duracion_total <= 60.
4. Pide: "Minutos de la siguiente canción: ".
5. ATENCIÓN: Solo suma la canción al acumulador SI (condición) la canción cabe en el tiempo restante.
- Si no cabe (ej, quedan 2 mins libres y la canción dura 4), muestra "La canción de X minutos no cabe". (Y la canción NO se agrega).
- Como no se agregó, la suma no cambia. El ciclo volverá a pedir otra pista.
6. Si suma_total llega justo a 60, el ciclo terminará solo. Muestra "¡Espacio lleno al 100%!".
"""
duracion_total = 0
tiempo_maximo = 60
while duracion_total <= 60 and tiempo_maximo > 0:
    Minutos_cancion = int(input("Minutos de la siguiente canción: "))
    if Minutos_cancion <= 60 and tiempo_maximo >= Minutos_cancion:
        duracion_total = duracion_total + Minutos_cancion
        tiempo_maximo = tiempo_maximo - Minutos_cancion
        print(f"Te quedan {tiempo_maximo} minutos")
    else:
        print(f"La canción de {Minutos_cancion} minutos no cabe.")
print("¡Espacio lleno al 100%!")