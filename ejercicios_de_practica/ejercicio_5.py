tarjeta_bip = 10000
pasaje_en_micro = 730
pasaje_en_metro = 850

tarjeta_bip = (tarjeta_bip - ((pasaje_en_micro) + (pasaje_en_metro * 2))) + 3000
print(tarjeta_bip)