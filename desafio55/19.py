###Ejercicio 19: Matchmaking por# ELO (J#ue#gos)#
#Busca un oponente justo para una part#i#da en línea.#
#
#Datos Iniciales: Tú tienes 1500 puntos. Encontraste un rival que tiene# #1570 puntos.#
#
#Reglas de Negocio: Para saber si la pelea es justa, hay que calcular la diferencia de puntos
#  entre ambos. Si la diferencia es de 50 puntos o menos, la partida es 'Perfecta'. Si es de 
# 100 o menos, es 'Justa'. Si la diferencia es mayor a 100, se debe mostrar 'Buscando ot#r#o 
# rival...'.#
#
#Restricciones: Usa la función matemática `abs(tus_puntos - sus_puntos)` para que el 
# resultado siempre sea positivo, sin importar quién tenga más puntos. Imprime #e#l 
# resultado.#
#
#Resultado esperad#o en consola:
#Partida Justa


mis_puntos = 1500
puntos_rival = 1570

if mis_puntos-puntos_rival <= 50:
    ("partida perfecta")

    if mis_puntos - puntos_rival <= 100:
        print("partida justa")

    elif mis_puntos - puntos_rival >= 100:
        print("buscando otro rival")



