polera = 15000
tela = 4000
estampado = 2500
empaque = 500

unidades_vendidas = 50

costo_total_unitario = tela + estampado + empaque
costo_por_unidad = polera - costo_total_unitario
ganancia_mensual = costo_por_unidad * unidades_vendidas

print(ganancia_mensual)


