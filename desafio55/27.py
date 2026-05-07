ventas_dia = [1500, -200, 5000, 0 ,100]
total_Ventas = 0
for ventas in ventas_dia:
    if ventas <= 0:
        continue 
    total_Ventas = total_Ventas + ventas
    
print(total_Ventas)