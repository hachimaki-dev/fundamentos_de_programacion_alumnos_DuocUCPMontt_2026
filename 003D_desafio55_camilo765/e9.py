precio_venta = 15000
costo_tela = 4000
costo_estampado = 2500
costo_empaque = 500
cantidad = 50

costo_total = costo_tela + costo_estampado + costo_empaque
ganancia_unitaria = precio_venta - costo_total
ganancia_mensual = ganancia_unitaria * cantidad

print(ganancia_mensual)
