precio_polera = 15000
tela = 4000
estampado = 2500
empaque = 500
total_ventas_en_el_mes = 50
ganancia_x_polera = precio_polera - (tela+estampado+empaque)
ganancia_total = ganancia_x_polera * total_ventas_en_el_mes
print(f"La ganancia del mes es de {ganancia_total}.")