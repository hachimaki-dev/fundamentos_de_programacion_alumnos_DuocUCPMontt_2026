saldo_bip = 10000
costo_micro =  730
metro_punta = 850
recarga = 3000
saldo_bip -= costo_micro
saldo_bip = saldo_bip - (metro_punta * 2)
saldo_bip += recarga
print(saldo_bip)
