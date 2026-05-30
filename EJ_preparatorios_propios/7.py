temperaturas_criticas = 0
temperaturas_normales = 0
temperaturas_bajas = 0
sensores = 0

while True:
    try:
        temperatura_cada_sensor = float(input("Ingrese la temperatura del sensor :   "))
        sensores += 1
    except ValueError:
        print("Ingrese una opcion Valida")
        continue

    if temperatura_cada_sensor > 80 :
        print("ALERTA: temperatura crítica")
        temperaturas_criticas += 1
    elif temperatura_cada_sensor >= 50 and temperatura_cada_sensor <= 80:
        print("Normal Operativo")
        temperaturas_normales += 1
    elif temperatura_cada_sensor < 50 :
        print("Temperatura Baja")
        temperaturas_bajas += 1
    
    
    if sensores == 5 :
        print()
        print(f"Temperaturas Criticas : {temperaturas_criticas}")
        print(f"Temperaturas Normales : {temperaturas_normales}")
        print(f"Temperaturas Bajas : {temperaturas_bajas}")
        break
    