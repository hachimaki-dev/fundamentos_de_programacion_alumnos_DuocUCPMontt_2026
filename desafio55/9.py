valor_venta_polera = 15000
valor_tela_polera = 4000
valor_estampado_polera = 2500
valor_empaque_polera = 500
ganancia_por_polera = valor_venta_polera - (valor_tela_polera + valor_empaque_polera + valor_estampado_polera)
poleras_vendidas_mes = 50
ganancia_mes = poleras_vendidas_mes * ganancia_por_polera
print(f"Ganancia del mes {ganancia_mes} pesos")
