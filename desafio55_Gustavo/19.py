yo = 1500
rival = 1570

diferencia = abs(rival - yo)

if diferencia <= 50 :
    print("Perfecto")

elif diferencia <= 100 :
    print("Partida Justa")

else :
    print("Buscando otro rival")