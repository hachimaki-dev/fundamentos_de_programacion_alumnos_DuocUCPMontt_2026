saldo_tarjeta_BIP = 10000

pasaje_micro = 730

pasaje_metro = 850

recarga = 3000

dia_1 = saldo_tarjeta_BIP - pasaje_micro - pasaje_metro * 2 + recarga

print(f"el saldo de la tarjeta BIP al final del dia es de {dia_1}")