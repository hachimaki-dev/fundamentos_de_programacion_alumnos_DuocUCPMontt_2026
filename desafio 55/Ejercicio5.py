tarjeta_bip = 10000
pasaje_micro = 730
pasaje_metro = 850
recarga = 3000

print(f"En el dia tome una micro (${pasaje_micro}CLP) y 2 metros (${pasaje_metro * 2}CLP)")
tarjeta_bip = tarjeta_bip - pasaje_micro - (pasaje_metro * 2)
print(f"Mi tarjeta bip quedo con ${tarjeta_bip}CLP")
tarjeta_bip = tarjeta_bip + recarga
print(f"A mi tarjeta bip le recargue ${recarga}CLP, en total mi tarjeta bip quedo con ${tarjeta_bip}CLP")