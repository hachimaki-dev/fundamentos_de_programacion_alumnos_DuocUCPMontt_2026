boss = {'hp': 100, 'estado': 'vivo'}
daño = 150

boss['hp'] -= daño
if boss['hp'] < 0:
    boss['hp'] = 0
 
if boss['hp'] <= 0:
    boss['estado'] = 'muerto'
 
print(boss)
print()
 
 