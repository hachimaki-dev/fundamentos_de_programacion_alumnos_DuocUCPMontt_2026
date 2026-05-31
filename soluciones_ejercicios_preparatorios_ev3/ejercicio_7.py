temperatura_en_sensores = []
sensores_temperatura_crítica = 0
sensores_temperatura_normal = 0
sensores_temperatura_baja = 0
for i in range(1,6):
    while True:
        try:
            temperatura = float(input(f"Ingrese la temperatura del sensor N°{i}: "))
            break
        except ValueError:
            print("ERROR: Ingrese un número decimal o entero")

    temperatura_en_sensores.append(temperatura)
    if temperatura > 80.0:
        sensores_temperatura_crítica += 1
    elif temperatura >= 50 and temperatura <=80:
        sensores_temperatura_normal += 1
    else:
        sensores_temperatura_baja += 1
print(f"Temperaturas críticas: {sensores_temperatura_crítica} \nTemperaturas normales: {sensores_temperatura_normal} \nTemperaturas bajas: {sensores_temperatura_baja}")