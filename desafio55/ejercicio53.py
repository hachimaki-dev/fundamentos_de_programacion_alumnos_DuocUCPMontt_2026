print("Quiero Queque")
elo = 1500
rivales = [{'id': 1, 'elo': 1200}, {'id': 2, 'elo': 1490}, {'id': 3, 'elo': 1800}]
diferencia_minima = 999

rival_elegido = None
for rival in rivales:
    diferencia = abs(elo - rival["elo"])
    if diferencia < diferencia_minima:
        diferencia_minima = diferencia
        rival_elegido = rival["id"]

print(f"El rival elegido por el sistema es {rival_elegido}")
print("Quiero queque")