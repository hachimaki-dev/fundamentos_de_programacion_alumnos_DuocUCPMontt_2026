Tarjeta_bip = 10000
pasaje_micro = 730
pasaje_metro = 850
recarga = 3000

pago_diario = Tarjeta_bip - pasaje_metro * 2 - pasaje_micro
saldo_total = pago_diario + recarga

print(saldo_total)