#Objetivo: Monitorear tu actividad física de los últimos 7 días.

#1. Crea un ciclo while que se ejecute 7 veces (representando los 7 días de la semana).
#2. Pregunta al usuario: "¿Cuántos km corriste el día X?".
#3. Si el usuario ingresa un número negativo (ej., -1), significa que se lesionó.
 #Muestra "Día saltado" y NO sumes esos kilómetros (pero sí cuenta el día).
#4. Acumula todos los kilómetros válidos.
#5. Al final, si el total es >= 30, muestra "¡Meta semanal cumplida! Eres un atleta".
#6. Si es menor, muestra "Sigue intentando, llevas X kilómetros, ¡tú puedes!".
contador = 0
km_dias = 7
total_km = 0
while contador != km_dias:
    km_recorridos = int(input("cuantos km corriste el dia X ?: "))
    if km_recorridos < 0:
        print("dia saltado ")
        contador = contador +1
        continue
    contador +=1
    total_km = total_km + km_recorridos 
    contador > 7
    
    

if total_km >= 30:
    print("meta SEMANAL CUMPLIDA ERES UN ATLETA")
elif total_km < 30:
    print(f"sigue intentado llevas , {total_km} km, tu puedes ")
