compras = ['espada', 'pocion', 'espada']
precios = {'espada': 100, 'pocion': 50}

subtotal = 0

for item in compras:
    subtotal += precios[item]

if subtotal > 200:
    total_final = subtotal * 0.9
else:
    total_final = subtotal

print(total_final)