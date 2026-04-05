while True:
    try:
        estudiantes_que_van_a_votar = int(input("¿cuántos estudiantes van a votar?: "))
        break
    except: ValueError
    print("Error: por favor, ingresa un núnero entero (ejemplo: 10).")

votos_a = 0
votos_c = 0
procesados= 0

while procesados < estudiantes_que_van_a_votar:
    voto = input(f"Estudiante {procesados + 1}, ingresa tu voto (A/C): ").upper()

    if voto == "A":
        votos_a = votos_a + 1
    elif voto == "C":
        votos_c = votos_c + 1
    else:
        print("Votos nulo no contabilizado")

    procesados = procesados + 1

print("--- Resultados ---")
if votos_a > votos_c:
    print("Ganó A favor")
elif votos_c > votos_a:
    print("Ganó en Contra")
else:
    print("Empate")