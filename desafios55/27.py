ventas = [1500, -200, 5000, 0, 100]
total_ventas = 0

for venta in ventas:
    if venta <=0:
        continue
    
    total_ventas += venta
    
print(total_ventas)
    
    


