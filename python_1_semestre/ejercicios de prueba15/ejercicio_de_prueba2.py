"""Objetivo: Monitorear tu actividad física de los últimos 7 días.

1. Crea un ciclo while que se ejecute 7 veces (representando los 7 días de la semana).
2. Pregunta al usuario: "¿Cuántos km corriste el día X?".
3. Si el usuario ingresa un número negativo (ej., -1), significa que se lesionó. Muestra 
"Día saltado" y NO sumes esos kilómetros (pero sí cuenta el día).
4. Acumula todos los kilómetros válidos.
5. Al final, si el total es >= 30, muestra "¡Meta semanal cumplida! Eres un atleta".
6. Si es menor, muestra "Sigue intentando, llevas X kilómetros, ¡tú puedes!".

Marcar como terminada       >) y menor que (< {}   """


dia = 0
while dia < 7:
    dia +=1  
    km_corridos = int(input("cuantos km corriste el dia x?: "))
    km_corridos += km_corridos
    if km_corridos < 0:
        print ("dia saltado")
        
    
    
    elif km_corridos >= 30:
        print ("meta semanal cumplida, eres un atleta")
        break
    else:
        km_corridos < 30
        print(f"sigue intentando, llevas " ,km_corridos , "km corridos tu puedes ")
 
