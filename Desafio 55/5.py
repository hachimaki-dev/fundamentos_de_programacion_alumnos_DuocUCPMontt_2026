saldo_inicial_tarjeta = 10000
saldo_actual_tarjeta = saldo_inicial_tarjeta

costo_micro = 730 
costo_metro = 850

cantidad_recarga = 3000

saldo_actual_tarjeta -= costo_micro + (costo_metro * 2) 
saldo_actual_tarjeta += cantidad_recarga

print(saldo_actual_tarjeta)