# Ejercicio 19: Matchmaking por ELO (Juegos)

print("============================")
print("Sistema de búsqueda de rival")
print("============================")

tus_puntos = 1500
sus_puntos = 1570

diferencia = abs(tus_puntos - sus_puntos)

if diferencia <= 50:
    print("Partida Perfecta")
elif diferencia <= 100:
    print("Partida Justa")
else:
    print("Buscando otro rival...")