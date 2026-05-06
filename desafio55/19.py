puntos= 1500
puntos_rival= 1570

diferencia= abs(puntos - puntos_rival)

if diferencia <= 50:
    print("Partida perfecta")
elif diferencia <= 100:
    print("Partida justa")
elif diferencia > 100:
    print("Buscando otro rival")
else:
    print("jodiste 💀")
    