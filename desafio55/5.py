tarjeta = 10000
pasaje_micro = 730
pasaje_metro = 850
recarga = 3000

por_el_dia = tarjeta - pasaje_micro - pasaje_metro - pasaje_metro

despues_de_la_recarga = por_el_dia + recarga

print(f"total al final de dia es {despues_de_la_recarga}")