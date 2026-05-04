precio_auto = 5000000
ahorros = 1500000
cantidad_a_ahorrar_cada_mes = 150000
dinero_faltante = precio_auto - ahorros
print(f"Te faltan {dinero_faltante} mil pesos para el auto.")
meses_para_juntar_el_dinero_restante = dinero_faltante//cantidad_a_ahorrar_cada_mes
print(f"Te demorarás {meses_para_juntar_el_dinero_restante} meses para juntar lo que te falta.")