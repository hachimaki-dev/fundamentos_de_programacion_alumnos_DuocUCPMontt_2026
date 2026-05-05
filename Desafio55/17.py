tipo_de_v = "Camion"
vel_camion = 95 
vel_auto = 220
vel_camion_max  = 80
vel_auto_max = 120

if tipo_de_v == "Camion" and vel_camion >= vel_camion_max:
    print("Multa Grave Camion")

elif tipo_de_v == "Auto" and vel_auto >= vel_auto_max:
    print("Multa Gravisima")

else:
    print("No Hay Multa")