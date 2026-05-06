precio_venta = 15000
costo_tela = 4000
costo_estampado = 2500
costo_empaque = 500
poleras_vendidas = 50

costo_total_por_polera = costo_tela + costo_estampado + costo_empaque

ganancia_por_polera = precio_venta - costo_total_por_polera

ganancia_mensual = ganancia_por_polera * poleras_vendidas

print(f"La ganancia es de {ganancia_mensual} mensuales")