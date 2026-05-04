jugador = 1500
rival = 1570

diferencia = abs(jugador - rival)

if diferencia <= 50:
    print("Perfecta")
elif diferencia <= 100:
    print("Justa")
else:
    print("Buscando otro rival...")