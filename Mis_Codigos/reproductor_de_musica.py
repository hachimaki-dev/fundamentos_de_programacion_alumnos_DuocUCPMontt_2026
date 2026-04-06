#1. Tienes un reproductor MP3 minúsculo que solo permite guardar canciones mientras el tiempo total sea EXACTO o MENOR a 60 minutos.
#2. Usa un acumulador "duracion_total" partido en 0.
#3. El while se ejecuta MIENTRAS la duracion_total <= 60.
#4. Pide: "Minutos de la siguiente canción: ".
#5. ATENCIÓN: Solo suma la canción al acumulador SI (condición) la canción cabe en el tiempo restante.
#- Si no cabe (ej, quedan 2 mins libres y la canción dura 4), muestra "La canción de X minutos no cabe". (Y la canción NO se agrega).
#- Como no se agregó, la suma no cambia. El ciclo volverá a pedir otra pista.
#6. Si suma_total llega justo a 60, el ciclo terminará solo. Muestra "¡Espacio lleno al 100%!".
duracion_total = 0
while duracion_total <= 60:
    cancion_ingresada = int(input("ingrese la duracion de la cancion: "))
    if cancion_ingresada <= 60 - duracion_total :
        duracion_total = duracion_total + cancion_ingresada
        print(f"la cancion se ha agregado correctamente el espacio restante es de: {60 - duracion_total}")
    elif cancion_ingresada > 60 - duracion_total:
        print("cancion no cabe")
    
    if duracion_total == 60: 
        print("espacion al 100%")
        break