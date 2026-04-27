autos = 0
camiones = 0    #Establecemos contadores
motos = 0
dinero = 0
while True:
    vehiculo = input("¿Que tipo de vehiculo trae?  Auto, Camion o Moto. Escriba SALIR para terminar la operación. ")
    if vehiculo == "SALIR":
        break
    if vehiculo == "Auto":
        autos += 1
        dinero += 1500
    elif vehiculo == "Camion":
        camiones += 1
        dinero += 3500
    elif vehiculo == "Moto":
        motos += 1
        dinero += 500
    else:
        print("Solo se admiten autos, camiones y motos.")

total_vehiculos = autos + camiones + motos
print(f"Pasaron {autos} autos.")
print(f"Pasaron {camiones} camiones.")
print(f"Pasaron {motos} motos.")
print(f"Han pasado un total de {total_vehiculos} vehiculos.")
print(f"Se ha recaudado un total de : ${dinero} pesos.")
porc_autos = (autos/total_vehiculos) * 100
porc_camiones = (camiones/total_vehiculos) * 100 #SACAMOS LOS PORCENTAJES DE LOS VEHICULOS QUE PASARON EL PEAJE
porc_motos = (motos/total_vehiculos) * 100
print(f"{porc_autos}%")
print(f"{porc_camiones}%")
print(f"{porc_motos}%")
if autos > motos and autos > camiones:
    print("Ganador del día: Autos.")
elif camiones > camiones and autos > motos:
    print("Ganador del día: Camiones.")
elif motos > motos and autos > camiones:
    print("Ganador del dia: Motos.")