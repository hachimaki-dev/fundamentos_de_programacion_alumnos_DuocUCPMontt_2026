ventas_del_dia = [1500, -200, 5000, 0, 100]
total = 0
for suma in ventas_del_dia:
    if suma <= 0:
        continue
    total = total + suma
print(total)