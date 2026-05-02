compras = ["espada", "pocion", "escudo"]

precios= {"espada": 100, "pocion": 50, "escudo": 80}

subtotal = 0

for producto in compras:
    subtotal += precios[producto]

if subtotal > 200:
    total_final = subtotal * 0.90

else:
    total_final = subtotal

print(f"El total final es de: ${total_final}")