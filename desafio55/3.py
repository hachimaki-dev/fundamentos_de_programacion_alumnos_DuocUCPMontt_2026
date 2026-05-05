personas = 5
pichanga = 2
precio_pichanga = 15000
schops = 5
precio_schop = 3500

total_comida = pichanga * precio_pichanga
total_bebida = schops * precio_schop
consumo_total = total_comida + total_bebida

propina = consumo_total * 0.1
total_a_pagar = consumo_total + propina
pago_por_persona = total_a_pagar // personas

print("Total a pagar por persona: ", pago_por_persona)