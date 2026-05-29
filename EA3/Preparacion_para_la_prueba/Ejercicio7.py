# Ejercicio 7 — Clasificación de temperaturas en una planta industrial
# Una planta industrial mide la temperatura de 5 sensores. Cada temperatura es un número decimal (usa float() para leerlo, no int()). El operador las ingresa una a una.

# Nota sobre el Patrón 1 de referencia: El patrón usa int() como ejemplo genérico. En este ejercicio reemplázalo por float() porque las temperaturas pueden tener decimales (ej: 75.5).

# Clasifica cada temperatura con estos rangos exactos:

# Mayor a 80°C (> 80, no incluye 80) → "ALERTA: temperatura crítica"
# De 50°C a 80°C (>= 50 y <= 80) → "Normal operativo"
# Menor a 50°C (< 50) → "Temperatura baja"
# Condiciones de borde: Una temperatura de exactamente 80°C es "Normal operativo". Una de exactamente 50°C también es "Normal operativo".

# Al final, muestra cuántas lecturas cayeron en cada categoría.

# Ejemplo de salida:

# Temperaturas críticas: 2
# Temperaturas normales: 2
# Temperaturas bajas: 1

sensor_numero = 1

temperatura_críticas = 0
temperatura_normales = 0
temperatura_bajas = 0

while True:
    try:
        for i in range(1,6):
            temperatura_ingresada = float(input(f"Ingrese la temperatura N°{sensor_numero}: "))
            sensor_numero += 1

            if temperatura_ingresada > 80:
                print("ALERTA: temperatura crítica\n")
                temperatura_críticas += 1
            elif temperatura_ingresada >= 50 and temperatura_ingresada <= 80:
                print("Normal operativo\n")
                temperatura_normales += 1
            elif temperatura_ingresada < 50:
                print("Temperatura baja\n")
                temperatura_bajas += 1
                
        print(f"Temperatura crítica: {temperatura_críticas}")
        print(f"Temperatura nomales: {temperatura_normales}")
        print(f"Temperaturas baja: {temperatura_bajas}")
        break
    except:
        print("Ingrese un número valido")


