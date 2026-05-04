personas = 5

cant_pichangas = 2
precio_pichanga = 15000

cant_schops = 5
precio_schop = 3500

consumo_total = (cant_pichangas * precio_pichanga) + (cant_schops * precio_schop)

total_pagar = consumo_total + (consumo_total*0.1)

pago_x_persona = total_pagar / personas

print(pago_x_persona)