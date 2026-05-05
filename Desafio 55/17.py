limite_velocidad_auto=120 #km/h
limite_velocidad_camion=80 #km/h

velocidad_vehiculo=95
tipo_vehiculo="Camion"

if tipo_vehiculo=="Camion" and velocidad_vehiculo > limite_velocidad_camion:
    print("Multa Grave Camion")
elif tipo_vehiculo=="Camion" and velocidad_vehiculo <= limite_velocidad_camion:
    print("Velocidad permitida")
 
elif tipo_vehiculo=="Auto" and velocidad_vehiculo > limite_velocidad_auto:
    print("Multa Gravisima")
elif tipo_vehiculo=="Auto" and velocidad_vehiculo <= limite_velocidad_auto:
    print("Velocidad permitida")
   


    