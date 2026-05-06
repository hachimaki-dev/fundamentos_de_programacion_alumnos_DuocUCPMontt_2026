tus_puntos = 1500
puntos_rival = 1570

diferencia_puntos = abs(puntos_rival - tus_puntos)

print(diferencia_puntos)

if diferencia_puntos < 100:
    print("Partida justa")
elif diferencia_puntos >= 50:
    print("Partida perfecta")
else:
    print("buscando rival")