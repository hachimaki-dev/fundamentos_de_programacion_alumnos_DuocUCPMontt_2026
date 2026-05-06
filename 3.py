personas = 5
precio_pichanga = 15000
cantidad_de_pichangas = 2
precio_shop = 3500
cantidad_de_shop = 5 

total = (precio_pichanga * cantidad_de_pichangas) + (precio_shop * cantidad_de_shop)

total_con_propina = total * 1.10

pago_por_persona = total_con_propina / personas 
print(pago_por_persona)