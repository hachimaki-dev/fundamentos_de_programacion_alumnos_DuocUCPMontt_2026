ventas_total_dia = [1500, -200, 5000, 0, 100]
total = 0

for ventas in ventas_total_dia:
    if ventas <= 0: continue
    total += ventas

print(total)