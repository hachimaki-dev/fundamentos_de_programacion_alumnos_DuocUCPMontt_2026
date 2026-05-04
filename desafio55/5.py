tarjeta_bip = 10000
pasaje_micro = 730
pasaje_metro = 850
recarga = 3000
gasto_primer_dia = pasaje_micro + (pasaje_metro * 2)
monto_restante = tarjeta_bip - gasto_primer_dia
print(gasto_primer_dia)
recarga_tarjeta = monto_restante + recarga
print(recarga_tarjeta)