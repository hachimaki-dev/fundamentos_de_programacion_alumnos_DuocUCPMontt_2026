polera = 15000
tela = 4000
estampado = 2500
empaque = 500
venta = 50

costo = tela + estampado + empaque
ganancia_polera = polera - costo
ganancia_mes = ganancia_polera * venta

print(f"Ganancia mensual: ${ganancia_mes}")