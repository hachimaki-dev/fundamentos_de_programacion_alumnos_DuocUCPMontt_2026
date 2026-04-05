# Smartwatch Activity Tracker
# Objetivo: Monitorear tu actividad física de los últimos 7 días.

# 1. Crea un ciclo while que se ejecute 7 veces (representando los 7 días de la semana).
# 2. Pregunta al usuario: "¿Cuántos km corriste el día X?".
# 3. Si el usuario ingresa un número negativo (ej., -1), significa que se lesionó. Muestra "Día saltado" y NO sumes esos kilómetros (pero sí cuenta el día).
# 4. Acumula todos los kilómetros válidos.
# 5. Al final, si el total es >= 30, muestra "¡Meta semanal cumplida! Eres un atleta".
# 6. Si es menor, muestra "Sigue intentando, llevas X kilómetros, ¡tú puedes!".

print(" SMARTWATCH ACTIVITY TRACKER ".center(40, "-"))

dias_semana = 7
numero_dia = 1
km_semana = 0

while dias_semana > 0:
    km_diario = int(input(f"¿Cuantos km recorriste el día {numero_dia}? "))
    dias_semana -= 1
    numero_dia += 1
    if km_diario < 0:
        print("Día saltado")
    else:
        km_semana = km_semana + km_diario
    
if dias_semana == 0 and km_semana >= 30:
    print("¡Meta semanal cumplida! Eres un atleta")
elif dias_semana == 0 and km_semana < 30:
    print(f"Sigue intentando, lograste {km_semana} kilómetros, ¡tú puedes!")

