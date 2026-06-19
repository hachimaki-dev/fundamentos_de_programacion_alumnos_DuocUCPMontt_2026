print("🏰 GRAN GREMIO DE AVENTUREROS")
print("Sistema de Registro y Recompensas")

while True:
    try:
        cantidad = int(input("¿Cuántos aventureros registrar? "))
        if cantidad > 0:
            break
        print("Debe ser mayor a 0.")
    except ValueError:
        print("Ingresa un entero válido.")

aventureros = []
legendarios = 0
veteranos = 0
novatos = 0
aprendices = 0
mejor_nombre = ""
mejor_oro = 0
total_oro = 0
suma_misiones = 0

for i in range(cantidad):
    print(f"\n--- Aventurero {i+1} ---")

    while True:
        nombre = input("Nombre del aventurero: ").strip()
        if len(nombre) >= 2:
            break
        print("El nombre debe tener al menos 2 caracteres.")

    while True:
        try:
            misiones = int(input("Misiones completadas (1-50): "))
            if 1 <= misiones <= 50:
                break
            print("Debe estar entre 1 y 50.")
        except ValueError:
            print("Ingresa un entero válido.")

    while True:
        try:
            dificultad = int(input("Dificultad promedio (1-10): "))
            if 1 <= dificultad <= 10:
                break
            print("Debe estar entre 1 y 10.")
        except ValueError:
            print("Ingresa un entero válido.")

    oro = misiones * dificultad * 10

    if oro >= 3000:
        rango = "Rango Legendario"
        legendarios += 1
    elif oro >= 1500:
        rango = "Rango Veterano"
        veteranos += 1
    elif oro > 500:
        rango = "Rango Novato"
        novatos += 1
    else:
        rango = "Rango Aprendiz"
        aprendices += 1

    print(f"→ {nombre}: {oro} monedas de oro — {rango}")

    if oro >= mejor_oro:
        mejor_nombre = nombre
        mejor_oro = oro

    aventurero = {"nombre": nombre, "misiones": misiones, "dificultad": dificultad, "oro": oro, "rango": rango}
    aventureros.append(aventurero)
    total_oro += oro
    suma_misiones += misiones

promedio_misiones = suma_misiones / len(aventureros)

print(f"\n🏰 RESUMEN DEL GREMIO")
print(f"Total de aventureros: {cantidad}")
print(f"Rango Legendario: {legendarios}")
print(f"Rango Veterano: {veteranos}")
print(f"Rango Novato: {novatos}")
print(f"Rango Aprendiz: {aprendices}")
print(f"Aventurero más rico: {mejor_nombre} con {mejor_oro} monedas")
print(f"Total de oro del gremio: {total_oro}")
print(f"Promedio de misiones: {promedio_misiones}")