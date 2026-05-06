boss = {'hp': 100, 'estado': 'vivo'}
dmg = 150

if boss["hp"] - dmg < 0:
    boss["hp"] = 0
    boss["estado"] = "muerto"
else:
    boss["hp"] -= dmg

print(boss)