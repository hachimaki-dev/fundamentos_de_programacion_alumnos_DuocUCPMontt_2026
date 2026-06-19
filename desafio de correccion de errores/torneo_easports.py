print("🎮 LIGA DE CAMPEONES — Torneo eSports")

while True:
    try:
        num_jugadores = int(input("¿Cuántos jugadores participan? "))
        if num_jugadores >= 2:
            break
        print("Se necesitan al menos 2 jugadores.")
    except ValueError:
        print("Ingresa un número entero.")

jugadores = []
diamante = 0
oro = 0
bronce = 0
mejor_gamertag = ""
mejor_puntaje = 0
suma_general = 0

for i in range(num_jugadores):
    print(f"\n--- Jugador {i+1} ---")

    while True:
        tag = input("Gamertag: ").strip()
        if len(tag) >= 3 and " " not in tag:
            break
        print("El gamertag debe tener al menos 3 caracteres y sin espacios.")

    puntajes = []
    for ronda in range(3):
        while True:
            try:
                pts = int(input(f"Puntaje ronda {ronda+1} (0-100): "))
                if 0 <= pts <= 100:
                    puntajes.append(pts)
                    break
                print("Debe estar entre 0 y 100.")
            except ValueError:
                print("Ingresa un entero válido.")

    puntaje_final = sum(puntajes) / 2

    if puntaje_final >= 80:
        division = "División Diamante"
        diamante += 1
    elif puntaje_final > 50:
        division = "División Oro"
        oro += 1
    else:
        division = "División Bronce"
        bronce += 1

    print(f"→ {tag}: Puntaje final {puntaje_final:.2f} — {division}")

    if puntaje_final > mejor_puntaje:
        mejor_puntaje = puntaje_final
        mejor_gamertag = tag

    jugador = {"gamertag": tag, "puntajes": puntajes, "final": puntaje_final, "division": division}
    jugadores.append(jugador)
    suma_general += puntaje_final

promedio_torneo = suma_general / len(jugadores)

print(f"\n🏆 RESULTADOS DEL TORNEO")
print(f"División Diamante: {diamante} jugadores")
print(f"División Oro: {oro} jugadores")
print(f"División Bronce: {bronce} jugadores")
print(f"Ganador del torneo: {mejor_gamertag}")
print(f"Promedio general del torneo: {promedio_torneo}")