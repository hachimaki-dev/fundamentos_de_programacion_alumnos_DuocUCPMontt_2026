precio_pichanga = 15000
cantidad_pichangas = 2

precio_schop = 3500
cantidad_schops = 5

personas = 5

consumo = (precio_pichanga * cantidad_pichangas) + (precio_schop * cantidad_schops)

propina = consumo * 0.10
monto_final = consumo + propina
pago_por_persona = monto_final / personas

print(pago_por_persona)
