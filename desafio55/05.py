saldo_en_tarjeta = 10000
precio_pasaje_micro = 730
precio_metro_punta = 850

saldo_en_tarjeta = saldo_en_tarjeta - precio_pasaje_micro - (precio_metro_punta * 2)

saldo_en_tarjeta = saldo_en_tarjeta + 3000 # Recarga

print(saldo_en_tarjeta)
