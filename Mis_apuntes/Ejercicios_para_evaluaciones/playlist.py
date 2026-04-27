duracion_total = 0
cantidad_canciones = 0
espacio = 60
while duracion_total <= 60:
    min = int(input("Ingrese la cantidad de minutos que tiene la siguiente canción. "))
    if min <= 60:
        duracion_total += min
        cantidad_canciones += 1
        espacio = espacio - min
    else:
        print("Imposible de seleccionar, porfavor escoja otra canción de menor duración.")
    print(f"Quedan {espacio} minutos disponibles.")
    if espacio == 0:
        print("Máxima capacidad alcanzada.")        #PONEMOS UN BREAK PARA QUE LA CONSOLA EVITE COLOCAR NUMEROS NEGATIVOS.
        break
print(f"Haz añadido un total de {cantidad_canciones} canciones a tu playlist.")
print("Ya no entran más canciones!!")