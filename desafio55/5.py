tarjeta = 10000
pasaje_micro = 730
pasaje_metro = 850
recarga = 3000

costo_dia = tarjeta - pasaje_micro - (pasaje_metro * 2)
tarjeta = costo_dia + recarga 
print(tarjeta)

