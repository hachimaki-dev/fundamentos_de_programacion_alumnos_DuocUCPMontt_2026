Mochilas = ["Mapa", "Espada"]

Piso = ["Madera", "Piedra", "Oro"]

for i in Piso:

    Mochilas.append(i)

    if (len(Mochilas)) == 4 :
        print ("lleno")
        break

print (f"Recogiste solo {Mochilas}")