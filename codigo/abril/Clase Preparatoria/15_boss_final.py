capital_total = 0
tienda = {
        "Poción":   { "Precio": 50, "Stock": 3 },
        "Espada":   { "Precio": 200, "Stock": 1 },
        "Escudo":   { "Precio": 150, "Stock": 2 }
}

for i in tienda.values():
    capital_total = capital_total + (i["Precio"] * i["Stock"])

print(capital_total)
