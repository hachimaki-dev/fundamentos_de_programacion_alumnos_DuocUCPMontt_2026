ventas_dia = [1500, -200, 5000, 0, 100]
total_dia = 0
for venta in ventas_dia:
    if venta >0:
        total_dia += venta
    elif venta <= 0:
        continue
    else:
        print("error")

print(f"Total en las ventas del dia es de ${total_dia}")