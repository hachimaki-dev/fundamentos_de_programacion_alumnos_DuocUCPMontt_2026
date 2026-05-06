saldo_bip = 10000
costo_micro = 730
costo_metro = 850
recarga = 3000

#dia 1

saldo_bip_restante = saldo_bip - costo_micro
saldo_bip_restante = saldo_bip_restante - costo_metro - costo_metro
print (saldo_bip_restante)

saldo_bip_restante = saldo_bip_restante + recarga
print (f"su saldo bip restante es de {saldo_bip_restante}")