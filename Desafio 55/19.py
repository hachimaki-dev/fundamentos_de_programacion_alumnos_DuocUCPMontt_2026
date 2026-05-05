puntos_iniciales=1500
puntos_rival=1570

if abs(puntos_iniciales-puntos_rival)<=50:
    print("Perfecta")

elif abs(puntos_iniciales-puntos_rival)<=100:
    print("Justa")

elif abs(puntos_iniciales-puntos_rival)>100:
    print("Buscando otro rival")
else:
    print("Error")


