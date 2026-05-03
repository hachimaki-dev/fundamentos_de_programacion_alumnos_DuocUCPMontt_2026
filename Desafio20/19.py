compras = ['espada', 'pocion', 'espada'] 
precios = {'espada': 100, 'pocion': 50}
subtotal = 0
total_final = 0
for items in compras:
    if items == "espada":
        subtotal += precios["espada"]
    elif items == "pocion":
        subtotal += precios["pocion"]
if subtotal > 200:
    total_final = subtotal * 0.9
    print(total_final)
else:
    print(total_final)