cantidad_personas = 5
cantidad_pichangas = 2
precio_pichanga = 15000
cantidad_shops= 5
precio_shops = 3500
propina = 0.10

total_pichangas = cantidad_pichangas * precio_pichanga
total_shops = cantidad_shops * precio_shops
total_consumo = total_pichangas + total_shops

valor_propina = total_consumo * propina 
total_con_propina = total_consumo + valor_propina

pago_por_persona = total_con_propina // cantidad_personas

print(f"lo que debe pagar cada uno es {pago_por_persona}")

