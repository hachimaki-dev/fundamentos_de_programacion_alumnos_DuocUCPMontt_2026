conductor = 95
multa_gravisima = 120
multa_grave_camion = 80
tipo_de_auto = "Camion"

if tipo_de_auto == "Camion" and conductor > multa_grave_camion :
    print("Multa Grave Camión")

elif tipo_de_auto == "Auto" and conductor > 120 :
    print ("Multa Grave")