ventas_diarias = [1500 , -200 , 5000 , 0 , 100]
total_diario = 0
total = 0 
for total_diario in ventas_diarias:
    if total_diario < 0:
        continue
    else:
        total = total_diario + total 
        print(f"su venta total fue :{total}")