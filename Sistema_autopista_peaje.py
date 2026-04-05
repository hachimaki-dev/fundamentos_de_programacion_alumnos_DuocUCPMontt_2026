dinero_acumulado=0
autos=0
motos=0
camiones=0

while True:
    tipo_de_auto= input("Ingrese el tipo de vehículo (AUTO, MOTO, CAMION O SALIR): ")
    if tipo_de_auto == "AUTO":
        dinero_acumulado+= 1500
        autos+=1
    elif tipo_de_auto== "MOTO":
        dinero_acumulado+=500
        motos+=1
    elif tipo_de_auto== "CAMION":
        dinero_acumulado+=3500
        camiones+=1
    elif tipo_de_auto== "SALIR":
        break
    elif tipo_de_auto!= "AUTO" or "MOTO" or "CAMION":
        print("El vehiculo ingresado es incorrecto, intentalo nuevamente")
        
total_vehiculos= autos + motos + camiones
print(f"Total recaudado: ${dinero_acumulado}")

if total_vehiculos>0:
    porcentaje_autos= (autos/total_vehiculos)*100
    porcentaje_motos= (motos/total_vehiculos)*100
    porcentaje_camiones= (camiones/total_vehiculos)*100

    if autos>motos and autos>camiones:
        print("El vehiculo que mas paso es: AUTO")
    elif motos>autos and motos>camiones:
        print("El vehiculo que mas pasó es: MOTO")
    elif camiones>autos and camiones>motos:
        print("El vehículo que mas pasó es: CAMIONES")
