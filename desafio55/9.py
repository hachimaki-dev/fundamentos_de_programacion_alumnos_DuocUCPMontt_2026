valor_por_polera = 15000
tela = 4000
estampado = 2500
empaque = 500
poleras_vendidas = 50
mano_de_obra = tela + estampado + empaque
ganacia_por_polera = valor_por_polera - mano_de_obra
ganancia_del_mes = ganacia_por_polera * poleras_vendidas
print(ganancia_del_mes)
