tienda = {
    "poción": {"precio": 50, "stock": 3},
    "espada": {"precio": 200, "stock": 1}
}
capital_total = 0
uno = tienda["espada"]["precio"] * tienda["espada"]["stock"]
capital_total = tienda["poción"]["precio"] * tienda["poción"]["stock"]
capital_total += uno
print(capital_total)