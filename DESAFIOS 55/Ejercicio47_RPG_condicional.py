boss = {'hp': 100, 'estado': 'vivo'}

ataque = 150

boss['hp'] -= ataque

if boss['hp'] < 0:
    boss['hp'] = 0
    boss['estado'] = 'muerto'

print(boss)    