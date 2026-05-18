puntos = 1500

puntos_rival = 1570

diferencia = abs(puntos_rival - puntos)

if diferencia <= 50:
    print("¡Partida Perfecta!")

elif diferencia <= 100 and diferencia > 50:
    print("¡Partida Justa!")

elif diferencia > 100:
    print("Busca otro rival...")