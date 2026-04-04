#1. Pregunta cuántos estudiantes van a votar (ej. N encuestados).
#2. Usa un while para recoger los votos. En cada iteración pide que el estudiante escriba "A" (A favor) o "C" (En contra).
#3. Vas a necesitar DOS contadores (uno para A, uno para C) que parten en 0.
#4. Si ingresan algo distinto a "A" o "C", muestra "Voto nulo no contabilizado" (no lo sumes a nada, pero la iteración se gasta igual).
#5. Fuera del ciclo, compara ambos contadores.
#- Si A > C, imprime "Ganó A favor".
#- Si C > A, imprime "Ganó En Contra".
#- Si A == C, imprime "Empate"

n_votos = int(input("cuantas personas votaran"))
votos_a = 0
votos_e = 0

while n_votos  > 0 :
    voto = input("por quien vas a votar, A o C")
    if voto == "A":
        votos_a += 1
        n_votos -= 1
    elif voto == "C":
        votos_e += 1
        n_votos -= 1
    else:
        print("voto nulo")
        n_votos -= 1
if votos_a > votos_e:
    print("voto A es el ganador")
elif votos_e > votos_a:
    print("votos C es el ganador")
elif votos_a == votos_e:
    print("empate")

