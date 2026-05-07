mis_puntos = 1500

puntos_rivales = [{"id" : 1,
                  "elo" : 1200} ,

                  {"id" : 2,
                   "elo" : 1490} ,
                  
                   {"id" : 3,
                    "elo": 1800}]

rival_escogido = puntos_rivales[0]

diferencia_mas_cercana = mis_puntos

for punto_rival in puntos_rivales :
    diferencia_de_puntos = abs(mis_puntos - punto_rival["elo"])

    if diferencia_de_puntos < diferencia_mas_cercana :
        diferencia_mas_cercana = diferencia_de_puntos
        rival_escogido = punto_rival

print(rival_escogido["id"])