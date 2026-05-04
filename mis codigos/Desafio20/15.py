tienda = {
    "pocion": {"precio": 50, "stock": 3},
    "espada": {"precio": 200, "stock": 1},
}
capital_total = 0
for producto in tienda:
    capital_total += tienda[producto]["precio"] * tienda[producto]["stock"]
print(capital_total)