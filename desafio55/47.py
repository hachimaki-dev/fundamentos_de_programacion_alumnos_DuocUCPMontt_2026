boss = {"hp": 100, "Estado": "vivo"}
golpe_crítico = 150
boss["hp"] = boss["hp"] - golpe_crítico
if boss["hp"] <= 0:
    boss["hp"] = 0
    boss["Estado"] = "muelto"
print(boss)