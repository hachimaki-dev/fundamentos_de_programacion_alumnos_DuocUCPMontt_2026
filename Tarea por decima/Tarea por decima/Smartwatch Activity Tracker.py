# Smartwatch Activity Tracker
# Objetivo: Monitorear tu actividad física de los últimos 7 días.

# 1. Crea un ciclo while que se ejecute 7 veces (representando los 7 días de la semana).
# 2. Pregunta al usuario: "¿Cuántos km corriste el día X?".
# 3. Si el usuario ingresa un número negativo (ej., -1), significa que se lesionó. Muestra "Día saltado" y NO sumes esos kilómetros (pero sí cuenta el día).
# 4. Acumula todos los kilómetros válidos.
# 5. Al final, si el total es >= 30, muestra "¡Meta semanal cumplida! Eres un atleta".
# 6. Si es menor, muestra "Sigue intentando, llevas X kilómetros, ¡tú puedes!".

cantidad_dia = 0
km_totales = 0
km_dia = 0

print("****Smartwatch Activity Tracker****")

while 7 > cantidad_dia:
    km_dia = int(input(f"¿Cuántos km corriste el día {cantidad_dia + 1}?: "))
    if km_dia <= 0:
        print("Día saltado")
    else:
        km_totales += km_dia 
    cantidad_dia += 1

if km_totales >= 30:
    print("¡Meta semanal cumplida! Eres un atleta")
elif km_totales < 30:
    print(f"Sigue intenado, levas {km_totales} kilómetros, ¡tú puedes!")
else:
    print("No se que hiceste para llegar a este resultado .-.")

print("Fin del programa")