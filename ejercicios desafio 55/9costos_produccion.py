valor_polera = 15000
valor_tela = 4000
valor_estampado = 2500
valor_empaque = 500 
vendidas_mes = 50
ganancia_polera = valor_polera - valor_tela - valor_empaque - valor_estampado
ganancia_mes = ganancia_polera * vendidas_mes
print(ganancia_mes)