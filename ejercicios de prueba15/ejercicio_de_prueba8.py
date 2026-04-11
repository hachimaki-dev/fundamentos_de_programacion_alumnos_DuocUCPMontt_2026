"""Objetivo: Procesar los resultados de una pequeña encuesta del curso.

1. Pregunta cuántos estudiantes van a votar (ej. N encuestados).
2. Usa un while para recoger los votos. En cada iteración pide que el estudiante escriba "A" (A favor) o "C" (En contra).
3. Vas a necesitar DOS contadores (uno para A, uno para C) que parten en 0.
4. Si ingresan algo distinto a "A" o "C", muestra "Voto nulo no contabilizado" (no lo sumes a nada, pero la iteración se gasta igual).
5. Fuera del ciclo, compara ambos contadores.
- Si A > C, imprime "Ganó A favor".
- Si C > A, imprime "Ganó En Contra".
- Si A == C, imprime "Empate".         >) y menor que (<{} """


estudiantes = 0
votos_de_a = 0
votos_de_c = 0
votos_realizados = 0

while True:
    estudiantes = int(input("cuantos estudiantes van a votar?:  "))
    votos_realizados = input(f"Estudiante {votos_realizados + 1}, ¿votas por A o por C?: ")
    
    if votos_realizados == "a":
        votos_de_a += 1
    elif votos_realizados == "c":
        votos_de_c += 1
        votos_realizados += 1
    
    else:
        print("Voto nulo (no es A ni C)")
if votos_de_a > votos_de_c:
    print(f"Ganó A con {votos_de_a} votos. ¡Felicidades!")
elif votos_de_c > votos_de_a:
    print(f"Ganó C con {votos_de_c} votos. ¡Felicidades!")






