boss = {"hp": 100, "estado": "vivo"}

boss["hp"] -= 150

if boss["hp"] < 0:
    diferencia = abs(boss["hp"])
    boss["hp"] += diferencia
    boss["estado"] = "muerto"

print(boss)