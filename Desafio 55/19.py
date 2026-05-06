mis_puntos = 1500
sus_puntos = 1570

if abs(mis_puntos - sus_puntos) <= 50 :
    print("Perfecto")
elif abs(mis_puntos - sus_puntos) <= 100 :
    print("Justa")
elif abs(mis_puntos - sus_puntos) > 100 :
    print("Buscando otro rival...")