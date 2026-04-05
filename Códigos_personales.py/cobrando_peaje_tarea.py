moto_str = "MOTO"
#500
auto_str = "AUTO"
#1500
Camionsote_str = "CAMION"
#3500
Salir_de_la_pega = "SALIR"
#dinero global
platita_peaje = 0
vehiculo = ""
cantidad_autos = 0
cantidad_camiones = 0
cantidad_moto = 0
salir_statement = True
vehiculos_totales = cantidad_moto + cantidad_camiones + cantidad_autos
print("MONITOR PEAJE")


while salir_statement == True:
    vehiculos_totales = cantidad_moto + cantidad_camiones + cantidad_autos
    
    print("""QUE VEHíCULO DESEA INGRESAR: 
          AUTO 
          MOTO
          CAMION""")
    print(f"(Inserte {Salir_de_la_pega} para mostrar las estadísticas del peaje)")
    vehiculo = str(input(""))
    if vehiculo == auto_str:
        platita_peaje = platita_peaje + 1500
        cantidad_autos = cantidad_autos + 1
        print(f"Ha ingresado un {auto_str} al peaje")
    if vehiculo == moto_str:
        platita_peaje = platita_peaje + 500
        cantidad_moto = cantidad_moto + 1
        print(f"Ha ingresado un {moto_str} al peaje")
    if vehiculo == Camionsote_str: 
        platita_peaje = platita_peaje + 3500
        cantidad_camiones = cantidad_camiones + 1
        print(f"Ha ingresado un {Camionsote_str} al peaje")
    else:
        
         print("ERROR. Tal vehículo no existe dentro de las tarifas.")
    
    if vehiculo == Salir_de_la_pega:
        salir_statement = False
    else: 
        salir_statement = True
    
    
    
print("CIERRE DE CAJA")
vehiculos_totales = cantidad_moto + cantidad_camiones + cantidad_autos

if vehiculos_totales == 0:
    print(f"No pasó ningún vehículo, ${platita_peaje} pesos recaudados")
else:
    porcentaje_moto = float((cantidad_moto / vehiculos_totales)*100)
    porcentaje_autos = float((cantidad_autos / vehiculos_totales)*100)
    porcentaje_camiones = float((cantidad_camiones / vehiculos_totales)*100)

    print(f"Pasaron {vehiculos_totales} vehiculos en el peaje. Recaudando un total de ${platita_peaje} pesos")
    print(f"Hubo un {porcentaje_moto}% de motos, un {porcentaje_camiones}% de camiones, y un {porcentaje_autos}% de autos")
    print(f"{cantidad_camiones} camiones {cantidad_autos} autos {cantidad_moto} motos")


    