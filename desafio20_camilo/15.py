tienda = {
    "Pocion" : {"Precio" : 50, "Stock" : 3},
    "Espada" : {"Precio" : 200, "Stock" : 1}
}

capital_total = 0

for objeto in tienda.values() :
    capital_total += objeto["Precio"] * objeto["Stock"]

print(capital_total)