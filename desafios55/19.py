yo = 1500
rival = 1570

diferencia = abs(yo - rival)

if diferencia <= 50 :
    print("Partida perfecta")
elif diferencia <= 100 :
    print("Partida Justa")
elif diferencia > 100 :
    print("Buscando otro rival...")