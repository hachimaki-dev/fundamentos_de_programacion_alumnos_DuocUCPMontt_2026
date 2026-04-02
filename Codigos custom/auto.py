"""
Objetivo: Contador analítico de transporte para un peaje de carretera.

1. Usar bucle infinito hasta que el cobrador ingrese tipo vehiculo "SALIR".
2. Los tipos que se pueden ingresar son: "AUTO", "CAMION", "MOTO".
3. Precios: AUTO=$1500, MOTO=$500, CAMION=$3500. Si introducen otra cosa muestra error.
4. Acumular en todo momento LA CANTIDAD de cada vehiculo que pasó.
5. Acumular el DINERO GLOBAL generado.
6. Al poner "SALIR", muestra un cierre de caja: (Ganancia Total, y por porcentaje aproximado qué tipo de vehiculo es el ganador del dia, ej: pasaron mas motos que autos).
"""
import time
Dinero_Total = 0
MOTOS_total = 0
AUTOS_total = 0
CAMION_total = 0
print("AUTO=$1500")
print("MOTO=$500")
print("CAMION=$3500")
while True:
    time.sleep(1)
    vehiculos_total = (input("Que vehiculo acaba de pasar? (Si quieres salir == SALIR) "))
    if vehiculos_total == "AUTO":
        Dinero_Total = Dinero_Total + 1500
        AUTOS_total = AUTOS_total + 1
        print(f"Paso {AUTOS_total} auto")
    elif vehiculos_total == "MOTO":
        Dinero_Total = Dinero_Total + 500
        MOTOS_total = MOTOS_total + 1
        print(f"Paso {MOTOS_total} moto")
    elif vehiculos_total == "CAMION":
        Dinero_Total = Dinero_Total + 3500
        CAMION_total = CAMION_total + 1
        print(f"Paso {CAMION_total} camion")
    elif vehiculos_total == "SALIR":
        break
    else:
        time.sleep(2)
        print("error")
        time.sleep(1)
if AUTOS_total > CAMION_total and AUTOS_total > MOTOS_total:
    print(f"El monto total es {Dinero_Total} y el tipo de vehiculo ganador del dia son los autos")
    print(f"Autos: {AUTOS_total}")
    print(f"Motos: {MOTOS_total}")
    print(f"Camiones: {CAMION_total}")
elif MOTOS_total > CAMION_total and MOTOS_total > AUTOS_total:
    print(f"El monto total es {Dinero_Total} y el tipo de vehiculo ganador del dia son las motos")
    print(f"Motos: {MOTOS_total}")
    print(f"Autos: {AUTOS_total}")
    print(f"Camiones: {CAMION_total}")
elif CAMION_total > AUTOS_total and CAMION_total > MOTOS_total:
    print(f"El monto total es {Dinero_Total} y el tipo de vehiculo ganador del dia son los camiones")
    print(f"Camiones: {CAMION_total}")
    print(f"Autos: {AUTOS_total}")
    print(f"Motos: {MOTOS_total}")
else:
    print(f"El monto total es {Dinero_Total} y no hay ganador")
    print(f"Autos: {AUTOS_total}")
    print(f"Motos: {MOTOS_total}")
    print(f"Camiones: {CAMION_total}")
    





