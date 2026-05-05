polera_unidad = 15000
costo_polera = 4000
estampado = 2500
empaque = 500
poleras_al_mes = 50

ganancia = polera_unidad - (costo_polera + estampado + empaque)
ganancia_del_mes = ganancia * poleras_al_mes

print(ganancia_del_mes)

