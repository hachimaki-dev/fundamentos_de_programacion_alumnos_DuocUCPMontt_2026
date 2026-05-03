tienda = {
    'pocion': {'precio': 50, 'stock': 3},
    'espada': {'precio': 200, 'stock': 1}
}

capital_total = 0


for item in tienda.values():
    capital_total += item['precio'] * item['stock']

print(capital_total)
