print("=== AGENCIA ESPACIAL INTERNACIONAL ===")
print("Sistema de Registro de Astronautas")

while True:
    try:
        cantidad = int(input("¿Cuántos astronautas registrar? "))
        if cantidad > 0:
            break
        print("Debe ser un número positivo.")
    except ValueError:
        print("Entrada inválida. Ingresa un número entero.")

aptos = 0
entrenamiento = 0
suma_puntajes = 0

for i in range(cantidad):
    print(f"\n--- Astronauta {i+1} ---")

    while True:
        nombre = input("Nombre del astronauta: ").strip()
        if len(nombre) > 0:
            break
        print("El nombre no puede estar vacío.")

    while True:
        try:
            puntaje = int(input("Puntaje de aptitud (1-100): "))
            if 1 <= puntaje <= 100:
                break
            print("El puntaje debe estar entre 1 y 100.")
        except ValueError:
            print("Ingresa un número entero válido.")

    suma_puntajes += puntaje

    if puntaje >= 80:
        print(f"→ {nombre}: Apto para misión")
        aptos += 1
    else:
        print(f"→ {nombre}: En entrenamiento")
        entrenamiento += 1

promedio = suma_puntajes / cantidad
print(f"\n=== RESUMEN DE LA MISIÓN ===")
print(f"Aptos para misión: {aptos}")
print(f"En entrenamiento: {entrenamiento}")
print(f"Promedio general: {round(promedio,2)}")