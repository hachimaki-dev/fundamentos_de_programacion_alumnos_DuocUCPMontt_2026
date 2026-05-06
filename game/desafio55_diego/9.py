precio_venta = 15000
costo_tela = 4000
costo_estampado = 2500
costo_empaque = 500
cantidad_vendida = 50

costo_unitario = costo_tela + costo_estampado + costo_empaque
ganancia_unitaria = precio_venta - costo_unitario
ganancia_mensual = ganancia_unitaria * cantidad_vendida

print(ganancia_mensual)