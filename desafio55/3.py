personas_totales = 5
cantidad_pichangas = 2
precio_pichangas = 15000 
cantidad_schops = 5
precio_schops = 3500

total_sin_propina = (precio_pichangas * cantidad_pichangas) + (precio_schops * cantidad_schops)
propina = total_sin_propina*10/100
total_con_propina = total_sin_propina + propina

division_entre_personas = total_con_propina/5
print(division_entre_personas)


