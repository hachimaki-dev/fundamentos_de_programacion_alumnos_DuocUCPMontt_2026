polera = 15000
hacer_polera = 4000
estampado = 2500
empaque = 500
vendidas = 50

costo_hacer_polera = hacer_polera + estampado + empaque
ganado_unidad_con_el_descuento = polera - costo_hacer_polera

total_ganado_mes = ganado_unidad_con_el_descuento * 50

print(f"ganancia mensual {total_ganado_mes}")

