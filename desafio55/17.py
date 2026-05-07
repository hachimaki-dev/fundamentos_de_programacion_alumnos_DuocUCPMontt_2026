vehiculo = {"tipo": "Camión", "velocidad": 85}
auto = "Auto"
auto_limite = 120
auto_multa = "Multa Gravísima"
camion = "Camión"
camion_limite = 80
camion_multa = "Multa Grave Camión"
if vehiculo["tipo"] == auto and vehiculo["velocidad"] > auto_limite:
    print(auto_multa)
elif vehiculo["tipo"] == camion and vehiculo["velocidad"] > camion_limite:
    print(camion_multa)