print("✨ ACADEMIA ARCANA — Clasificación de Aprendices ✨")

while True:
    try:
        cantidad = int(input("¿Cuántos aprendices registrar? "))
        if cantidad > 0:
            break
        print("Ingresa un número mayor a 0.")
    except ValueError:
        print("Entrada inválida.")

fenix = 0
grifo = 0
buho = 0
mejor_nombre = ""
mejor_poder = 0

for i in range(cantidad):
    print(f"\n--- Aprendiz {i+1} ---")

    while True:
        nombre = input("Nombre mágico: ").strip()
        if len(nombre) >= 3:
            break
        print("El nombre debe tener al menos 3 caracteres.")

    while True:
        try:
            poder = int(input("Nivel de poder (1-100): "))
            if 1 <= poder <= 100:
                break
            print("Debe estar entre 1 y 100.")
        except ValueError:
            print("Ingresa un entero válido.")

    if 71 <= poder <= 100:
        print(f"→ {nombre} ingresa a la Casa del Fénix 🔥")
        fenix += 1
    elif 41 <= poder <= 70:
        print(f"→ {nombre} ingresa a la Casa del Grifo 🦅")
        grifo += 1
    else:
        print(f"→ {nombre} ingresa a la Casa del Búho 🦉")
        buho += 1

    if poder > mejor_poder:
        mejor_poder = poder

print(f"\n✨ RESULTADOS DE LA CLASIFICACIÓN ✨")
print(f"Casa del Fénix: {fenix}")
print(f"Casa del Grifo: {grifo}")
print(f"Casa del Búho: {buho}")
print(f"Aprendiz más poderoso: {mejor_nombre} con poder {mejor_poder}")