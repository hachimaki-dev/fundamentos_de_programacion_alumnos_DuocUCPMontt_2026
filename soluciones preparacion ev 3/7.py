contador_temperaturas_criticas = 0
contador_temperaturas_normales = 0
contador_temperaturas_bajas = 0

for i in range(1, 6) :
    while True :
        try :
            temperatura = float(input(f"Ingrese la temperatura del sensor {i}: "))

            if temperatura < 50 :
                contador_temperaturas_bajas += 1
            elif temperatura >= 50 and temperatura <= 80 :
                contador_temperaturas_normales += 1
            elif temperatura > 80 :
                contador_temperaturas_criticas += 1
            break
        except ValueError :
            print("Ingrese un valor numérico (decimal).")
        
print(f"Temperaturas críticas: {contador_temperaturas_criticas}")
print(f"Temperaturas normales: {contador_temperaturas_normales}")
print(f"Temperaturas bajas: {contador_temperaturas_bajas}")