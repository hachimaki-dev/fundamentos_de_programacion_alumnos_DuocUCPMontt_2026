puntos =1500
rival = 1570

funcion_matematica = abs(puntos - rival)

if funcion_matematica <= 50:
    print("partida perfecta")

elif funcion_matematica <= 100:
    print("partida justa")

else:
    print("buscando otro rival...")