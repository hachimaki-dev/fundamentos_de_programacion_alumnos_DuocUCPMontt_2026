Mis_puntos = 1500
Puntos_rival = 1570
diferencia_puntos = Puntos_rival - Mis_puntos
if diferencia_puntos <= 50:
  print("Perfecta")
elif diferencia_puntos <= 100:
  print(" Patida Justa")
elif diferencia_puntos > 100:
  print("Buscando otro rival...")
