print("===== CREADOR DE PLAYLIST MP3 =====")

DURACION_TOTAL = 0
TIEMPO_MAXIMO = 60

while DURACION_TOTAL < TIEMPO_MAXIMO:
    
    print(f"\nEspacio ocupado: {DURACION_TOTAL} / {TIEMPO_MAXIMO} min.")
    añadir_cancion = int(input("Desea añadir una cancion? (SI/NO):"))

    if añadir_cancion == "SI" or "si" or "Si":
        tiempo_cancion = int(input("Minutos de la siguiente cancion:"))

    if DURACION_TOTAL + tiempo_cancion <= TIEMPO_MAXIMO:

        DURACION_TOTAL = DURACION_TOTAL + tiempo_cancion
        print("Perfecto, cancion añadida.")

    if tiempo_cancion == tiempo_cancion:
        print("===== PLAYLIST LLENA AL 100& =====")

    else:
        print(f"La cancion de {tiempo_cancion} minutos no cabe")
