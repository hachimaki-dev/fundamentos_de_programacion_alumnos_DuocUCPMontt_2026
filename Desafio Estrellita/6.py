resenas = [
    {'anfitrion': 'Mario',   'nota': 5},
    {'anfitrion': 'Claudia', 'nota': 3},
    {'anfitrion': 'Mario',   'nota': 4},
    {'anfitrion': 'Claudia', 'nota': 5},
    {'anfitrion': 'Mario',   'nota': 2},
    {'anfitrion': 'Claudia', 'nota': 4},
    {'anfitrion': 'Mario',   'nota': 5},
]

totales = {}
conteos = {}

promedios = []

for resena in resenas:
    if resena.get("anfitrion") not in totales.keys():
        totales[resena.get("anfitrion")] = resena.get("nota")
        conteos[resena.get("anfitrion")] = 1
    else:
        totales[resena.get("anfitrion")] += resena.get("nota")
        conteos[resena.get("anfitrion")] += 1

for anfitrion in totales.keys():
    dict_aux = {}
    dict_aux["anfitrion"] = anfitrion
    dict_aux["promedio"] = round(totales.get(anfitrion) / conteos.get(anfitrion), 2)
    promedios.append(dict_aux)                                                              # Estructura del diccionario en promedios = []: {"anfitrion": "(nombre)", "promedio": (promedio)}
    
anfitrion_mejor_rep = [promedios[0]]

for item in promedios:
    if item.get("promedio") > anfitrion_mejor_rep[0].get("promedio") and item.get("anfitrion") != anfitrion_mejor_rep[0].get("anfitrion"):
        anfitrion_mejor_rep.clear()
        anfitrion_mejor_rep = item
    elif item.get("promedio") == anfitrion_mejor_rep[0].get("promedio") and item.get("anfitrion") != anfitrion_mejor_rep[0].get("anfitrion"): 
        anfitrion_mejor_rep.append(item)

for item in anfitrion_mejor_rep:
    print(f"{item.get("anfitrion")}: {item.get("promedio")}")

if len(anfitrion_mejor_rep) > 1:
    print("Empate en reputación")
else:
    print(f"Mejor reputación: {anfitrion_mejor_rep[0].get("anfitrion")}")