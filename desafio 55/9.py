precio_venta = 15000
costo_tela = 4000
costo_estampado = 2500
costo_empaque = 500
poleras_vendidas = 50

ganancia_unitaria = precio_venta - costo_tela - costo_estampado - costo_empaque
ganancia_mensual = ganancia_unitaria * poleras_vendidas

print(f"ganancia al final del mes: {ganancia_mensual}")