monto_tarjeta_bip=10000
pasaje_micro=730
pasaje_metro=850
recarga=3000

actividades_tarjeta = (monto_tarjeta_bip - pasaje_micro) - (pasaje_metro*2)

saldo_nuevo= actividades_tarjeta + recarga

print(saldo_nuevo)

