#Ejercicio 19 — Registro de vehículos en una empresa de transporte de carga
#Una empresa de transporte registra su flota. El sistema debe:

#Preguntar cuántos vehículos se registrarán (entero positivo, validado)
#Para cada vehículo:
#Patente: exactamente 6 caracteres, sin espacios
#Capacidad de carga en toneladas: entero positivo, validado
#Clasificar:
#Capacidad > 15 ton → Camión pesado
#Capacidad ≤ 15 ton → Camión liviano
#Al finalizar:
#"La flota cuenta con 3 camiones pesados y 5 camiones livianos. Registro completado."

camion_pesado = []
camion_liviano = []

while True:
    try:
        registro_vehiculos = int(input("Cantidad de vehículos a registrar: "))
        if registro_vehiculos <= 0:
            print("Error: la cantidad debe ser mayor a 0.")
        else:
            break
    except ValueError:
        print("Error: ingresa una cantidad válida")

for v in range(registro_vehiculos):

    while True:
        patente = input(f"Patente del camión {v + 1}: ").strip().upper()
        if len(patente) == 6 and " " not in patente:
            if (patente in camion_liviano) or (patente in camion_pesado):
                print("Error: La patente ya ha sido registrada.")
            else:
                break
        else:
            print("Error: La patente debe tener 6 caracteres, sin espacios.")
    
    while True:
        try:
            capacidad = int(input(f"Capacidad (ton) del camión con patente {patente}: "))
            if capacidad <= 0:
                print("Error: La capacidad del camión debe ser mayor a 0.")
            else:
                break
        except ValueError:
            print("Error: La capacidad del camión debe ingresarse en formato numérico.")
        
    if capacidad > 15:
        camion_pesado.append(patente)
    else:
        camion_liviano.append(patente)
    
print(f"Camión pesado = {camion_pesado}")
print(f"Camión liviano = {camion_liviano}")
print(f"La flota cuenta con {len(camion_pesado)} camiones pesados y {len(camion_liviano)} camiones livianos. Registro completado.")