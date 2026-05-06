ventas = [1500, -200, 5000, 0, 100]
total = 0

for venta in ventas:
    
    if venta <= 0:
        continue  
    

    total += venta

print(f"La suma total limpia es: {total}")
