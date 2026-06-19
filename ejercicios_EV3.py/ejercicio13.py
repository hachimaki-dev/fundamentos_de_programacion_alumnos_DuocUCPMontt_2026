while True:
    try:
        n = int(input("¿Cuántos equipos se registrarán? "))
        if n > 0:
            break
        print("Error: debe ser un entero positivo.")
    except ValueError:
        print("Error: debe ser un entero positivo.")

obsoletos = 0
vigentes  = 0

for i in range(n):
    print("\n--- Equipo", i+1, "---")

    while True:
        codigo = input("  Código de activo: ").strip().upper()
        if len(codigo) >= 6 and " " not in codigo:
            break
        print('Error: mínimo 6 caracteres, sin espacios.')

    while True:
        try:
            anio = int(input("  Año de fabricación (1990-2026): "))
            if 1990 <= anio <= 2026:
                break
            print("Error: el año debe estar entre 1990 y 2026.")
        except ValueError:
            print("Error: ingresa un número entero.")

    if anio < 2018:
        print("Equipo obsoleto")
        obsoletos += 1
    else:
        print("Equipo vigente")
        vigentes += 1

print('Resumen del inventario')
print("Equipos obsoletos:", obsoletos)
print("Equipos vigentes: ", vigentes)