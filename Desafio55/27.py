ventas_del_dia=[1500, -200, 5000, 0, 100]
ventas_totales=0
for x in ventas_del_dia:
    if x<=0:
        continue
    else:
        ventas_totales+=x
print(ventas_totales)