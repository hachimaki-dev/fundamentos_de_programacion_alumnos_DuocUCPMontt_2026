boss = {'hp': 100, 'estado': 'vivo'}
hit_crit = 150
boss["hp"] -= 150
if boss['hp'] <= 0:
    boss['hp'] = 0
    boss['estado'] = "muerto"
print(boss)