'''Ejercicio 19: Matchmaking por ELO (Juegos)
Busca un oponente justo para una partida en línea.

Datos Iniciales: Tú tienes 1500 puntos. Encontraste un rival que tiene 1570 puntos.

Reglas de Negocio: Para saber si la pelea es justa, hay que calcular la diferencia de puntos entre ambos. Si la diferencia es de 50 puntos o menos, la partida es 'Perfecta'. Si es de 100 o menos, es 'Justa'. Si la diferencia es mayor a 100, se debe mostrar 'Buscando otro rival...'.

Restricciones: Usa la función matemática `abs(tus_puntos - sus_puntos)` para que el resultado siempre sea positivo, sin importar quién tenga más puntos. Imprime el resultado.'''

puntos = 1500
puntos_rival = 1570
diferencia = abs(puntos - puntos_rival)

if diferencia <= 50:
    print("Partida Perfecta")
elif diferencia <= 100:
    print("Partida Justa")
else:
    print("Buscando otro rival...")