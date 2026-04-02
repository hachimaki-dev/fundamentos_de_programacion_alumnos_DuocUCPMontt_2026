"""
Contador de Votos Estudiantil
Objetivo: Procesar los resultados de una pequeña encuesta del curso.

1. Pregunta cuántos estudiantes van a votar (ej. N encuestados).
2. Usa un while para recoger los votos. En cada iteración pide que el estudiante escriba "A" (A favor) o "C" (En contra).
3. Vas a necesitar DOS contadores (uno para A, uno para C) que parten en 0.
4. Si ingresan algo distinto a "A" o "C", muestra "Voto nulo no contabilizado" (no lo sumes a nada, pero la iteración se gasta igual).
5. Fuera del ciclo, compara ambos contadores.
- Si A > C, imprime "Ganó A favor".
- Si C > A, imprime "Ganó En Contra".
- Si A == C, imprime "Empate".
"""

Contador_A = 0
Contador_C = 0

Encuestados = int(input("Numero de encuestados? "))
while Encuestados > 0:
    voto = input("Votas por A o C? ")
    if voto == "A":
        print("Voto a favor")
        Contador_A = Contador_A + 1
        Encuestados = Encuestados - 1
    elif voto == "C":
        print("Voto en contra")
        Contador_C = Contador_C + 1
        Encuestados = Encuestados - 1
    else:
        print("Voto nulo no contabilizado")
        Encuestados = Encuestados - 1

if Contador_A > Contador_C:
    print("Ganó A favor")
elif Contador_A < Contador_C:
    print("Ganó En Contra")
else:
    print("Empate")