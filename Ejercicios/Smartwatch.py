dia = 1
total_km = 0

while dia <=7:
    km = float(input(f"¿Cuantos km corriste en el dia {dia}: "))
    if km < 0:
        print("Día saltando (Lesión detectada)")
    else:

        total_km = total_km + km
    
    dia = dia + 1

print("--- RESUMEN SEMANAL ---")
if total_km >= 30:
    print(f"¡Meta semanal cumplida! Recorriste {total_km} km. Eres un atleta.")
else:
    print(f"Sigue intentando, llevas {total_km} kilómetros, ¡tú puedes!")

    
          


