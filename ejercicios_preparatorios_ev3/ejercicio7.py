temperaturas_criticas = 0 
temperaturas_normales = 0 
temperaturas_bajas = 0 

for i in range(1, 6):
    temperatura_sensores = float(input(f"Ingrese la temperatura del sensor {i} (°C): "))

    if temperatura_sensores > 80:
        print("ALERTA: temperatura crítica")
        temperaturas_criticas += 1

    elif temperatura_sensores >= 50 and temperatura_sensores <= 80:
        print("Normal operativo")
        temperaturas_normales += 1 
    else:
        print("Temperatura baja")
        temperaturas_bajas += 1

print("\n---- RESUMEN ----")
print(f"Temperaturas criticas: {temperaturas_criticas}")
print(f"Temperaturas normales: {temperaturas_normales}")
print(f"Temperaturas bajas: {temperaturas_bajas}\n")