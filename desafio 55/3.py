personas = 5
pichangas = 2 * 15000
schops = 5 * 3500

total_consumo = pichangas + schops
propina = total_consumo * 0.10

total_final = total_consumo + propina
pago_por_persona = total_final / personas

print(pago_por_persona)