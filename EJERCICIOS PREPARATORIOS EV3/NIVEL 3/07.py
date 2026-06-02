#Ejercicio 7 — Clasificación de temperaturas en una planta industrial
#Una planta industrial mide la temperatura de 5 sensores. Cada temperatura es un número decimal (usa float() para leerlo, no int()). El operador las ingresa una a una.

#Nota sobre el Patrón 1 de referencia: El patrón usa int() como ejemplo genérico. En este ejercicio reemplázalo por float() porque las temperaturas pueden tener decimales (ej: 75.5).

#Clasifica cada temperatura con estos rangos exactos:

#Mayor a 80°C (> 80, no incluye 80) → "ALERTA: temperatura crítica"
#De 50°C a 80°C (>= 50 y <= 80) → "Normal operativo"
#Menor a 50°C (< 50) → "Temperatura baja"
#Condiciones de borde: Una temperatura de exactamente 80°C es "Normal operativo". Una de exactamente 50°C también es "Normal operativo".

#Al final, muestra cuántas lecturas cayeron en cada categoría.

#Ejemplo de salida:

#Temperaturas críticas: 2
#Temperaturas normales: 2
#Temperaturas bajas: 1

t_critica = 0
t_normales = 0
t_bajas = 0

for i in range (5):
    t_registrada = float(input(f"Ingresa la temperatura del sensor {i + 1}: " ))

    if t_registrada > 80:
        t_critica += 1
        print("ALERTA: temperatura crítica")
    elif 50 <= t_registrada <= 80:
        t_normales += 1
        print("Normal operativo")
    else:
        t_bajas += 1
        print("Temperatura baja")

print(f"Temperatura críticas: {t_critica}")
print(f"Temperaturas normales: {t_normales}")
print(f"Temperaturas bajas: {t_bajas}")