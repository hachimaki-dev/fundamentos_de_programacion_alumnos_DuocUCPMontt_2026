tarjeta_bip = 10000
pasaje_micro = 730
pasaje_metro = 850
recarga = 3000

tarjeta_bip = tarjeta_bip - (pasaje_metro * 2) - pasaje_micro + recarga
print(tarjeta_bip)
