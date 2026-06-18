# Contador de Votos Estudiantil
# Objetivo: Procesar los resultados de una pequeña encuesta del curso.

# 1. Pregunta cuántos estudiantes van a votar (ej. N encuestados).
# 2. Usa un while para recoger los votos. En cada iteración pide que el estudiante escriba "A" (A favor) o "C" (En contra).
# 3. Vas a necesitar DOS contadores (uno para A, uno para C) que parten en 0.
# 4. Si ingresan algo distinto a "A" o "C", muestra "Voto nulo no contabilizado" (no lo sumes a nada, pero la iteración se gasta igual).
# 5. Fuera del ciclo, compara ambos contadores.
# - Si A > C, imprime "Ganó A favor".
# - Si C > A, imprime "Ganó En Contra".
# - Si A == C, imprime "Empate".

votos_a = 0
votos_c = 0
votos_procesados = 0

print("*****Bienvenidos al Contador de Votos Estudiantil*****")
num_estudiantes = int(input("¿Cuántos estudiantes van a votar? (Ingrese el número): "))
while num_estudiantes > votos_procesados:
    voto = input("Escribe 'A' (A favor) o 'C' (En contra): ")
    if voto == "A":
        votos_a += 1
        print("Has votado por A")
    elif voto == "C":
        votos_c += 1
        print("Has votado por C")
    else:
        print("Voto nulo no contabilizado")

    votos_procesados += 1

if votos_a > votos_c:
    print("Ganó A favor")
elif votos_c > votos_a:
    print("Ganó En Contra")
else:
    print("Empate")

print("Fin del programa")