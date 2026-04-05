print("Bienvenido al contador de votos estudiantil!!!")
print("Ganara A? o C? o habra empate? AVERIGUEMOSLO!!!")
N_encuestados = 0 
votos_del_A = 0
votos_del_C = 0
voto_del_estudiante = 0
contador = 0 
N_encuestados = int(input("¿Cuantos estudiantes van a votar?: "))
while contador < N_encuestados:
    voto_del_estudiante = input("Porfavor escribe A (A favor) o C (En contra):")

    if voto_del_estudiante == "A":
        votos_del_A = votos_del_A + 1
    elif voto_del_estudiante == "C":
        votos_del_C = votos_del_C + 1
    else: 
        print("Voto nulo no contabilizado")
contador = contador + 1

print(f"Votos a favor: {votos_del_A}")
print(f"Votos en contra: {votos_del_C}")

if votos_del_A > votos_del_C:
    print("Gano A favor!!!")
elif votos_del_C > votos_del_A:
    print("Gano En contra!!!")
else:
    print("!EMPATE!")
#1. Pregunta cuántos estudiantes van a votar (ej. N encuestados).
#2. Usa un while para recoger los votos. En cada iteración pide que el estudiante escriba "A" (A favor) o "C" (En contra).
#3. Vas a necesitar DOS contadores (uno para A, uno para C) que parten en 0.
#4. Si ingresan algo distinto a "A" o "C", muestra "Voto nulo no contabilizado" (no lo sumes a nada, pero la iteración se gasta igual).
#5. Fuera del ciclo, compara ambos contadores.
#- Si A > C, imprime "Ganó A favor".
#- Si C > A, imprime "Ganó En Contra".
#- Si A == C, imprime "Empate".