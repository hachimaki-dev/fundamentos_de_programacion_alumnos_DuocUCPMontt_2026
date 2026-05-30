# Ejercicio 13 — Inventario de computadores en una empresa TI
# Un técnico registra computadores en el sistema de inventario. Ingresa cuántos equipos ingresarán. Para cada computador:

# Código de activo: mínimo 6 caracteres, sin espacios
# Año de fabricación: entero entre 1990 y 2026 (validado)
# ¿Por qué un rango? Validar solo "entero positivo" aceptaría valores absurdos como 3 o 9999. Un rango razonable (1990 a año actual) es más realista y te obliga a practicar validación de rango, una habilidad muy útil para la evaluación.

# Clasifica:

# Fabricado antes del año 2018 → Equipo obsoleto
# Fabricado en 2018 o después → Equipo vigente
# Muestra el resumen al finalizar.


while True:
    try:

        ingreso_de_computador = int(input("Ingrese la cantidad de computadores: "))

        if ingreso_de_computador > 0:
            break
        else:
            print("Ingrese un número entero positivo\n")

    except ValueError:
        print("Ingrese un número entero positivo\n")

fabricado_antes = 0
fabricado_despues = 0
fabricados_totales = 0

for i in range(1,ingreso_de_computador + 1):
    while True:
            
        codigo_del_computador = input(f"Ingrese el código del activo N°{i}: ")

        if len(codigo_del_computador) >= 6 and " " not in codigo_del_computador:
            break
        else:
            print("Ingrese un mínimo 6 caracteres, sin espacios\n")

    while True:
        try:
            epoca_de_fabricación = int(input("Ingrese el año de fabricación: "))

            if epoca_de_fabricación >= 1990 and epoca_de_fabricación <= 2026:
                print(f"Ingreso exitoso del computador N°{ingreso_de_computador} con código {codigo_del_computador}\n")
                break
            else:
                print("Ingrese el año de fabrico entre el 1990 y 2026\n")
        except ValueError:
            print("Ingrese un año con números positivos\n")    

    if epoca_de_fabricación < 2018:
        fabricado_antes += 1
    else:
        fabricado_despues += 1

fabricados_totales = fabricado_antes + fabricado_despues
        
print("Resultados\n")
print(f"Equipo obsoleto: {fabricado_antes}")
print(f"Equipo vigente: {fabricado_despues}")
print(f"Equipo totales: {fabricados_totales}")








