""" Objetivo: Procesar los resultados de una pequeña encuesta del curso.

1. Pregunta cuántos estudiantes van a votar (ej. N encuestados).

2. Usa un while para recoger los votos. En cada iteración pide que el estudiante 
escriba "A" (A favor) o "C" (En contra).

3. Vas a necesitar DOS contadores (uno para A, uno para C) que parten en 0.

4. Si ingresan algo distinto a "A" o "C", muestra "Voto nulo no contabilizado" 
(no lo sumes a nada, pero la iteración se gasta igual).

5. Fuera del ciclo, compara ambos contadores.
- Si A > C, imprime "Ganó A favor".
- Si C > A, imprime "Ganó En Contra".
- Si A == C, imprime "Empate"."""

estudiantes = int(input("cuantos estudiantes seran encuestados ? : "))
 
votos_a = 0
votos_c = 0
contador = 0

while contador < estudiantes :
    voto = input("ingresa tu voto: a: afavor o  c: en contra")
    if voto == "a":
        votos_a +=1
        contador +=1

    elif voto == "c":
        votos_c +=1
        contador +=1

if votos_a > votos_c:
    print("gano a favor")

elif votos_c > votos_a:
    print("gano en contra")

elif votos_a == votos_c:
    print("empate")    

