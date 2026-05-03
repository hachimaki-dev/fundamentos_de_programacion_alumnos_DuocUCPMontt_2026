tienda = {
    "pocion": {"precio": 50, "stock": 3},
    "espada": {"precio": 200, "stock": 1}
}
capital_valor = 0
for p in tienda:
    precio = tienda[p]["precio"]
    stock = tienda[p]["stock"]
    capital_valor += precio * stock
print(capital_valor)
