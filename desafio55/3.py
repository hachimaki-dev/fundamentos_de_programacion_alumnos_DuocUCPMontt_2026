#Repartiendo la Cuenta en el Bar
personas = 5
pichangas = 15000
schops = 3500
propina = 10



consumo_total = (pichangas * 2 ) + (schops * 5)
total_propina = consumo_total * propina / 100
monto_final = consumo_total + total_propina

pago_individual = monto_final / 5

print(pago_individual)