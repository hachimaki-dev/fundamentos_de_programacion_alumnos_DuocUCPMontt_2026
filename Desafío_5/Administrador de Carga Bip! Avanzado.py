tarjeta = 10000
pasaje = 730 
metro = 850
recarga = 3000
saldo_final_del_dia = 0


tarjeta = (tarjeta - pasaje * 1) 
tarjeta = (tarjeta - metro * 2)
tarjeta = (tarjeta + recarga)  
saldo_final_del_dia = tarjeta
print (f"El saldo final del día es de ${saldo_final_del_dia}")
