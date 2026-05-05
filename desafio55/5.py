sueldo_tarjeta = 10000
pasaje_micro = 730
pasaje_metro = 850
recarga = 3000
sueldo_tarjeta = sueldo_tarjeta - pasaje_micro - (pasaje_metro*2) + recarga
print(f"Tu saldo actual es de {sueldo_tarjeta}")