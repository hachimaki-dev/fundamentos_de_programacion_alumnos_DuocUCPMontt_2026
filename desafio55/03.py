precio_pichanga = 15000
precio_schop = 3500
cantidad_pichanga = 2
cantidad_schop = 5
asistentes = 5
porcentaje_propina = 10

consumo_total = (precio_pichanga * cantidad_pichanga) + (precio_schop * cantidad_schop)
total_grupal = consumo_total + (consumo_total / 100 * porcentaje_propina)
total_individual = total_grupal / 5

print(total_individual)
