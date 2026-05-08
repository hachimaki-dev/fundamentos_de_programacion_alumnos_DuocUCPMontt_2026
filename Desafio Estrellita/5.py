partidas = [
    {'resultado': 'victoria', 'minutos': 32},
    {'resultado': 'derrota',  'minutos': 18},
    {'resultado': 'victoria', 'minutos': 45},
    {'resultado': 'derrota',  'minutos': 22},
    {'resultado': 'victoria', 'minutos': 38},
    {'resultado': 'derrota',  'minutos': 11},
]

registro_sesion = {
    "victorias": 0, 
    "derrotas": 0, 
    "tiempo total": 0, 
    "promedio tiempo victorias": 0
}

tiempo_victorias = 0

for partida in partidas:
    if partida.get("resultado") == "victoria":
        registro_sesion['victorias'] += 1
        tiempo_victorias += partida.get("minutos")
    else:
        registro_sesion['derrotas'] += 1

    registro_sesion['tiempo total'] += partida.get("minutos")

    if registro_sesion.get("victorias") > 0:
        registro_sesion["promedio tiempo victorias"] = tiempo_victorias / registro_sesion.get("victorias")

for key in registro_sesion.keys():
    print(f"{key.capitalize()}: {registro_sesion.get(key)}")