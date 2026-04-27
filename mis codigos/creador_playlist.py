# TERMINADO

print("===== CREADOR DE PLAYLIST MP3 =====")

DURACION_TOTAL = 0
TIEMPO_MAXIMO = 60

while True:

    cancion_usuario = input("Desea añadir una cancion?: ").lower()

    if cancion_usuario == "si":

        tiempo_cancion_usuario = int(input("cuanto tiempo dura su cancion?:"))
        DURACION_TOTAL += tiempo_cancion_usuario

        if DURACION_TOTAL > 60:
            print(f"cancion incompatible, espacio maximo de {TIEMPO_MAXIMO}")
        elif DURACION_TOTAL == TIEMPO_MAXIMO:
            print("MEMORIA LLENA, DISFRUTE SUS CANCIONES >:3")
            break
        
    elif cancion_usuario == "no":
        print("No hay problema, hasta luego <3")
        break
    else:
        print("opcion invalida, intente nuevamente")