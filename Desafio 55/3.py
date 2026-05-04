personas = 5

pichangas_compradas = 2
schops_comprados = 5

precio_pichanga = 15000
precio_schop = 3500

gasto_consumo = (pichangas_compradas * precio_pichanga) + (schops_comprados * precio_schop)
costo_propina = gasto_consumo * 0.1

monto_final = gasto_consumo + costo_propina

monto_por_persona = monto_final / personas

print(monto_por_persona)