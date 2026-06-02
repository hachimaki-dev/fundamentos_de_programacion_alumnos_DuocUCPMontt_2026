#Ejercicio 13 — Inventario de computadores en una empresa TI
#Un técnico registra computadores en el sistema de inventario. Ingresa cuántos equipos ingresarán. Para cada computador:

#Código de activo: mínimo 6 caracteres, sin espacios
#Año de fabricación: entero entre 1990 y 2026 (validado)
#¿Por qué un rango? Validar solo "entero positivo" aceptaría valores absurdos como 3 o 9999. Un rango razonable (1990 a año actual) es más realista y te obliga a practicar validación de rango, una habilidad muy útil para la evaluación.

#Clasifica:

#Fabricado antes del año 2018 → Equipo obsoleto
#Fabricado en 2018 o después → Equipo vigente
#Muestra el resumen al finalizar.

while True:
    try:
        cantidad_equipos = int(input("Ingrese la cantidad de equipos: "))
        if cantidad_equipos > 0:
            break
        else:
            print("Error: la cantidad de equipos no puede ser menor a 0.")
    except ValueError:
        print("Error: ingresa un número entero positivo válido.")

obsoleto = 0
vigente = 0

for i in range(cantidad_equipos):
    while True:
        codigo_equipo = input(f"Ingresa código del computador {i + 1}: ").strip().upper()
        if len(codigo_equipo) >= 6 and " " not in codigo_equipo:
            break
        else:
            print("Error: El código debe tener al menos 6 caracteres, sin espacios.")
    
    while True:
        try:
            año_fabricacion = int(input(f"Año de fabricación equipo {codigo_equipo}: "))
            if 1990 <= año_fabricacion <= 2026:
                break
            elif año_fabricacion < 1990:
                print("Error: El equipo no puede ser anterior al año 1990.")
            else:
                print("Error: El año del equipo no puede ser posterior al año 2026.")
        except ValueError:
            print("Error: Ingresa un año válido, en formato numérico.")
    
    if año_fabricacion < 2018:
        obsoleto += 1
        print(f"{codigo_equipo} está obsoleto.")
    else:
        vigente += 1
        print(f"{codigo_equipo} está vigente.")

print("\n-----------------RESUMEN-------------------------")
print(f"Equipos obsoletos = {obsoleto} computadores")
print(f"Equipos vigentes = {vigente} computadores")
print("---------------------------------------------------")