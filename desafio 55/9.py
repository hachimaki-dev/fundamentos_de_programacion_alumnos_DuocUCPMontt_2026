venta_poleras = 15000
precio_tela = 4000
precio_estampado = 2500
empaque = 500
cantidad_vendidas = 50

costo_total_unidad = precio_tela + precio_estampado + empaque
ganancia_por_unidad = venta_poleras - costo_total_unidad
ganacia_mensual = ganancia_por_unidad * cantidad_vendidas 

print(f"la ganancia mensual final es: {ganacia_mensual}")