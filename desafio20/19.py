compras = ["espada", "poción", "espada"]
precios = {"espada": 100, "poción": 50}
subtotal = 0
for objeto in compras:
    if objeto in precios:
        subtotal += precios[objeto]
if subtotal > 200:
    total_final = subtotal * .9
    print(total_final)