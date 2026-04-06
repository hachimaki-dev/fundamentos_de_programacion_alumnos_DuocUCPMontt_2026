# Objetivo: Procesar los resultados de una pequeña encuesta del curso.
# Pregunta cuántos estudiantes van a votar (ej. N encuestados).
cantidad_estudiantes = int(input("¿Cuántos estudiantes van a votar? "))
# Usa un while para recoger los votos. En cada iteración pide que el estudiante escriba "A" (A favor) o "C" (En contra).
# vas a necesitar DOS contadores (uno para A, uno para C) que parten en 0.
contador_a = 0
contador_c = 0
# Si ingresan algo distinto a "A" o "C", muestra "Voto nulo no contabilizado" (no lo sumes a nada, pero la iteración se gasta igual).
contador_votos = 0
while contador_votos < cantidad_estudiantes:
    voto = input("Ingrese su voto (A para A favor, C para En contra): ")
    if voto == "A":
        contador_a += 1
    elif voto == "C":
        contador_c += 1
    else:
        print("Voto nulo no contabilizado")
    contador_votos += 1
# Fuera del ciclo, compara ambos contadores.
# - Si A > C, imprime "Ganó A favor".
# - Si C > A, imprime "Ganó En Contra".    
# - Si A == C, imprime "Empate".
if contador_a > contador_c:
    print("Ganó A favor")   
elif contador_c > contador_a:
    print("Ganó En Contra")
else:
    print("Empate")