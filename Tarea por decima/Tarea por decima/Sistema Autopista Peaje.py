# Sistema Autopista Peaje
# Objetivo: Contador analítico de transporte para un peaje de carretera.

# 1. Usar bucle infinito hasta que el cobrador ingrese tipo vehiculo "SALIR".
# 2. Los tipos que se pueden ingresar son: "AUTO", "CAMION", "MOTO".
# 3. Precios: AUTO=$1500, MOTO=$500, CAMION=$3500. Si introducen otra cosa muestra error.
# 4. Acumular en todo momento LA CANTIDAD de cada vehiculo que pasó.
# 5. Acumular el DINERO GLOBAL generado.
# 6. Al poner "SALIR", muestra un cierre de caja: (Ganancia Total, y por porcentaje aproximado qué tipo de vehiculo es el ganador del dia, ej: pasaron mas motos que autos).

contador_auto = 0
contador_moto = 0 
contador_camion = 0
total = 0

while True:
    tipo_transporte = input("¿En que tipo de vehiculo maneja? (AUTO, MOTO Y CAMION): ")

    if tipo_transporte == "SALIR":
        break

    if tipo_transporte == "AUTO":
        contador_auto += 1
        total += 1500
    elif tipo_transporte == "MOTO":
        contador_moto += 1
        total += 500
    elif tipo_transporte == "CAMION":
        contador_camion += 1
        total += 3500
    else:
        print("Error")

print(f"Ganacia total ${total},  ")

total_vehiculos = contador_auto + contador_moto + contador_camion

if total_vehiculos == 0:
    print("No hubieron Vehiculos")
else:
    if contador_auto > contador_moto and contador_auto > contador_camion:
        ganador = "AUTOS"
    elif contador_moto > contador_auto and contador_moto > contador_camion:
        ganador = "MOTOS"
    elif contador_camion > contador_auto and contador_camion > contador_moto:
        ganador = "CAMIONES"
    else:
        ganador = "EMPATE"

    print(f"El vehiculo ganador son los {ganador}")
        
