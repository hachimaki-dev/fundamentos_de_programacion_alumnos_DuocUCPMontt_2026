subtotal = 0

compras = [ "Espada", "Poción", "Espada" ]
precios = { "Espada": 100, "Poción": 50 }

for i in compras:
    subtotal = subtotal + precios[i]

if subtotal > 200:
    total = subtotal - (subtotal / 100 * 10)
    print(f"10% de descuento. Total: {total}")
else:
    total = subtotal
    print(f"Total: {total}")
