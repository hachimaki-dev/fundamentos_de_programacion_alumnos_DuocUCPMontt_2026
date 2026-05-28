criticas = 0
normales = 0
bajas = 0

for i in range (1, 6):
    temperatura = float(input(f"Ingresa valor de la T°{i}: "))
    if temperatura > 80:
        print("ALERTA: temperatura crítica")
        criticas += 1
    elif temperatura >=50 and temperatura <= 80:
        print("Normal operativo")
        normales +=1
    else:
        print("Temperatura baja")
        bajas += 1
        
print(f"Temperaturas críticas: {criticas}")
print(f"Temperaturas normales: {normales}")
print(f"Temperaturas bajas: {bajas}")