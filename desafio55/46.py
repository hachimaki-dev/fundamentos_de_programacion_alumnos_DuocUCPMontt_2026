ventas = {"LocalA": 150, "LocalB": 300, "LocalC": 100}
total_ganancias = 0 
for ganancia in ventas.values():
    total_ganancias += ganancia

print(total_ganancias)