boss = {'hp': 100, 'estado': 'vivo'}
golpe_critico = 150
boss['hp'] -= 150
if boss['hp'] <= 0:
    boss["hp"] = 0
    boss["estado"] = "Muerto"
print(boss)