# Contador de Votos Estudiantil
# Objetivo: Procesar los resultados de una pequeña encuesta del curso.

# 1. Pregunta cuántos estudiantes van a votar (ej. N encuestados).
# 2. Usa un while para recoger los votos. En cada iteración pide que el estudiante escriba "A" (A favor) o "C" (En contra).
# 3. Vas a necesitar DOS contadores (uno para A, uno para C) que parten en 0.
# 4. Si ingresan algo distinto a "A" o "C", muestra "Voto nulo no contabilizado" (no lo sumes a nada, pero la iteración se gasta igual).
# 5. Fuera del ciclo, compara ambos contadores.
#     - Si A > C, imprime "Ganó A favor".
#     - Si C > A, imprime "Ganó En Contra".
#     - Si A == C, imprime "Empate".

print(" ELECCION ESTUDIANTIL ".center(40, "-"))

votos_a_favor = 0
votos_en_contra = 0
opcion_elegida = ""
numero_votante = 1
cantidad_votantes = int(input("Cantidad de votantes: "))

if cantidad_votantes == 0:
    print("No hay votantes")
else:
    while cantidad_votantes > 0:
        print(f"\nVotante {numero_votante}, ingrese su opcion elegida")
        opcion_elegida = input("Si esta A FAVOR escriba 'A' | Si esta EN CONTRA escriba 'C': ").upper()
        if opcion_elegida == "A":
            votos_a_favor += 1
        elif opcion_elegida == "C":
            votos_en_contra += 1
        else:
            print("Voto nulo no contabilizado")
        cantidad_votantes -= 1
        numero_votante += 1

    if cantidad_votantes == 0:
        print(f"\nVotos A FAVOR: {votos_a_favor}")
        print(f"Votos EN CONTRA: {votos_en_contra}")
        if votos_a_favor > votos_en_contra:
            print(" GANO A FAVOR ".center(30, "*"))
        if votos_en_contra > votos_a_favor:
            print(" GANO EN CONTRA ".center(30, "*"))
        if votos_a_favor == votos_en_contra:
            print(" EMPATE ".center(30, "*"))