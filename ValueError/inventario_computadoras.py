# Ejercicio 13 — Inventario de computadores en una empresa TI
# Un técnico registra computadores en el sistema de inventario. Ingresa cuántos equipos ingresarán. Para cada computador:

# Código de activo: mínimo 6 caracteres, sin espacios
# Año de fabricación: entero entre 1990 y 2026 (validado)
# ¿Por qué un rango? Validar solo "entero positivo" aceptaría valores absurdos como 3 o 9999. Un rango razonable (1990 a año actual) es más realista y te obliga a practicar validación de rango, una habilidad muy útil para la evaluación.

# Clasifica:

# Fabricado antes del año 2018 → Equipo obsoleto
# Fabricado en 2018 o después → Equipo vigente
# Muestra el resumen al finalizar.
id_computadora = []
inventario = {
    "obsoletos": 0,
    "vigentes": 0
}

while True:
    try:
        cantidad_computadoras = int(input("¿Cuántos equipos ingresarán? "))
        if cantidad_computadoras <= 0:
            print("Debe ser un número positivo")
            continue
        
        for computadora in range(cantidad_computadoras):
            id_activo = input("Ingrese el código de activo \n").upper()
            if len(id_activo) < 6 or " " in id_activo:
                print("Debe tener mínimo 6 caracteres y sin espacios")
                continue
            año_de_fabricacion = int(input("Ingrese el año de fabricación \n"))
            if año_de_fabricacion < 1990 or año_de_fabricacion > 2026:
                print("Año inválido, solo entre 1990 y 2026")
                continue
            if año_de_fabricacion < 2018:
                print("Equipo obsoleto")
                inventario["obsoletos"] += 1
            elif año_de_fabricacion >= 2018:
                print("Equipo vigente")
                inventario["vigentes"] += 1
            id_computadora.append(id_activo)
        print(f"Resumen: {inventario}")
        print(f"Id de cada computadora : {id_computadora}")
        break

    except Exception as error:
        print(f"Error: {error}")