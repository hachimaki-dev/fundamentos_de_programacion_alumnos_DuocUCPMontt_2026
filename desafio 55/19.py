
mis_puntos = 1500
sus_puntos = 1570


diferencia = abs(mis_puntos - sus_puntos)


if diferencia <= 50:
    resultado = "Perfecta"
elif diferencia <= 100:
    resultado = "Justa"
else:
    resultado = "Buscando otro rival..."

print(f"Diferencia de puntos: {diferencia}")
print(f"Estado de la partida: {resultado}")
