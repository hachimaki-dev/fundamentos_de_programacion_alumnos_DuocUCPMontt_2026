pichangas = 2 * 15000
schops = 5 * 3500

total_con_propina = (pichangas + schops) * 1.10

pago_por_persona = total_con_propina / 5


### AGREGUE UN "ROUND" PARA REDONDEAR ###
print(round(pago_por_persona, 1))

