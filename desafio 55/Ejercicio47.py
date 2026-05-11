boss = {'hp': 100, 'estado': 'vivo'}

print(boss)
print("Le haz dado un golpe critico, le has restado 150 de HP")

boss["hp"] = boss["hp"] - 150
print(boss)
print("Corrigiendo errores")
if boss["hp"] < 0:
    boss["hp"] = 0
print(boss)