polera_precio_final = 15000
tela_polera = 4000
estampado_polera = 2500
empaque_polera = 500
total_poleras_vendidas_mes = 50

ganancia = polera_precio_final - (tela_polera + estampado_polera + empaque_polera)
ganancia = ganancia * total_poleras_vendidas_mes
print(f"Las ganancias registradas son de: {ganancia}")