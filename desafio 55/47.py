boss = {'hp': 100, 'estado': 'vivo'}
danio_critico = 150

print(f"Estado inicial: {boss}")


boss['hp'] -= danio_critico
print(f"Vida tras el golpe: {boss['hp']}")

if boss['hp'] < 0:
    
    boss['hp'] = 0
    boss['estado'] = 'muerto'

# 4. Imprime al jefe
print(f"Estado final: {boss}")
