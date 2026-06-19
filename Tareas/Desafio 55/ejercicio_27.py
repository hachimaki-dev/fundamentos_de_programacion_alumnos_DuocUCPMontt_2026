# Saltar Errores del Sistema (Kiosko)


ventas = [1500, -200, 5000, 0, 100]  # vemtas del dia
total = 0 # Cantidad de dinero ganado

for venta in ventas:
    
    if venta <= 0:
        continue
    total += venta

print('Total limpio: ', total )    
