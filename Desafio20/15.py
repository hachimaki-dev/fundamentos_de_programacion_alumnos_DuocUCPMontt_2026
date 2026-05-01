tienda = {"pocion":{"precio":50, "stock":3}, "espada":{"precio":200,"stock":1}}
capital_total = 0
for articulo, valor in tienda.items():
    capital_total+= valor.get("precio") * valor.get("stock")
print(capital_total)