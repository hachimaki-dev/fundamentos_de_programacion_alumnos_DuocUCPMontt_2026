tarjeta = 10000 
pasaje_micro = 730 
pasaje_metro = 850 
recarga = 3000

total_dia = pasaje_micro + (pasaje_metro * 2)

final_dia = tarjeta - total_dia + recarga 
print(final_dia)