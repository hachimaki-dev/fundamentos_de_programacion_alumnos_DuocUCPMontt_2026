#Busca un oponente justo para una partida en línea.
#Datos Iniciales: Tú tienes 1500 puntos. Encontraste un rival que tiene 1570 puntos.
#Reglas de Negocio: Para saber si la pelea es justa, hay que calcular la diferencia de puntos entre ambos. Si la diferencia es de 50 puntos o menos, la partida es 'Perfecta'. Si es de 100 o menos, es 'Justa'. Si la diferencia es mayor a 100, se debe mostrar 'Buscando otro rival...'.
#Restricciones: Usa la función matemática `abs(tus_puntos - sus_puntos)` para que el resultado siempre sea positivo, sin importar quién tenga más puntos. Imprime el resultado.z

puntos = 1500
P_rival = 1570
diferencia_P = abs(puntos - P_rival)
if diferencia_P <= 50:
    print("partida perfecta")
elif diferencia_P <= 100:
    print("partida justa")
else:
    print("Buscando otro rival")