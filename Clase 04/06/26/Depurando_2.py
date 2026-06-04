#Desafío 2 — Clasificación de Aprendices de Magia
#La Academia Arcana necesita clasificar a sus nuevos aprendices en tres casas según su poder mágico. El sistema debe registrar cada estudiante y generar estadísticas al final.

#📋 Requisitos del programa:
#Pedir cuántos aprendices se registrarán (entero positivo).
#Para cada aprendiz pedir su nombre mágico (mínimo 3 caracteres) y su nivel de poder (entero entre 1 y 100).
#Clasificación por poder: 71 a 100 → "Casa del Fénix", 41 a 70 → "Casa del Grifo", 1 a 40 → "Casa del Búho".
#Al finalizar mostrar cuántos aprendices hay en cada casa.
#Mostrar el nombre y poder del aprendiz más poderoso (el de mayor puntaje).


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

    if poder >= 71:
        print(f"→ {nombre} ingresa a la Casa del Fénix 🔥")
        fenix += 1
    elif poder >= 40:
        print(f"→ {nombre} ingresa a la Casa del Grifo 🦅")
        grifo += 1
    else:
        print(f"→ {nombre} ingresa a la Casa del Búho 🦉")
        buho += 1

    if poder > mejor_poder:
        mejor_nombre = nombre

print(f"\n✨ RESULTADOS DE LA CLASIFICACIÓN ✨")
print(f"Casa del Fénix: {fenix}")
print(f"Casa del Grifo: {grifo}")
print(f"Casa del Búho: {buho}")
print(f"Aprendiz más poderoso: {mejor_nombre} con poder {mejor_poder}")