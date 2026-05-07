boss = {'hp': 100,
        'estado': 'vivo'}

valor_golpe_critico = 150

boss["hp"] -= valor_golpe_critico

if boss["hp"] <= 0 :
    boss["hp"] = 0
    boss["estado"] = "muerto"

print(boss)