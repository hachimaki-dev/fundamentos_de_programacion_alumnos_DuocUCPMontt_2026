temperaturas_criticas = []
temperaturas_normales = []
temperaturas_bajas = []

for sensor in range(1,6):
    temperatura_sensor = float(input(f"Ingrese la temperatura del sensor actual n°{sensor} : "))
    if temperatura_sensor > 80:
        print("ALERTA: Temperatura critica.")
        temperaturas_criticas.append(temperatura_sensor)
    elif temperatura_sensor >= 50 and temperatura_sensor <= 80:
        print("Normal operativo.")
        temperaturas_normales.append(temperatura_sensor)
    else:
        print("Temperatura baja")
        temperaturas_bajas.append(temperatura_sensor)
print(f"Temperaturas criticas: {len(temperaturas_criticas)}.\nTemperaturas normales: {len(temperaturas_normales)}.\nTemperaturas bajas: {len(temperaturas_bajas)}.")
