personas = 5
pichangas = 2 * 15000
schops = 5 * 3500

total = pichangas + schops
total_con_propina = total * 1.10
pago_por_persona = total_con_propina // personas
print(pago_por_persona)
