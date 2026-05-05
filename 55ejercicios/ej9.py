# Ejercicio 9: Costos de Producción (Emprendimiento)

print("Ejercicio 9: Costos de Producción")

precio_venta = 15000
tela = 4000
estampado = 2500
empaque = 500
poleras_vendidas = 50

costo_total = tela + estampado + empaque
ganancia_por_polera = precio_venta - costo_total
ganancia_mensual = ganancia_por_polera * poleras_vendidas

print(ganancia_mensual)