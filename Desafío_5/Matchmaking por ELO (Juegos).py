
Puntaje = 1500
Puntaje_de_rival = 1570

Diferencia_de_elo = abs(Puntaje - Puntaje_de_rival) 


print (f"La diferencia de elo es de {Diferencia_de_elo}")


if Diferencia_de_elo < 50:
    print ("Rival encontrado, la partida esta en igualdad de condiciones.")

elif Diferencia_de_elo <= 100 :
    print ("Rival encontrado, la partida es justa para ambos jugadores.")

elif Diferencia_de_elo > 100:
    print ("Buscando a otro rival, el rival a o tu tiene mucho nivel.")

else:
    print ("ERROR")