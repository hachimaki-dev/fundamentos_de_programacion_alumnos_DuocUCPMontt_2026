# Sistema Autopista Peaje
# Objetivo: Contador analítico de transporte para un peaje de carretera.

# 1. Usar bucle infinito hasta que el cobrador ingrese tipo vehiculo "SALIR".
# 2. Los tipos que se pueden ingresar son: "AUTO", "CAMION", "MOTO".
# 3. Precios: AUTO=$1500, MOTO=$500, CAMION=$3500. Si introducen otra cosa muestra error.
# 4. Acumular en todo momento LA CANTIDAD de cada vehiculo que pasó.
# 5. Acumular el DINERO GLOBAL generado.
# 6. Al poner "SALIR", muestra un cierre de caja: 
# (Ganancia Total, y por porcentaje aproximado qué tipo de vehiculo es el ganador del dia, ej: pasaron mas motos que autos).

print(" PEAJE AUTOPISTA ".center(40, "-"))

cantidad_autos = 0
cantidad_camiones = 0
cantidad_motos = 0
cantidad_vehiculos = 0
total_global = 0
precio = 0
vehiculo_ganador = ""
porcentaje_auto = 0
porcentaje_camion = 0
porcentaje_moto = 0

while True:
    tipo_vehiculo = input("Ingrese tipo de vehiculo: ").upper()

    if tipo_vehiculo == "SALIR":

        if cantidad_vehiculos > 0:
            porcentaje_auto = (cantidad_autos/cantidad_vehiculos)*100
            porcentaje_camion = (cantidad_camiones/cantidad_vehiculos)*100
            porcentaje_moto = (cantidad_motos/cantidad_vehiculos)*100

            if porcentaje_auto > porcentaje_camion and porcentaje_auto > porcentaje_moto:
                vehiculo_ganador = "AUTO"
            elif porcentaje_camion > porcentaje_auto and porcentaje_camion > porcentaje_moto:
                vehiculo_ganador = "CAMION"
            else:
                vehiculo_ganador = "MOTO"
        else:
            vehiculo_ganador = "No hay registro de vehiculos"

        print(f"Ganancia total: ${total_global}")
        print(f"Detalle porcentajes: Autos: {porcentaje_auto}% | Camion: {porcentaje_camion}% | Moto: {porcentaje_moto}%")
        print(f"Vehiculo ganador del día: {vehiculo_ganador}")
        break
    
    elif tipo_vehiculo == "AUTO":
        precio = 1500
        cantidad_autos += 1
        cantidad_vehiculos += 1
    elif tipo_vehiculo == "CAMION":
        precio = 3500
        cantidad_camiones += 1
        cantidad_vehiculos += 1
    elif tipo_vehiculo == "MOTO":
        precio = 500
        cantidad_motos += 1
        cantidad_vehiculos += 1
    else:
        print("Error: vehiculo no identificado")
        continue

    total_global += precio






