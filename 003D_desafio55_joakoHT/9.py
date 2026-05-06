poleras = 15000
tela = 4000
estampado = 2500
empaque = 500
p_vendidas = 50

costo_total = (tela + estampado + empaque)
ganancia_por_polera = (poleras - costo_total)
ganancia_total = (ganancia_por_polera * p_vendidas)

print(ganancia_total)