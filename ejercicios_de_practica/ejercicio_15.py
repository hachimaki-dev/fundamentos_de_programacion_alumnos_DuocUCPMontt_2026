tienda = {"espada": {"precio": 250, "stock": 3}, "escudo":{"precio": 150, "stock": 5}}

capital_total = 0

for producto, datos in tienda.items():
    valor_producto = datos["precio"] * datos["stock"]
    capital_total += valor_producto

print(f"El capital total es de: ${capital_total}")