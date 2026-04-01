"""Smartwatch Activity Tracker
Objetivo: Monitorear tu actividad física de los últimos 7 días.

1. Crea un ciclo while que se ejecute 7 veces (representando los 7 días de la semana).
2. Pregunta al usuario: "¿Cuántos km corriste el día X?".
3. Si el usuario ingresa un número negativo (ej., -1), significa que se lesionó. Muestra "Día saltado" y NO sumes esos kilómetros (pero sí cuenta el día).
4. Acumula todos los kilómetros válidos.
5. Al final, si el total es >= 30, muestra "¡Meta semanal cumplida! Eres un atleta".
6. Si es menor, muestra "Sigue intentando, llevas X kilómetros, ¡tú puedes!".
"""
Total = 0
Dia = 1
while Dia < 8:
    KM = int(input(f"¿Cuántos km corriste el día {Dia}?"))
    if KM < 0:
        print("Día saltado")
        Dia = Dia + 1
    else:
        print("Vas bien")
        Total = Total + KM
        Dia = Dia + 1
if Total >= 30:
    print("¡Meta semanal cumplida! Eres un atleta")
else:
    print(f"Sigue intentando, llevas {Total} kilómetros, ¡tú puedes!")