criticas = 0
normales = 0
bajas = 0

for i in range(1,6):
    temperatura_sensor = float(input(f"Ingrese la temperatura del sensor {i}: "))

    if temperatura_sensor > 80:
        criticas += 1
    
    elif temperatura_sensor >= 50 and temperatura_sensor <= 80:
        normales += 1

    else:
        bajas += 1

print("\nResumen temperaturas")
print(f"-Criticas: {criticas}")
print(f"-Normales: {normales}")
print(f"-Bajas: {bajas}")