tarjeta = 10000
pasaje_micro = 730
pasaje_metro = 850
recarga = 3000

tarjeta = tarjeta - pasaje_micro

tarjeta = tarjeta - pasaje_metro*2

tarjeta_final = tarjeta + recarga

print(tarjeta_final)