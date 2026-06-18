# Ejercicio 7 — Clasificación de temperaturas en una planta industrial

temperaturas_criticas = 0
temperaturas_normales = 0
temperaturas_bajas = 0

for i in range(5):

    temperatura = float(input(f"Ingrese la temperatura del sensor {i + 1}: "))

    if temperatura > 80:
        print("ALERTA: temperatura crítica")
        temperaturas_criticas += 1

    elif temperatura >= 50:
        print("Normal operativo")
        temperaturas_normales += 1

    else:
        print("Temperatura baja")
        temperaturas_bajas += 1

print()
print(f"Temperaturas críticas: {temperaturas_criticas}")
print(f"Temperaturas normales: {temperaturas_normales}")
print(f"Temperaturas bajas: {temperaturas_bajas}")