print("********INVERNADERO********")

alertas_consecutivas = 0

while True:
    temperatura = int(input("Ingrese temperatura actual: "))
    
    if temperatura == 0:
        print("Lectura de datos finalizada")
        break
    
    if 18 <= temperatura < 35:
        print(f"Estado: [ESTABLE] - Temperatura de {temperatura}°C dentro del rango optimo")
        alertas_consecutivas = 0

    elif temperatura >= 35:
        print(f"\n ⚠️  ¡Estado: [CRITICO] - Temperatura de {temperatura}°C! ⚠️ \n")
        print("\n¡Solo se permite debajo de 35°C en el rango optimo!\n")
        alertas_consecutivas += 1

        if alertas_consecutivas == 3:
            print("¡¡¡ACTIVANDO ASPERSORES DE EMERGENCIA!!!")

    elif temperatura < 18:
        print(f"Estado: [PRECUACION] - Temperatura baja {temperatura}°C")
        alertas_consecutivas = 0