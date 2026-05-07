carrito = [{"item" : "Mouse",
            "qty" : 2,
            "precio" : 15000},
            
            {"item" : "Teclado",
            "qty" : 1,
            "precio" : 30000}]

precio_total = 0

for objeto in carrito :
    precio_total += objeto["qty"] * objeto["precio"]

if precio_total > 50000 :
    precio_total *= 0.9

print(precio_total)