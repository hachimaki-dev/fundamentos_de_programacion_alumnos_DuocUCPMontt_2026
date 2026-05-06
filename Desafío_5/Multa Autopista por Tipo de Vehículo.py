
tipo_vehiculo = str(input("¿Qué tipo de vehículo manejas? (auto/camión): ")).lower()
Velocidad_del_Vehiculo = int(input(("¿A que velocidad va manejando? : ")))


if tipo_vehiculo == "auto" and Velocidad_del_Vehiculo >= 120:
    print (f"Usted va a manejando {Velocidad_del_Vehiculo} KM/H por lo tanto es una !Multa Grave¡")

elif tipo_vehiculo == "auto" and Velocidad_del_Vehiculo <= 120:
    print (f"Usted va a manejando {Velocidad_del_Vehiculo} KM/H por lo tanto es una !No tiene multa¡")

elif tipo_vehiculo == "camion" and Velocidad_del_Vehiculo >= 80:
    print (f"Usted va a manejando {Velocidad_del_Vehiculo} KM/H por lo tanto es una !Multa Grave¡")
    
elif tipo_vehiculo == "camion" and Velocidad_del_Vehiculo <= 80:
    print (f"Usted va a manejando {Velocidad_del_Vehiculo} KM/H por lo tanto es una !No tiene multa¡")