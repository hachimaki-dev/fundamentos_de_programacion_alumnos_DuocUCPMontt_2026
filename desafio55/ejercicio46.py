ventas = {"LocalA": 150,
          "LocalB": 300,
          "LocalC": 100}
ventas_total = ventas.values()
total_dinero = 0
for i in ventas_total:
    total_dinero = total_dinero + i
    
print(total_dinero)
