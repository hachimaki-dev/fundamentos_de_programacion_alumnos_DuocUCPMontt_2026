compras = ['Espada', 'Pocion', 'Espada']
precios = {'Espada': 100, 'Pocion': 50}

subtotal_compra = 0

for nombre, precio in precios.items() :
    for compra in compras :
        if compra == nombre :
            subtotal_compra += precio

total_final = 0

if subtotal_compra > 200 :
    total_final = subtotal_compra * 0.1

print(subtotal_compra - total_final)