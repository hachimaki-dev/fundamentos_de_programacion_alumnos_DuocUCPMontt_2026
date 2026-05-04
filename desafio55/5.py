saldo_tarjeta = 10000
pasaje_micro = 730 
pasaje_metro = 850
recarga = 3000


saldo_tarjeta -= pasaje_micro
saldo_tarjeta -= pasaje_metro*2


saldo_tarjeta += recarga
print(saldo_tarjeta)